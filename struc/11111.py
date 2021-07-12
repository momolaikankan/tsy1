def change_num(str1,path,lis,index):
    if index == len(str1)-2:
        path1 = path + 'aa'
        lis.append(path1)
        path2 = path+'k'
        lis.append(path2)
        return
    if index == len(str1)-1:
        path1 = path + 'a'
        lis.append(path1)
        return

    one = path+'a'
    change_num(str1, one, lis, index+1)

    two = path+'k'
    change_num(str1, two, lis, index+2)
    return lis


str1 = '1111'

res = change_num(str1, '', [], 0)
print(res)

