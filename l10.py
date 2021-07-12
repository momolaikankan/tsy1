# kk = 'T:/projects/test_xmov/mocap/EP001/SQ001/SH009_SH010/SYNC/FBX\\ep001-sq001-sh009_sh010-res_shot_sh009_sh010-siran-c052_xiaobu4.atom'
# ll = 'T:/projects/test_xmov/mocap/EP001/SQ001/SH009_SH010/SYNC/FBX\\ep001-sq001-sh009_sh010-res_shot_sh009_sh010-xiaowen-c052_xiaobu4.atom'
# lis = [ll, kk]
# lis.sort()
# print(lis)
dic = {u'SH009_SH010': {u'T:/projects/test_xmov/mocap/EP001/SQ001/SH009_SH010/SYNC/FBX\\ep001-sq001-sh009_sh010-res_shot_sh009_sh010-xiaowen-c052_xiaobu4.fbx': (u'xiaowen', u'C052_Xiaobu4'),
                        u'T:/projects/test_xmov/mocap/EP001/SQ001/SH009_SH010/SYNC/FBX\\ep001-sq001-sh009_sh010-res_shot_sh009_sh010-siran-c052_xiaobu4.fbx': (u'siran', u'C052_Xiaobu4')},
        u'SH009_SH011': {u'T:/projects/test_xmov/mocap/EP001/SQ001/SH009_SH010/SYNC/FBX\\ep001-sq001-sh009_sh010-res_shot_sh009_sh010-xiaowen-c052_xiaobu4.fbx': (u'xiaowen', u'C052_Xiaobu4'),
                        u'T:/projects/test_xmov/mocap/EP001/SQ001/SH009_SH010/SYNC/FBX\\ep001-sq001-sh009_sh010-res_shot_sh009_sh010-siran-c052_xiaobu4.fbx': (u'siran', u'C052_Xiaobu4')},

       }

dic1 = {u'T:/projects/test_xmov/mocap/EP001/SQ001/SH009_SH010/SYNC/FBX\\ep001-sq001-sh009_sh010-res_shot_sh009_sh010-siran-c052_xiaobu4.fbx': (u'siran', u'C052_Xiaobu4'),
        u'T:/projects/test_xmov/mocap/EP001/SQ001/SH009_SH010/SYNC/FBX\\ep001-sq001-sh009_sh010-res_shot_sh009_sh010-xiaowen-c052_xiaobu4.fbx': (u'xiaowen', u'C052_Xiaobu4'),}
# dic2 = dic[max(dic,key=lambda k:dic[k])]
dic2 = sorted(dic1.items(), key=lambda k: k[0])
print(dict(dic2))
dic3 = {key: dict(sorted(value.items(), key=lambda k: k[0])) for key, value in dic.items()}
print(dic3)

from collections import Counter
lis = ['xiao', 'xiao', 'kk', 'cc']
res = Counter(lis)
print(res['xiao'])
# for i, j in res.items():
#     print(i, j)


