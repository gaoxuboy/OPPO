class Foo(object):
    def __init__(self,name):
        self.name = name

    def func1(self):
        print(self.name)

obj1 = Foo("111")
obj1.func1()

obj2 = Foo("222")
obj2.func1()

