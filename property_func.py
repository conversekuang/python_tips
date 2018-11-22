#coding:utf-8
"练习property"


__author__ = "kzk"

class Screen(object):

	@property
	def width(self):
		return self._width

	#变量名不与方法名一致，

	@width.setter
	def width(self, value):
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self._height = value

	@property
	def resolution(self):
		return self._height * self._width


if __name__ == '__main__':
	s = Screen()
	s.width = 1024
	#与方法名一致，
	s.height = 768
	print('resolution =', s.resolution)
	if s.resolution == 786432:
		print('测试通过!')
	else:
		print('测试失败!')

	"""
	通过封装函数来操作属性值，但是传统的s.get_value(),  s.set_value()函数调用麻烦，
	直接s.value，通过@property将函数属性化，对属性值进行修改十分方便。

	@perperty可以将类的方法转变为属性，分为读和写两个属性，
	通过定义读不定义写可以设定只读属性。
	@property提供了可读可写可删除的操作

	@height.deleter
	def height(self):
    	del self.true_height

	"""