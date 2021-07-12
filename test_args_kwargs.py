#示例一
def fun(**kwargs):
    print(**kwargs)

    a = kwargs

    print(a,type(a))
fun(k1 = 1,k2 = 2) #注意：k1，k1在此处没有" "


#示例二
#另外的一种表示方法
def fun(**kwargs):
    print(**kwargs)
    a = kwargs

    print(a,type(a))
fun(**{'k1' : 1,"k2" : 2}) #直接以字典的形式输入

def fun(*args):
    print(*args)
    a = args

    print(a,type(a))
fun(*(1,2,3)) #可在元组钱加*，意为打散其中的元素，此情况适用于列表和元组