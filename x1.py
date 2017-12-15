

# obj = Foo()
# print(obj.func) # <bound method Foo.func of <__main__.Foo object at 0x00000000021E8400>>

# print(Foo.func)  # <function Foo.func at 0x0000000001E89B70>
#
# obj = Foo()
# Foo.func(obj)
#
# obj = Foo()
# obj.func()
class Foo(object):
    def __init__(self):
        self.name = 'alex'
    def func(self):
        print(self.name)

from types import FunctionType,MethodType

obj = Foo()
print(isinstance(obj.func,FunctionType)) # False
print(isinstance(obj.func,MethodType))   # True

print(isinstance(Foo.func,FunctionType)) # True
print(isinstance(Foo.func,MethodType))   # False
"""
注意：
    方法，无需传入self参数
    函数，必须手动传入self参数
"""













