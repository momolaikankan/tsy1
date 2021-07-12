# coding: utf-8
import os
import json
import logging
import glob
import numpy as np
from scipy import spatial
import os
import scipy

from virtual_stream_task.utils.common import check_file_or_dir_exist
from virtual_stream_task.utils.cgtw_api_wrapper import CGTW_API_INSTANCE
from virtual_stream_task.utils.maya.maya_help import ctrl_to_maya
from virtual_stream_task.utils.maya.maya_help import maya_to_ctrl

LOGGER = logging.getLogger('okra_slave')


def save_mouth_data_to_ctrl_file(mouth_data, ctrl_path):
    t_mouth_data = mouth_data.tolist()
    with open(ctrl_path, 'w') as f:
        json.dump({'Mouth_Params': t_mouth_data, 'Eyes_Params': [], 'Brows_Params': []}, f)


def getValidIndices(json_path, type_name):
    with open(json_path, 'r') as f:
        content = json.load(f)
    # indices = content[f'{type_name}_valid_indices']
    indices = content['{}_valid_indices'.format(type_name)]
    mu = np.array(content['{}_mean'.format(type_name)]).reshape((1, -1)).astype(np.float32)
    std = np.array(content['{}_std'.format(type_name)]).reshape((1, -1)).astype(np.float32)
    return indices, mu, std


def get_train_data(ada_dir, char_dir, prefix):
    name_list = [t_name for t_name in os.listdir(char_dir) if t_name.endswith('.ctrl')]
    char_data_list = []
    ada_data_list = []
    for t_name in name_list:
        char_path = os.path.join(char_dir, t_name)
        with open(char_path, 'r') as f:
            char_data_list.append(np.array(json.load(f)['Mouth_Params']))
        ada_path = os.path.join(ada_dir, t_name.replace(prefix, '')[:-5] + '.npy')
        ada_data_list.append(np.load(ada_path))
    char_data = np.vstack(char_data_list)
    ada_data = np.vstack(ada_data_list)
    return char_data, ada_data


def farthest_sampling_boost(features, k):
    mean_f = np.mean(features, axis=0)
    t_diff = np.square((features - mean_f)).sum(axis=1)
    t_idx = t_diff.argmin()
    indices = [t_idx]
    remidx = list(range(0, features.shape[0]))
    del remidx[t_idx]
    D = spatial.distance.cdist(features[remidx, :], features[indices, :])
    while len(indices) < k:
        d = np.amin(D, axis=1)
        id = np.argmax(d)
        indices.append(remidx[id])
        del remidx[id]
        D_temp = spatial.distance.cdist(features[remidx, :], features[indices[-1], None])
        D = np.delete(D, id, axis=0)
        D = np.hstack([D, D_temp])
    return indices


def rbf_train(X, Y, t_lambda, t_sigma):
    M, N = X.shape
    C = Y.shape[1]
    A = np.zeros((2 * M, M))
    b = np.zeros((2 * M, C))
    for i in range(M):
        A[i, :] = np.exp(-0.5 * np.sum(np.square(X[i, :] - X), axis=1) / (t_sigma * t_sigma))
    b[:M, :] = Y
    A[M:, :] = t_lambda * np.eye(M)
    # try:
    #     W = scipy.linalg.lstsq(A, b)[0]
    # except np.linalg.LinAlgError as err:
    #     print(err)
    #     W = np.ones((M, C))
    W = scipy.linalg.lstsq(A.transpose().dot(A), A.transpose().dot(b))[0]
    return W


def rbf_test(X, X_train, t_sigma, W):
    M = X_train.shape[0]
    A = np.zeros((X.shape[0], M))
    for i in range(X.shape[0]):
        A[i, :] = np.exp(-0.5 * np.sum(np.square(X[i, :] - X_train), axis=1) / (t_sigma * t_sigma))
    y = A.dot(W)
    return y


# def predict(char_data, ada_data, unfinished_dict):
#     valid_ada_indices, _, _ = getValidIndices(
#         r'S:\users\jinshihao\code\FaceRetarget\data_sta_ada\data_cfg.json',
#         'mouth'
#     )
#     mgj_mu = np.mean(char_data, axis=0, keepdims=True)
#     mgj_std = np.std(char_data, axis=0, keepdims=True)
#     valid_mgj_indices = (mgj_std > 1e-4).nonzero()[1].tolist()
#
#     train_ada_data = ada_data[:, valid_ada_indices]
#     train_mgj_data = char_data[:, valid_mgj_indices]
#     # ### hyperparameter1
#     K = 500
#     t_sigma = 0.9
#     t_lambda = 0.1
#     selected_indcies = farthest_sampling_boost(train_ada_data, K)
#     train_X = train_ada_data[selected_indcies, :]
#     mean_Y = np.mean(train_mgj_data, axis=0).reshape((1, -1))
#     train_Y = train_mgj_data[selected_indcies, :] - mean_Y
#
#     W = rbf_train(train_X, train_Y, t_lambda, t_sigma)
#
#     ### test in folder
#     # test_path_list = [
#     #     os.path.join(r'S:\users\jinshihao\code\FaceRetarget\data_sta_ada\all\mouth', '{}.npy'.format(t_name)) for t_name
#     #     in unfinished_dict.keys()
#     # ]
#     #
#     # save_path_list = [
#     #     os.path.join(dir_path, '{}.ctrl'.format(full_name)) for dir_path, full_name in unfinished_dict.values()
#     #
#     # ]
#     # for t_path, save_path in zip(test_path_list, save_path_list):
#     #     t_ada_data = np.load(t_path)
#     #     y = rbf_test(t_ada_data[:, valid_ada_indices], train_X, t_sigma, W) + mean_Y
#     #     predicted_y = np.zeros((t_ada_data.shape[0], mgj_mu.shape[1]))
#     #     predicted_y += mgj_mu
#     #     predicted_y[:, valid_mgj_indices] = y
#     #     save_mouth_data_to_ctrl_file(predicted_y, save_path)
#     for shot_name, ctrl_file_path in unfinished_dict.items():
#         test_path = os.path.join(r'S:\users\jinshihao\code\FaceRetarget\data_sta_ada\all\mouth', '{}.npy'.format(shot_name))
#         t_ada_data = np.load(test_path)
#         y = rbf_test(t_ada_data[:, valid_ada_indices], train_X, t_sigma, W) + mean_Y
#         predicted_y = np.zeros((t_ada_data.shape[0], mgj_mu.shape[1]))
#         predicted_y += mgj_mu
#         predicted_y[:, valid_mgj_indices] = y
#         save_mouth_data_to_ctrl_file(predicted_y, ctrl_file_path)


# def expression_prediction_task(proj_db, task_id, module_type, module):
#     char_data_list = []
#     ada_data_list = []
#     unfinished_dict = {}
#     try:
#         CGTW_API_INSTANCE.change_task_autotask_status(proj_db, [task_id], 'PredictIng', module=module)
#         #获取apporve ctrl 数据
#         task = CGTW_API_INSTANCE.common_get_one_item(
#             proj_db, module, module_type, {'task.id': task_id},
#             fields=['eps.entity', 'seq.entity', 'shot.entity', 'task.status']
#         )
#         if task.task_status != 'Wait':
#             raise ValueError('任务状态不是 Wait')
#         prediction_ctrl_info = get_ctrl_files(proj_db, task.eps_entity, task.seq_entity)
#         for shot_entity, one_ctrl_path in prediction_ctrl_info.items():
#             with open(one_ctrl_path, 'r') as f:
#                 char_data_list.append(np.array(json.load(f)['Mouth_Params']))
#             ada_dir = r'S:\users\jinshihao\code\FaceRetarget\data_sta_ada\all\mouth'
#             ada_path = os.path.join(ada_dir, '{}.npy'.format(shot_entity))
#             ada_data_list.append(np.load(ada_path))
#         char_data = np.vstack(char_data_list)
#         ada_data = np.vstack(ada_data_list)
#         #得到预测ctrl
#         prediction_ctrl_dir = CGTW_API_INSTANCE.get_filebox_info(proj_db, module, module_type, task_id, 'origin_data')['path']
#         ctrl_file_path = '{}_{}_{}.ctrl'.format(task.eps_entity, task.seq_entity, task.shot_entity)
#         prediction_ctrl_path = os.path.join(prediction_ctrl_dir, ctrl_file_path)
#         unfinished_dict[task.shot_entity] = prediction_ctrl_path
#         predict(char_data, ada_data, unfinished_dict)
#         #预测ctrl转maya
#         char_asset_cfg_task = CGTW_API_INSTANCE.common_get_item_one_link_item(
#             proj_db, module, module_type, {'task.id': task_id}, 'asset', 'task',
#             {'asset.link_asset_type': 'char', 'pipeline.entity': 'FaceRetarget'},
#             link_item_fields=['task.id']
#         )
#         cfg_dir = CGTW_API_INSTANCE.get_filebox_info(
#             proj_db, 'asset', 'task', char_asset_cfg_task.task_id, 'approve')['path']
#         cfg_file_path = glob.glob(os.path.join(cfg_dir, '*.cfg'))[0]
#
#         char_asset_rig_task = CGTW_API_INSTANCE.common_get_item_one_link_item(
#             proj_db, module, module_type, {'task.id': task_id},  'asset', 'task',
#             {'asset.link_asset_type': 'char', 'pipeline.entity': 'Rig'},
#             link_item_fields=['task.id', 'asset.rig_path', 'asset.entity']
#         )
#         asset_rig_path = char_asset_rig_task.asset_rig_path
#
#         ref_namespace = char_asset_rig_task.asset_entity
#         save_maya_path = prediction_ctrl_path.replace('.ctrl', '_auto.ma')
#         face_video_dir = CGTW_API_INSTANCE.get_filebox_info(proj_db, module, module_type, task_id, 'face_video')['path']
#         audio_path = glob.glob(os.path.join(face_video_dir, '*.wav'))[0]
#         start_image_path = glob.glob(os.path.join(face_video_dir, '*feature', '*detail', 'images', '*.0.jpg'))[0]
#         check_file_or_dir_exist([prediction_ctrl_path, cfg_file_path, asset_rig_path, start_image_path, audio_path])
#         ctrl_to_maya(
#             prediction_ctrl_path, cfg_file_path, asset_rig_path, ref_namespace, 60, save_maya_path, audio_path,
#             start_image_path
#         )
#         CGTW_API_INSTANCE.change_task_autotask_status(proj_db, [task_id], 'PredictDone', module=module)
#
#     except Exception as e:
#         LOGGER.error("expression_prediction_task error, proj %s task_id %s", proj_db, task_id, exc_info=True)
#         CGTW_API_INSTANCE.change_task_autotask_status(proj_db, [task_id], 'PredictError', module, str(e))

def mytest():
    tasks = CGTW_API_INSTANCE.common_get_items('proj_digitalman_zj_ggl', 'shot', 'task',
                                                 {'eps.entity': 'train', 'seq.entity': 'GGL', 'task.status': 'Approve', 'pipeline.entity': 'Animation'},
                                                 fields=['task.id', 'shot.entity'])
    print(tasks)
    # for i in tasks:
    #     print(i.shot_entity,'---', i.task_id)

def get_ctrl_files(proj_db, eps, seq):
    prediction_ctrl_info = {}
    ctrl_tasks = CGTW_API_INSTANCE.common_get_items(
        proj_db, 'shot', 'task',
        {
            'eps.entity': eps,
            'seq.entity': seq,
            'task.status': 'Approve',
            'pipeline.entity': 'FaceTrain'
        },
        fields=['task.id', 'shot.entity']
    )
    if not ctrl_tasks:
        raise ValueError('获取不到Approve 状态')
    for task in ctrl_tasks:
        prediction_ctrl_dir = CGTW_API_INSTANCE.get_filebox_info(proj_db, 'shot', 'task', task.task_id, 'current_role_ctrl_data')[
        'path']
        prediction_ctrl_path = glob.glob(os.path.join(prediction_ctrl_dir, '*.ctrl'))
        if not prediction_ctrl_path:
            continue
        prediction_ctrl_info[task.shot_entity] = prediction_ctrl_path[0]
    return prediction_ctrl_info


if __name__ == '__main__':
    mytest()
