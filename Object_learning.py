#coding:utf-8

"This module is used for record learning tips"

__author__ = "kzk"


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


"""
OOP: 继承性，封装性，多态性

class :  类
Instance : 实例 


__name__ 表示的是 特殊的变量，双下滑开头且结尾的。

python内没有 private 关键字，需要靠的是自觉遵守。
__name 表示的是 私有变量

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，
这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，
意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。



数据封装：

类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。
这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法

通过函数来修改 private 变量 
"""


"""
Case:

>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'

表面上看，外部代码“成功”地设置了__name变量，
但实际上这个__name变量和class内部的__name变量不是一个变量！
内部的__name变量已经被Python解释器自动改成了_Student__name，
而外部代码给bart新增了一个__name变量。不信试试：

>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
"""


class Animal(object):
    def run(self):
        print('Animal is running...')



class Dog(Animal):
	"""docstring for Dog"""
	def run(self):
		print('Dog is running...')
		



"""
继承性:


继承最大的好处：子类获得了父类的全部功能

判断一个变量是否是某个类型可以用isinstance()判断：

>>> isinstance(a, list)
True


在继承关系中，如果一个实例的数据类型是某个子类，
那它的数据类型也可以被看做是父类
Dog可以看成Animal，但Animal不可以看成Dog


class Timer(object):
    def run(self):
        print('Start...')

静态语言 vs 动态语言
对于静态语言（例如Java）来说，
如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，
否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。
我们只需要保证传入的对象有一个run()方法就可以了：

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
"""


"""

可以在外部绑定属性和方法。


定义类时可以添加 __slots__  用于限制实例添加的属性
__slots__ = （name, age）#表示在实例中不能额外添加其他属性
"""