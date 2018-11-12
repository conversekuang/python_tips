#coding:utf-8

def decorator(fuc):
	print("enter__wapper__")
	def wapper1(para):
		print("in__wapper__")
		fuc(para)
		print("exit__wapper__")
	return wapper1


def Outer(fuc):
	print("enter__Outer__")
	def wapper2(para):
		print("in__Outer__")
		print("**%s**"%fuc.__name__)
		fuc(para)
		print("exit__Outer__")
	return wapper2


@Outer
@decorator
def func(para):
	print("__core__function %s" % para)


def sanem():
	print ("name function")

def dec(func):
	print("%s" % func.__name__)
	return func




if __name__ == '__main__':
	func("kzk")



"""
	@  是  语法糖
	x1 = decorator(f)    #先调用下面的，最后调用上面的
	x2 = outer(x1)		 #之后所有返回函数均为嵌套，从上往下执行。
	f = x2
	也就是：

	f = outer(decorator(f))  #从内往外函数的装饰执行顺序，最后新的f是叠加各种装饰器之后的f。是一个
	函数，并没有进行实际的调用执行。
	f()    #函数调用，从外往内；

	#  装饰器：一般表现形式，外层传递函数，里面传递参数。装饰器返回的是函数
	#无参数装饰器

	def decorator(func):      
		def _wapper(*args, **kwargs):
			...
			return func(*args, **kwargs)
		return _wapper

	#含参数装饰器
	
	def decorator(*dargs, **kwagrs):
		def wapper(func):     
			def _wapper(*args, **kwargs):
				...
				dargs,kwargs
				...
				return func(*args, **kwargs)
			return _wapper
		return wapper

	from functools import wraps

	作用：
		Python装饰器（decorator）在实现的时候，
		被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），
		为了不影响，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。
		写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring。


		def wapper(func):
		    @wraps(func)   #保持原函数的名称和文档信息
			def _wapper(*args, **kwargs):
				...
				dargs,kwargs
				...
				print func.__name__, func.__doc__  #保持原来函数的信息，而不是嵌套函数的信息
				return func(*args, **kwargs)
			return _wapper



	多个装饰器的调用顺序是自下往上，但是运行时的执行顺序是自上往下！！！
	https://blog.csdn.net/bigdaddy_maybe/article/details/81946258

"""