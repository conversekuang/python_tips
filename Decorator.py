#coding :utf-8

def decorator(fuc):
	def wapper(para):
		print("__wapper__")
		fuc(para)
		print("__wapper__")
	return wapper


def Outer(fuc):
	def wapper(para):
		print("__Outer__")
		fuc(para)
		print("__Outer__")
	return wapper


@Outer
@decorator
def func(para):
	print("__core__function %s" % para)







if __name__ == '__main__':
	func("kzk")

