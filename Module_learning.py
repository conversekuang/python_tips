#coding:utf-8

"This is a file to record Module Learning tips"
#一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

#使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
__author__ = "kzk"

#以上为python的模板，以后需要规范化。




if __name__ == '__main__':
	import sys
	print sys.argv
	print sys.argv[0]
	#sys模块有一个argv变量，用list存储了命令行的所有参数。
	#argv至少有一个元素，因为第一个参数永远是该.py文件的名称


	"""
	>>> python  xxx.py
	当我们在命令行运行模块文件时，
	Python解释器把一个特殊变量__name__置为__main__，
	而如果在其他地方导入该hello模块时，if判断将失败

	"""