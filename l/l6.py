def restr(str, numrow):
    lis = []
    for i in range(numrow):
        lis.append([])
    print(lis)
    count = 0
    ind = 1
    for i in str:
        lis[count].append(i)
        count += ind
        if count == numrow-1:
            ind = -1
        if count == 0:
            ind = 1
    final_lis = []
    for j in lis:
        for k in j:
            final_lis.append(k)
    return ''.join(final_lis)


lis1 = restr("PAYPALISHIRING", 4)
print(lis1)
#"PINALSIGYAHRPI"
#"PINALSIGYAHRPI"