#coding:utf-8
#当函数的参数不确定时
#*args 没有key值    list,tuple, etc.
#**kwargs有key值		dict
def main(*args,**kwargs):
	for arg in args:
		print arg
	for k, v in enumerate(kwargs):
		print k, v


if __name__ == '__main__':
	args = [1,2,100,50,10]
	kwargs = {'dict':'name'}
	main(args,kwargs)