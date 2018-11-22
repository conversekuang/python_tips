#coding:utf-8
"File to learn magic function"

__author__ = "kzk"



import sys



class Base(object):
	def __init__(self, id_name):
		self.id = id_name

	def __str__(self):
		"""这个函数用于print的输出格式,为了打印更好看"""
		return "base id is %d "% self.id

	__repr__ = __str__   
	"""
	__str__() 返回的是用户看的，一般print出来
	__repr__() 返回的是开发者调试看到的。
	这两个函数内容是相同的，因此可以通过函数赋值得到
	变量调用的
	"""



	def __iter__(self):
		"""
		__iter__(): 一个类想被用于 for ... in 循环，eg.:list, tuple，要实现__iter__()。
		该方法返回一个迭代对象，然后for循环可以不断调用该对象的next方法。
		在python2.7  中是用next()实现。
		在python3    中是用__next__()实现的。
		
		"""







if __name__ == '__main__':
	b = Base(1)
