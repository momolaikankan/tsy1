def func(s,c):
    lis = []
    for i in range(len(s)):
        if s[i] == 'e':
            lis.append(i)
    lis1 = []
    for i in range(len(s)):
        kk = min([abs(i-j) for j in lis])
        lis1.append(kk)
    return lis1


def func1(s,c):
    lis = []
    for i in range(len(s)):
        flag = True

        if s[i] == 'e':
            lis.append(i)
        else:
            left = right = i
            while flag and left > 0 and right < len(s):

                if s[left] == 'e' or s[right] == 'e':
                    lis.append(abs(left - i))
                    flag = False

                left -= 1
                right +=1
            while flag and left > 0:
                if s[left] == 'e':
                    lis.append(abs(left - i))
                    flag = False

                left -= 1
            while flag and right < len(s):
                if s[right] == 'e':
                    lis.append(abs(right - i))
                    flag = False

                right += 1


    return lis
s = 'loveleetcode'
c = 'e'




res = func(s,c)
print(res)
res2 = func1(s,c)
print(res2)
