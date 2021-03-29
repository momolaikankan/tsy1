import requests
import json
def get_check_call():
    url = "http://120.27.236.26:8880/api.php"
    d = {
        "token":"841D6A1F-3059-353D-B210-F7B40B74CE0D",
        "controller":"c_note",
        "method":"get_with_link_id",
        "db":"proj_test_xmov",
        "link_id":"1C29A9DB-ED67-6A53-B0D6-F213E6A3F368",
        "field_array":['dom_text', 'time'],
        # "module":"asset",
        # "module_type":"task",
         }
    res = requests.post(url, {
                'data': json.dumps(d)
            }, verify=False)
    print(res)
    print(res.json())
dic2 = {'code': '1', 'type': 'json', 'data': [['[{"type": "text", "style": "", "content": "all the people can see\\n"}]', '2021-03-23 13:52:33'],
                                              ['[{"type": "text", "content": "test create"}]', '2021-03-23 14:02:46'],
                                              ['[{"type": "text", "style": "", "content": "hello world"}]', '2021-03-23 15:15:12'],
                                              ['[{"type": "text", "style": "", "content": "kkkkkkk"}]', '2021-03-23 15:40:45']]}



dic1 = {'code': '1', 'type': 'json', 'data': [['[{"type": "text", "style": "", "content": "all the people can see\\n"}]', '2021-03-23 13:52:33'],
                                       ['[{"type": "text", "content": "test create"}]', '2021-03-23 14:02:46'],
                                       ['[{"type": "text", "style": "", "content": "hello world"}]', '2021-03-23 15:15:12'],
                                       ['[{"type": "text", "style": "", "content": "kkkkkkk"}]', '2021-03-23 15:40:45']]}


def create_check_call2():
    #{'code': '0', 'type': 'msg', 'data': 'v_note::create, There must be key(db, module, module_type, id, dom_text, permission, tags)'}
    url = "http://120.27.236.26:8880/api.php"
    d = {
        "token":"841D6A1F-3059-353D-B210-F7B40B74CE0D",
        "controller":"v_note",
        "method":"create",

        "db": "proj_test_xmov",
        "module":"asset",
        "module_type":"info",
        "id": "4883D7AE-02B2-EA6D-9DF8-4CA908E7E35E",
        "dom_text":[{"type": "text", "content": "9512364", "style": "font-size:14px;font-weight:;"}],
        "permission": "all",
        "tags":""
         }

    res = requests.post(url, {
                'data': json.dumps(d)
            }, verify=False)
    print(res)
    print(res.json())

# class CGNoteView(CustomizedAPIView):
#     @expose(["POST"])
#     @common_wrapper
#     def create(self, request):
#         project = request.data["project"]
#         db = convert_project_database(request.api_handler, project)
#         module = request.data["module"]
#         module_type = request.data.get("module_type", "task")
#         task_id = request.data["task_id"]
#         content_type = request.data.get('type', 'text')
#         content = request.data.get("content")
#         font_size = request.data.get("font_size", 14)
#         font_weight = request.data.get("font_weight", '')
#         style = "font-size:14px;font-weight: ;".format(font_size, font_weight)
#         dom_text = [{"type": content_type, "content": content, "style": "font-size:14px;font-weight:;"}]
#
#         data = {
#             "db": db,
#             "module": module,
#             "module_type": module_type,
#             "id": task_id,
#             "dom_text": dom_text,
#             "permission": "all",
#             "tags": ""
#         }
#         result = request.api_handler.common_call(data, controller="v_note", method="create")
#         return Response(data=result)
# class CGNoteView(CustomizedAPIView):
#     @expose(["POST"])
#     @common_wrapper
#     def create(self, request):
#         project = request.data["project"]
#         db = convert_project_database(request.api_handler, project)
#         module = request.data["module"]
#         module_type = request.data.get("module_type", "task")
#         task_id = request.data["task_id"]
#         dom_text = [{"type":"text", "content":"517852", "style":"font-weight:bold;"}]
#         data = {
#             "db": db,
#             "module": module,
#             "module_type": module_type,
#             "id": task_id,
#             "dom_text": dom_text,
#             "permission": "all",
#             "tags": ""
#         }
#         result = request.api_handler.common_call(data, controller="v_note", method="create")
#         return Response(data=result)

def save_check_call3():
    #{'code': '0', 'type': 'msg', 'data': 'v_note::create, There must be key(db, module, module_type, id, dom_text, permission, tags)'}
    url = "http://120.27.236.26:8880/api.php"
    d = {
        "token":"841D6A1F-3059-353D-B210-F7B40B74CE0D",
        "controller":"v_note",
        "method":"save",

        "db": "proj_test_xmov",
        "module":"asset",
        "module_type":"task",
        "link_id": "4883D7AE-02B2-EA6D-9DF8-4CA908E7E35E",  ###task_id
        "id": "9ECC5121-A87E-325E-7CFF-FE94639234F7",   ####note_id
        "dom_text":[{"type": "text", "content": "9512364", "style": "font-size:14px;font-weight:;"}],
        "permission": "all",
        "tags":""
         }

    res = requests.post(url, {
                'data': json.dumps(d)
            }, verify=False)
    print(res)
    print(res.json())


def time_check_call3():
    #{'code': '0', 'type': 'msg', 'data': 'v_note::create, There must be key(db, module, module_type, id, dom_text, permission, tags)'}
    url = "http://120.27.236.26:8880/api.php"
    d = {
        "token":"841D6A1F-3059-353D-B210-F7B40B74CE0D",
        "controller":"v_sys_plugin",
        "method":"update_flow",

        "db": "proj_test_xmov",
        "module":"asset",
        "module_type":"task",
        "dom_text": [{"type": "text", "content": "8888", "style": "font-size:14px;font-weight:;"}],
        "status": "",
        "status_type":"zk",
        "is_task_status": "Y",
        "id_array": ["C999D419-9603-B6D9-A5DC-9DA88DFAEB5F"],   ####task_id

        "permission": "all",
        "tags": ""
         }

    res = requests.post(url, {
                'data': json.dumps(d)
            }, verify=False)
    print(res)
    print(res.json())




if __name__ == '__main__':

    time_check_call3()
