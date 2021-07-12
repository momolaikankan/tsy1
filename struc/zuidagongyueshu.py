def max_num(a,b):
    smaller = a if a < b else b
    for i in range(1, smaller+1):
        if a%i ==0 and b %i ==0:
            num = i
    return num
res = max_num(4, 8)
print(res)