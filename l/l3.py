s = "tmmzuxtk"
# start = -1
# max1 = 0
# d = {}
# for i in range(len(s)):
#     if s[i] in d and d[s[i]] > start:
#         start = d[s[i]]
#         d[s[i]] = i
#     else:
#         d[s[i]] = i
#         if i - start > max1:
#             max1 = i-start
#
# print(max1)
d = {}
start = -1
max1 = 0
for i in range(len(s)):
    if s[i] in d:
        start = d[s[i]]
        d[s[i]] = i
    else:
        d[s[i]] = i
        if i - start > max1:
            max1 = i - start
print(max1)