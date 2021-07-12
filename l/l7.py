# def rev(num):
#     num = str(num)
#     num1 = num[::-1]
#     num1 = num1.strip('0')
#     if num1.endswith('-'):
#         num1 = num1.strip('-')
#         num1 = '-'+num1
#     num2 = int(num1)
#     return num2
# res = rev(120)
# print(res)

def rev1(a):
    count = 0
    num = abs(a)
    while num != 0:
        temp = num % 10
        count = count *10 + temp
        num = num // 10
    if a >= 0:
        final_num = count
    else:
        final_num = -count
    if -2**31 <= final_num <= 2**31:
        return final_num
    else:
        return 0
res = rev1(123)
print(res)