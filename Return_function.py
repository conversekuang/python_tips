#coding:utf-8
"""
第一个global是定义一个全局变量a
第二个global在嵌套函数中定义，作用是修改全局变量。
嵌套函数中的global只对整体环境下的变量（全局变量）起作用，而不对函数内的变量起作用。
如果第一个a不定义成global，那么嵌套函数是找不到a的，
因为此时a是一个局部变量，嵌套函数不能给外部函数中的局部变量重新赋值，这时的a相当于未定义。
"""

#https://blog.csdn.net/Virtual_Func/article/details/50551076?utm_source=blogxgwz8

def CreateCounter(para):
	global x 
	x = para
	def Counter():
		global x
		x = x+1
		return x
	return Counter

def sum():
	m = 3
	def var():
		n = 2
		print n + m
	print m
	var()

if __name__ == '__main__':
	#wq = CreateCounter(100)
	#print wq(), wq()
	sum()