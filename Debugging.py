#coding:utf-8

"用于调试相关的信息"

"""
1.print
2.assert expression, "错误信息提示"
3.logging
4.pdb

"""
__author__ = "kzk"


import logging


def logging_info():
	logging.basicConfig(format='%(asctime)s %(message)s',level = logging.INFO )
	logging.info('print datetime')


def main():
	logging.basicConfig(filename = 'test.log', level = logging.WARNING)
	logging.info('')
	logging.error('failed')



if __name__ == '__main__':
	#main()
	logging_info()