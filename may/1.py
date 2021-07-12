#big num add

str1 = '12345678'
str2 = '3456785555'
str1 = str1[::-1]
str2 = str2[::-1]
lis = []
add0_num = abs(len(str1)-len(str2))
if len(str1) > len(str2):
    str2 = str2 + '0' * add0_num
else:
    str1 = str1+'0' * add0_num
jingwei = 0
for i in range(len(str1)):
    num = int(str1[i]) + int(str2[i]) + jingwei
    jingwei = 0
    if num >= 10 :
        jingwei = num // 10
        yu = num % 10
        lis.append(yu)
    else:
        lis.append(num)
if jingwei == 0:
    pass
else:
    lis.append(jingwei)

print(lis)

res = lis[::-1]
print(res)

