class Person(object):
    def __init__(self, **args):
        self.name = args['name']
        self.age = args['age']
        print('in preson')
        print(args)

    def talk(self):
        print("person is talking....")


class Mywork():
    def __init__(self, **args):
        print('in Mywork')
    def talk(self):
        print('in mywork')

class Chinese(Mywork, Person):

    # def __init__(self, name, age, language):  # 先继承，在重构
    #     Person.__init__(self, name, age)  # 继承父类的构造方法，也可以写成：super(Chinese,self).__init__(name,age)
    #     self.language = language  # 定义类的本身属性
    def __init__(self, **args):
        super().__init__( **args)


    def walk(self):
        print('is walking...')



info = {'name':'xioaming', 'age':22}
c = Chinese(**info)
c.walk()
def func(*args):
    print(*args)
    print(args)
fi = (1,2,3,4)
func(fi)