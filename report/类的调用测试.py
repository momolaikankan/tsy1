# coding=utf-8


import os

class Methods:
    """实例方法、静态方法、类方法"""
    def imeth(self, x):
        print (self, x)

    @staticmethod
    def smeth(x):  # 静态方法不需要self参数
        print (x)

    @classmethod
    def cmeth(cls, x):  # 类方法需要一个类参数
        print (cls, x)

    def kk(self):
        self.imeth('clscls')






me = Methods()
print dir(me)
mell = Methods()
me.imeth('ll')
Methods.imeth(Methods(), 'kk')
Methods.kk(me)
print("******")
#也就是说用类直接调用实例方法需要传参数
##############################
me.smeth('1')
Methods.smeth('2')
#############################
me.cmeth('ii')
Methods.cmeth('oo')


