'''给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 '''


def get_mid(nums1, nums2):
    lis = []
    while nums1 and nums2:
        if nums1[0] <= nums2[0]:
            lis.append(nums1.pop(0))
        else:
            lis.append(nums2.pop(0))
    while nums1:
        lis.extend(nums1)
        break
    while nums2:
        lis.extend(nums2)
        break
    print(lis)
    if len(lis) % 2 == 0:
        mid_index1 = len(lis)//2
        mid_index2 = mid_index1 - 1
        return (lis[mid_index1]+lis[mid_index2])/2
    else:
        mid_index = len(lis)//2
        return lis[mid_index]

lis1 = [1,1]
lis2 = [1,2]
res = get_mid(lis1, lis2)
print(res)
