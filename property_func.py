#coding:utf-8
"练习property"


__author__ = "kzk"

class Screen(object):

	def __init__(self):
		
	
	@property
	def width(self):
		return self.xwidth

	@width.setter
	def width(self, value):
		self.xwidth = value

	@property
	def height(self):
		return self.xheight

	@height.setter
	def width(self, value):
		self.xheight = value	

	@property
	def resolution(self):
		return self.xheight * self.xwidth


if __name__ == '__main__':
	s = Screen()
	s.xwidth = 1024
	s.xheight = 768
	print('resolution =', s.resolution)
	if s.resolution == 786432:
		print('测试通过!')
	else:
		print('测试失败!')

	"""
	@perperty可以将类的方法转变为属性，分为读和写两个属性，
	通过定义读不定义写可以设定只读属性。
	
	"""