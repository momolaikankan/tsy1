# 输入: S = "loveleetcode", C = 'e'
#
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
s = "loveleetcode"
c = 'e'
lis = []
for i in range(len(s)):
    l = r = i
    flag = 'true'
    while l >=0 and r <len(s) and flag == 'true':
        if s[l] == c or s[r] == c:
            lis.append(abs(r-i))
            flag = 'false'
            break
        l -= 1
        r += 1
    if l >= 0 and r >= len(s) and flag == 'true':
        while l >= 0:
            if s[l] == c:
                lis.append(abs(l-i))
                flag = 'false'
                break
            l -= 1
    elif l < 0 and r < len(s) and flag == 'true':
        while r < len(s):
            if s[r] == c:
                lis.append(abs(r-i))
                flag = 'flase'
                break
            r += 1
print(lis)

