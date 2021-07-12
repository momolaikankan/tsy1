import os

lis = [1, 2, 3]
# for i in lis:
#     for j in lis:
#         for k in lis:
#             if i != j and j != k and i != k:
#                 print([i, j, k])


def perm(arr):
    """实现全排列"""
    length = len(arr)
    if length == 1:  # 递归出口
        return [arr]

    result = []  # 存储结果
    fixed = arr[0]
    rest = arr[1:]

    for _arr in perm(rest):  # 遍历上层的每一个结果
        for i in range(0, length):  # 插入每一个位置得到新序列
            new_rest = _arr.copy()  # 需要复制一份
            new_rest.insert(i, fixed)
            result.append(new_rest)
    return result


res = perm(lis)
print(res)


def permutations(arr, position, end):
    if position == end:
        print(arr)

    else:
        for index in range(position, end):
            if arr[index] != arr[position]:
                arr[index], arr[position] = arr[position], arr[index]
                permutations(arr, position + 1, end)
                arr[index], arr[position] = arr[position], arr[index]


arr = ["a", "b", "c"]
permutations(arr, 0, len(arr))





import copy

def myallsort(lis):
    res = lis.pop(0)
    if len(lis) == 0:
        return [[res]]
    lis1 = myallsort(lis)
    kk = []
    for one_lis in lis1:
        for i in range(len(one_lis)+1):
            origin_lis = one_lis[:]
            origin_lis.insert(i,res)
            kk.append(origin_lis)
    return kk



res = myallsort([1,2,3])
print(res)




















