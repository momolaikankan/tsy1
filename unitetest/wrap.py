from functools import wraps


def outer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('in the before')
        ret = func(*args, **kwargs)
        print("in the after")
        return ret
    return inner


@outer
def func(kk):
    print("this is func", kk)
    return 'this is return'


print(func.__name__)
res = func("kkkkkkk")
print(res)


#完全不搞不懂
def outer(flag):
    def timer(func):
        def inner(*args,**kwargs):
            if flag:
                print('''执行函数之前要做的''')
            re = func(*args,**kwargs)
            if flag:
                print('''执行函数之后要做的''')
            return re
        return inner
    return timer


@outer(False)
def func():
    print(111)

func()


def decorator(arg_of_decorator):
    def deco(func):
        def wrapper(*arg, **kw):
            print('decorator arg: %s' % arg_of_decorator)
            print('call %s in decorator' % func.__name__)
            return func(*arg, **kw)

        return wrapper

    return deco


@decorator("修饰器参数")
def test1():
    pass
test1()
# 等价于 test1 = decorator("修饰器参数")(test1) = deco(test1)
# 修饰器的参数已经传递进去



