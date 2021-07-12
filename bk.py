# class Book():
#     pk = 'hh'
#     def __init__(self, age):
#         self.age = age
#
#     def func(self):
#         print('this is in func')
#     @classmethod
#     def run(cls):
#         cls.func()
#         print('this is in the run')
# print(Book.run())

def person_info(name, age, **kw):
    print("name", name, "age", age, "other", kw)

ani_task_data = {'run': 'mocap_transfer', 'mappings': {}, 'task_id': 'C694E040-B63A-BA77-3C5C-911480C19AB7',
                 'time_margin': 0, 'maya_version': 20180600, 'project_db_name': 'proj_kiehls_mr_bones',
                 'frame_rate': '60fps', 'extra_params': {'retarget_type': 'fix'}, 'data': [
        {'rig': u'T:/projects/Kiehls_Mr_Bones/asset/char/MR_Bones_body/rig/MR_Bones_body_rig.ma',
         'fbx': u'T:/projects/Kiehls_Mr_Bones/mocap/1/1/1/SYNC/FBX\\1-1-1-115_510-res_shot_1-xiaowen-mr_bones_body.fbx',
         'end': 196, 'namespace': u'MR_Bones_body', 'start': 0}]}
person_info("Dahuang", 35, **ani_task_data)