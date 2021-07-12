# coding: utf-8
import os
import sys
import logging
from virtual_stream_task.utils.maya.maya_api import MayaHelp
from virtual_stream_task.utils.cgtw_api_wrapper import CGTW_API_INSTANCE
from virtual_stream_task.utils.common import mapping_drive
from mayatools.mayautil import delete_keys

LOGGER = logging.getLogger('okra_slave')

#
# def delete_references(references):
#     for i in references:
#         i.remove()


def import_anim(atom_filename, dstTime=None):
    MayaHelp.cmds.loadPlugin("atomImportExport.mll")
    dstTimeStr = ""
    if dstTime is not None:
        dstTimeStr = "dstTime=%s" % dstTime

    MayaHelp.cmds.file(
        atom_filename, i=True, type="atomImport", ra=True,
        options=";;targetTime=1;%s;option=insert;match=string;;selected=childrenToo;search=;replace=;prefix=;suffix=;" %dstTimeStr
    )


def get_root_cv(namespace=None):
    if namespace:
        rigs = MayaHelp.pm.ls(regex=r"{}.+".format(namespace), type="nurbsCurve")
    else:
        rigs = MayaHelp.pm.ls(type="nurbsCurve")
    rigs = [(i.longName().count("|"), i) for i in rigs if "FitSkeleton" not in i.nodeName()]

    rigs.sort(key=lambda x: x[0])
    return rigs[0][1].getParent()


# def export_atom_by_time(atom_filename, start_time, end_time):
#     atom_filename = atom_filename.replace("\\", "/")
#     MayaHelp.pm.loadPlugin("atomImportExport", quiet=True)
#     mel = 'file -force -options "precision=8;statics=0;baked=1;sdk=0;constraint=0;animLayers=0;selected=childrenToo;' \
#           'whichRange=2;range={}:{};hierarchy=none;controlPoints=0;useChannelBox=1;' \
#           'options=keys;copyKeyCmd=-animation objects -time >{}:{}> -float >{}:{}> -option keys -hierarchy none ' \
#           '-controlPoints 0 " -typ "atomExport" -es "{}";'.format(
#         start_time, end_time, start_time, end_time, start_time, end_time, atom_filename
#     )
#     print('export atom: {}'.format(mel))
#     MayaHelp.pm.mel.eval(mel)


def export_atom(atom_filename):
    atom_filename = atom_filename.replace("\\", "/")
    MayaHelp.pm.loadPlugin("atomImportExport", quiet=True)
    mel = 'file -force -options "precision=8;statics=0;baked=1;sdk=0;constraint=0;animLayers=0;selected=childrenToo;' \
          'whichRange=1;range=1:10;hierarchy=none;controlPoints=0;useChannelBox=1;' \
          'options=keys;copyKeyCmd=-animation objects -option keys -hierarchy none ' \
          '-controlPoints 0 " -typ "atomExport" -es "{}";'.format(atom_filename)
    MayaHelp.pm.mel.eval(mel)


def export_animation_atom(animation_filename):
    animation_data = {}
    MayaHelp.open_maya(animation_filename)
    ref_infos = MayaHelp.get_file_ref_infos()
    for ref_info in ref_infos:
        character_name = ref_info['ns']
        rig_filename = ref_info['ref']

        # 关键帧范围
        fkrootm_node = MayaHelp.pm.ls('{}:FKRoot_M'.format(character_name))[0]
        keyframe_index_list = MayaHelp.pm.keyframe(fkrootm_node, query=True)
        if not keyframe_index_list:
            raise ValueError('节点{}没有关键帧'.format(nurbs_curve_root_node.name()))

        # 导出atom
        nurbs_curve_root_node = get_root_cv(character_name)
        atom_filename = animation_filename.replace('.ma', '_{}.atom'.format(character_name))
        MayaHelp.pm.select(nurbs_curve_root_node)
        export_atom(atom_filename)

        animation_data[character_name] = {
            'rig_filename': rig_filename,
            'atom_filename': atom_filename,
            'time_range': (keyframe_index_list[0], keyframe_index_list[-1])
        }

    return animation_data


def merge_layout_and_animation_handler(layout_filename, animation_filenames, output_filename):
    #导出atom并获取动画文件的rig文件路径
    if not animation_filenames:
        raise ValueError('没有修复后maya文件')
    animation_data = {}
    for animation_filename in animation_filenames:
        ani_data = export_animation_atom(animation_filename)
        animation_data.update(ani_data)
    print('animation_data: {}'.format(animation_data))

    # 获取layout文件各个角色的时间偏移量
    MayaHelp.pm.openFile(layout_filename, pr=1, prompt=0, f=1, lrd="topOnly")
    layout_data = {}

    # 记录layout文件中角色的偏移量和引用文件
    fkroot_nodes = MayaHelp.pm.ls('*:FKRoot_M')

    if not fkroot_nodes:
        raise ValueError('没有找到FKRoot_M节点')

    time_span = None
    for node in fkroot_nodes:
        node_name = node.name()
        character = node_name.split(':')[0]
        keyframe_index_list = MayaHelp.pm.keyframe(node, query=True)
        if not keyframe_index_list:
            print('node {} has not keyframes'.format(node.name()))
            offset = 0
        else:
            offset = keyframe_index_list[0]

        character_rig_ref_node = MayaHelp.pm.ls('{}RN'.format(character), type='reference')[0]

        nurbs_curve_root_node = get_root_cv(character)
        layout_data[character] = {
            'time_offset': offset,
            'transform_offset': nurbs_curve_root_node.wm.get().translate.get(),
            'rotate_offset':  nurbs_curve_root_node.wm.get().rotate.get(),
            'rig_ref_node': character_rig_ref_node
        }

        if time_span is None:
            time_span = (keyframe_index_list[0], keyframe_index_list[-1])
        else:
            if keyframe_index_list[0] < time_span[0]:
                time_span = (keyframe_index_list[0], time_span[1])
            if keyframe_index_list[-1] > time_span[1]:
                time_span = (time_span[0], keyframe_index_list[-1])

    if not layout_data:
        raise ValueError('文件{}中没有FKRoot_M节点或节点上没有关键帧'.format(layout_filename))

    # 清理layout文件中的动画曲线
    print('layout data: {}'.format(layout_data))
    delete_keys(begin=time_span[0], end=time_span[1])

    for character in layout_data:
        if character not in animation_data:
            print('no atom to be imported for character: {}'.format(character))
            continue

        character_ani_data = animation_data[character]

        # 替换引用文件
        old_ref_path = os.path.normpath(layout_data[character]['rig_ref_node'].referenceFile().path)
        new_ref_path = os.path.normpath(os.path.normpath(character_ani_data['rig_filename']))
        if old_ref_path != new_ref_path:
            layout_data[character]['rig_ref_node'].replaceWith(
                new_ref_path.replace('\\', '/')
            )

        # 导入动画
        nurbs_curve_root_node = get_root_cv(character)
        MayaHelp.pm.select(nurbs_curve_root_node)
        import_anim(
            character_ani_data['atom_filename'],
            character_ani_data['time_range'][0] + layout_data[character]['time_offset']
        )

        # 恢复偏移
        nurbs_curve_root_node.setRotation(layout_data[character]['rotate_offset'])
        nurbs_curve_root_node.setTranslation(layout_data[character]['transform_offset'])

    MayaHelp.save_as(output_filename)


def merge_layout_and_animation(proj_db, task_id, module_type, module):
    try:
        mappings = CGTW_API_INSTANCE.get_project_diskmap(proj_db)
        if mappings:
            mapping_drive(mappings)
        tasks = CGTW_API_INSTANCE.get_shot_tasks(proj_db, task_id=task_id)
        if not tasks:
            raise ValueError('can not get shot task {}:{}'.format(proj_db, task_id))
        task = tasks[0]
        if task.task_pipeline != 'Layout':
            raise ValueError('请在阶段是：Layout 上发任务')

        LOGGER.info("begin merge_layout_and_animation_task {},集数:{} 场次{} 镜头号{},".format(proj_db, task.eps_entity, task.seq_entity, task.shot_entity))
        CGTW_API_INSTANCE.change_task_autotask_status(proj_db, [task_id], 'ImportAnimationIng', module=module)

        mocap_tasks = CGTW_API_INSTANCE.common_get_item_link_items(
            proj_db, module, module_type,
            {'eps.entity': task.eps_entity, 'seq.entity':  task.seq_entity, 'shot.entity':  task.shot_entity, 'pipeline.entity': 'Layout'},
            link_module='mocap', link_module_type='task', link_item_fields=['task.id']
        )
        layout_ma_file = CGTW_API_INSTANCE.download_filebox_files(
            proj_db, module, module_type, task_id, 'approve', '.', ['*.ma'], check_exist=True
        )[0]

        mocap_ma_files = []
        for mocap_task in mocap_tasks:
            _ma_files = CGTW_API_INSTANCE.download_filebox_files(
                proj_db, 'mocap', 'task', mocap_task.task_id, 'sync_maya', '.', ['*.ma'], check_exist=True
            )
            mocap_ma_files.extend(_ma_files)

        shot_task = CGTW_API_INSTANCE.common_get_one_item(
            proj_db, module, module_type,
            filter_data={
                'eps.entity': task.eps_entity, 'seq.entity': task.seq_entity, 'shot.entity': task.shot_entity, 'pipeline.entity': 'BodyAnimation'
                        },
            fields=['task.id']
        )
        work_dir = CGTW_API_INSTANCE.get_filebox_info(proj_db, module, module_type, shot_task.task_id, 'work')['path']
        print (work_dir)
        print (os.path.isdir(work_dir))
        if not os.path.isdir(work_dir):
            os.makedirs(work_dir)

        output_filename = '{}_{}_{}_ani_body.ma'.format(task.eps_entity, task.seq_entity, task.shot_entity)
        output_filename_path = os.path.join(work_dir, output_filename)

        print(layout_ma_file)
        print(mocap_ma_files)

        merge_layout_and_animation_handler(
            layout_ma_file,
            mocap_ma_files,
            output_filename_path
        )

        CGTW_API_INSTANCE.upload_files_to_filebox(proj_db, module, module_type, shot_task.task_id, 'work', ['*.ma'])
        CGTW_API_INSTANCE.change_task_autotask_status(proj_db, [task_id], 'ImportAnimationDone', module=module)
    except Exception as e:
        LOGGER.error("merge_layout_and_animation_task error, proj %s task_id %s", proj_db, task_id, exc_info=True)
        CGTW_API_INSTANCE.change_task_autotask_status(proj_db, [task_id], 'ImportAnimationError', module, str(e))


if __name__ == '__main__':
    merge_layout_and_animation('proj_shsd', 'F109375F-301A-E767-6F0F-60349F47E63A', 'task', 'shot')

    #merge_layout_and_animation_task('proj_shsd', 'A6213D3F-0BBA-677F-D15F-40AD98982212')