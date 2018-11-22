#coding:utf-8     coding与它们之间都不能有空格。否则也会报错
"IO programming"

"""
输入输出编程


同步IO:  CPU等待输入输出结果，什么都不干，等待结束后，继续执行相关代码。
异步IO:	 CPU无需等输入输出结果，等待执行结束后，通知CPU再去执行对应的代码
（通知CPU的方式有很多，回调函数，或者发信号而CPU要去检查是否接到信号。）

"""


"""
#读文件

read()会一次性读取文件的全部内容, 内存不够的情况下，容易出错
read(size)方法，每次最多读取size个字节的内容
readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list


file-like Object
像open()函数返回的这种有个read()方法的对象，file-like Object不要求从特定类继承，只要写个read()方法就行。


前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件

#读取二进制文件：
要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
f = open('xxx.jpeg,'rb')


#读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码
f = open('gbk.txt','rb')
u = f.read().decode('gbk')  #unicode编码


#Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode：
import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() #





#py3
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()




##StringIO 和 BytesIO

很多时候，数据读写不一定是文件，也可以在内存中读写。StringIO顾名思义就是在内存中读写str。

f = StringIO() 内存中读写字符串,py2.7中只能对unicode
f.write('')   #写
f.getvalue()  #读

"""

def PrintDecorator(func):
	def wapper(*args,**kwargs):
		func()
		print func.__name__,'函数执行完毕'
	return wapper


def  fileReader():
	try:
		f = open('tip.txt','r')
		for i in f.readlines():
			print i
	except IOError as e:
		print e
	finally:
		f.close()


def fileReader2():
	with open('tip.txt','r')  as f:
		for i in f.readlines():
			print i


from io import StringIO

def RWIO():
	s = StringIO()
	s.write(u'i')
	s.write(u'h')
	s.write(u'u')
	x = "我们"
	s.write(x.decode('utf-8'))
	print  s.getvalue()



import codecs


@PrintDecorator
def codecsReadFile():
	with codecs.open('gbk.txt','rb',encoding='gbk') as f:
		u = f.read(4)
		print u



@PrintDecorator
def codecsWriteFile():
	with codecs.open('gbk.txt','w') as f :
		#f.write('你说'.decode('utf-8'))  #字符串通过utf-8编码，需要先解码成unicode
		f.write('我们不是')

@PrintDecorator
def write_file():
	with open('new.txt','w') as f:
		f.write('我们')



import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

"""
将类信息与json信息对应
"""
def student2dict(std):
    return {
        'name': std.name,
        'age':  std.age,
        'score': std.score
    }


#序列化:我们把变量从内存中变成可存储或传输的过程称之为序列化
#pickle.dumps(d)  方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
#pickle.dump(d, f) 输出到文件f
#d = pickle.load(f) 序列化后的文件反序列化出来


if __name__ == '__main__':
	#fileReader()
	#codecsWriteFile()
	#write_file()
	#codecsReadFile()
	s = Student('Bob', 20, 88)
	print(json.dumps(s, default=student2dict))

	