lis = {'abb', 'ab', 'ab', 'a', 'bb', 'b', 'b'}
lis.add('b')
print(lis)
print(set())

def zisort2(str1, index, ans, path):
    if index == len(str1):
        ans.add(path)
        return
    yes = path + str1[index]
    zisort2(str1, index + 1, ans, yes)
    no = path
    zisort2(str1, index + 1, ans, no)
    return ans
res1 = zisort2('abb', 0, set(), '')
print(res1)




visit = [True, True, True]
temp = ["" for x in range(0, 3)]

#position表示需要对temp哪个位置进行填充

def dfs(arr, position):
    if position == len(arr):
        print(temp)
        return
    for index in range(0,len(arr)):
        if visit[index] ==  True:
            temp[position] = arr[index]
            visit[index] = False
            dfs(arr, position+1)
            visit[index] = True
arr1 = [1,2,2]

dfs(arr1, 0)
lis = []
with open('123','r') as f:
    for i in f:
        shot = i.strip()
        new_shot = shot.split('_')
        shot_name1 = '_'.join(new_shot[:-1])
        shot_name = shot_name1+'-'+new_shot[-1]
        lis.append(['train', 'KYDS', shot_name])
print(lis)
print(len(lis))


print('_'.join(['rk', 'tag']))
def func():
    import os
    import shutil
    out_dir = r"C:\Users\admin\Desktop\ggl_fbx\train_GGL_STA-shot9-_3___8.fbx"
    file_list = [files for root, dirs, files in os.walk(out_dir)][0]
    print(file_list)

    need_fbx_file = [file for file in file_list if file.endswith('___GGL.fbx')][0]
    print(need_fbx_file)
    file_dir = [root for root, dirs, files in os.walk(out_dir)][0]
    print(os.path.join(file_dir,need_fbx_file))
    fbx_all_path = r'C:\Users\admin\Desktop\fbx_all'
    dest_path = os.path.join(fbx_all_path, need_fbx_file)
    shutil.copy(os.path.join(file_dir,need_fbx_file),dest_path)

