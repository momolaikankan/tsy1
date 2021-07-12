# import itertools
# lis = [nt.Transform(u'Sclera'), nt.Transform(u'Sclera_L'), nt.Mesh(u'Sclera_LShape'), nt.Mesh(u'Sclera_LShapeOrig'), nt.Transform(u'Sclera_R'), nt.Mesh(u'Sclera_RShape'), nt.Mesh(u'Sclera_RShapeOrig'), nt.Mesh(u'ScleraShape'), nt.Mesh(u'ScleraShapeOrig'), nt.Transform(u'Teeth_Bed_Dn'), nt.Mesh(u'Teeth_Bed_DnShape'), nt.Mesh(u'Teeth_Bed_DnShapeOrig'), nt.Transform(u'Teeth_Bed_Up'), nt.Mesh(u'Teeth_Bed_UpShape'), nt.Mesh(u'Teeth_Bed_UpShapeOrig'), nt.Transform(u'Teeth_Dn'), nt.Mesh(u'Teeth_DnShape'), nt.Mesh(u'Teeth_DnShapeOrig'), nt.Transform(u'Teeth_Up'), nt.Mesh(u'Teeth_UpShape'), nt.Mesh(u'Teeth_UpShapeOrig'), nt.Transform(u'Tongue'), nt.Mesh(u'TongueShape'), nt.Mesh(u'TongueShapeOrig'), nt.Transform(u'meimao'), nt.Mesh(u'meimaoShape'), nt.Mesh(u'meimaoShapeOrig'), nt.PointConstraint(u'RootX_M_pointConstraint1'), nt.OrientConstraint(u'FKCup_L_orientConstraint1'), nt.OrientConstraint(u'FKWrist_L_orientConstraint1'), nt.OrientConstraint(u'FKThumbFinger2_L_orientConstraint1'), nt.OrientConstraint(u'FKPinkyFinger3_L_orientConstraint1'), nt.OrientConstraint(u'FKMiddleFinger2_L_orientConstraint1'), nt.OrientConstraint(u'FKWrist_R_orientConstraint1'), nt.OrientConstraint(u'FKPinkyFinger3_R_orientConstraint1'), nt.OrientConstraint(u'FKHip_L_orientConstraint1'), nt.OrientConstraint(u'FKShoulder_R_orientConstraint1'), nt.OrientConstraint(u'FKKnee_L_orientConstraint1'), nt.OrientConstraint(u'FKNeck1_M_orientConstraint1'), nt.OrientConstraint(u'FKThumbFinger3_L_orientConstraint1'), nt.OrientConstraint(u'FKMiddleFinger3_L_orientConstraint1'), nt.OrientConstraint(u'FKHip_R_orientConstraint1'), nt.OrientConstraint(u'FKAnkle_L_orientConstraint1'), nt.OrientConstraint(u'FKIndexFinger1_L_orientConstraint1'), nt.OrientConstraint(u'FKRingFinger2_L_orientConstraint1'), nt.OrientConstraint(u'FKMiddleFinger3_R_orientConstraint1'), nt.OrientConstraint(u'FKScapula_R_orientConstraint1'), nt.OrientConstraint(u'FKNeck_M_orientConstraint1'), nt.OrientConstraint(u'FKElbow_R_orientConstraint1'), nt.OrientConstraint(u'FKPinkyFinger2_L_orientConstraint1'), nt.OrientConstraint(u'FKShoulder_L_orientConstraint1'), nt.OrientConstraint(u'FKThumbFinger1_L_orientConstraint1'), nt.OrientConstraint(u'FKCup_R_orientConstraint1'), nt.OrientConstraint(u'FKThumbFinger2_R_orientConstraint1'), nt.OrientConstraint(u'FKSpine2_M_orientConstraint1'), nt.OrientConstraint(u'FKMiddleFinger1_R_orientConstraint1'), nt.OrientConstraint(u'FKAnkle_R_orientConstraint1'), nt.OrientConstraint(u'FKChest_M_orientConstraint1'), nt.OrientConstraint(u'FKHead_M_orientConstraint1'), nt.OrientConstraint(u'FKIndexFinger3_R_orientConstraint1'), nt.OrientConstraint(u'FKThumbFinger1_R_orientConstraint1'), nt.OrientConstraint(u'FKIndexFinger3_L_orientConstraint1'), nt.OrientConstraint(u'FKKnee_R_orientConstraint1'), nt.OrientConstraint(u'FKIndexFinger2_R_orientConstraint1'), nt.OrientConstraint(u'FKRingFinger1_L_orientConstraint1'), nt.OrientConstraint(u'FKPinkyFinger1_R_orientConstraint1'), nt.OrientConstraint(u'FKRingFinger1_R_orientConstraint1'), nt.OrientConstraint(u'FKSpine1_M_orientConstraint1'), nt.OrientConstraint(u'FKPinkyFinger2_R_orientConstraint1'), nt.OrientConstraint(u'FKElbow_L_orientConstraint1'), nt.OrientConstraint(u'FKSpine3_M_orientConstraint1'), nt.OrientConstraint(u'FKMiddleFinger2_R_orientConstraint1'), nt.OrientConstraint(u'FKMiddleFinger1_L_orientConstraint1'), nt.OrientConstraint(u'FKRingFinger3_L_orientConstraint1'), nt.OrientConstraint(u'FKRoot_M_orientConstraint1'), nt.OrientConstraint(u'FKRingFinger3_R_orientConstraint1'), nt.OrientConstraint(u'FKToes_R_orientConstraint1'), nt.OrientConstraint(u'FKScapula_L_orientConstraint1'), nt.OrientConstraint(u'FKIndexFinger1_R_orientConstraint1'), nt.OrientConstraint(u'FKPinkyFinger1_L_orientConstraint1'), nt.OrientConstraint(u'FKIndexFinger2_L_orientConstraint1'), nt.OrientConstraint(u'FKThumbFinger3_R_orientConstraint1'), nt.OrientConstraint(u'FKToes_L_orientConstraint1'), nt.OrientConstraint(u'FKRingFinger2_R_orientConstraint1'), nt.ParentConstraint(u'FKRoot_M_parentConstraint1'), nt.ParentConstraint(u'FKChest_M_parentConstraint1'), nt.ParentConstraint(u'IKSpine11_M_parentConstraint1'), nt.ParentConstraint(u'IKSpine12_M_parentConstraint1'), nt.ParentConstraint(u'IKSpine13_M_parentConstraint1'), nt.ParentConstraint(u'IKSpine21_M_parentConstraint1'), nt.ParentConstraint(u'IKSpine22_M_parentConstraint1'), nt.ParentConstraint(u'IKSpine23_M_parentConstraint1'), nt.ParentConstraint(u'FKSpine1_M_parentConstraint1'), nt.ParentConstraint(u'FKSpine2_M_parentConstraint1'), nt.ParentConstraint(u'FKSpine3_M_parentConstraint1'), nt.ParentConstraint(u'PoleLeg_L_parentConstraint1'), nt.ParentConstraint(u'IKArm_R_parentConstraint1'), nt.ParentConstraint(u'IKToes_L_parentConstraint1'), nt.ParentConstraint(u'PoleLeg_R_parentConstraint1'), nt.ParentConstraint(u'IKArm_L_parentConstraint1'), nt.ParentConstraint(u'IKToes_R_parentConstraint1'), nt.ParentConstraint(u'IKLeg_L_parentConstraint1'), nt.ParentConstraint(u'IKLeg_R_parentConstraint1'), nt.Transform(u'polySurface1'), [nt.Cluster(u'cluster1'), nt.Transform(u'cluster1Handle')], [nt.Cluster(u'cluster2'), nt.Transform(u'cluster2Handle')], [nt.Cluster(u'cluster3'), nt.Transform(u'cluster3Handle')], nt.PointConstraint(u'cluster1Handle_pointConstraint1'), nt.PointConstraint(u'cluster2Handle_pointConstraint1'), nt.PointConstraint(u'cluster3Handle_pointConstraint1'), nt.Transform(u'locator1'), nt.PointOnPolyConstraint(u'locator1_pointOnPolyConstraint1'), nt.ParentConstraint(u'PoleArm_L_parentConstraint1'), nt.Transform(u'polySurface2'), [nt.Cluster(u'cluster4'), nt.Transform(u'cluster4Handle')], [nt.Cluster(u'cluster5'), nt.Transform(u'cluster5Handle')], [nt.Cluster(u'cluster6'), nt.Transform(u'cluster6Handle')], nt.PointConstraint(u'cluster4Handle_pointConstraint1'), nt.PointConstraint(u'cluster5Handle_pointConstraint1'), nt.PointConstraint(u'cluster6Handle_pointConstraint1'), nt.Transform(u'locator2'), nt.PointOnPolyConstraint(u'locator2_pointOnPolyConstraint1'), nt.ParentConstraint(u'PoleArm_R_parentConstraint1'), nt.Transform(u'mocap')]
# res = itertools.chain.from_iterable(lis)
# for i in res:
#     print(i)
# print(isinstance(['c', 'd', 'e'], list))
# lis1 = []
# def flatten(lis, kk = []):
#     for i in lis:
#         if isinstance(i, list):
#             flatten(i, kk)
#         else:
#             kk.append(i)
#     return kk
#
# kk1 = ["a", "abc", ['c', 'd', 'e', ['ijk', 'plokm']], ['abdcd','skdfj']]
#
# res = flatten(kk1)
# print(res)
# import os
# import glob
# path = r"T:\projects\DigitalMan_ZJ_GGL\shot\train\GGL\STA-shot8-_1___9\faceTrain\face_video"
# cap = glob.glob(os.path.join(path, '*feature', '*detail', 'images', '*.0.jpg'))
# print(cap)


kk = {1:'ming', 2:'xiao'}
print('ming' in kk.values())
# print([kk.values()])
# for i, j in kk.values():
#     try:
#         print(i, j, k)
#     except Exception as e:
#         print('****')
#         print(e)
#         raise

