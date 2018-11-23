#coding:utf-8

__author__ = 'kzk'

"file to learn regular expression"

"""
具体字符就是精确匹配

.   除了新的一行外的任何字符
\b  匹配空字符串，但仅匹配单词的开头或结尾。
    单词被定义为字母数字或下划线字符的序列，因此单词的结尾由空格或非字母数字的非下划线字符表示。

\d  [0-9]数字
\D  [^0-9]非数字

\w   [a-zA-Z0-9_]   数字或字母
\w   [^a-zA-Z0-9_]  非数字或字母

\s  [ \t\n\r\f\v] 可以匹配一个空格（也包括Tab等空白符）
\S  [^ \t\n\r\f\v]
贪婪：
？  0或1 个字符
*   任意字符，包括0个
+   至少一个字符
{n,m}  n-m 个字符


非贪婪：
*?, +?, ??
{m,n}?
添加？ 在限定符之后，它以非贪婪或最小的方式执行匹配; 尽可能少的字符将匹配


\|  或者 [|]  ： 匹配字符 |

\-  -是特殊字符 需要转义 

[0-9a-zA-Z\_] 匹配一个 数字，字母，下划线
[0-9a-zA-Z\_][0-9a-zA-Z\_]* 字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串
[0-9A-Fa-f]   十六进制数

A|B	可以匹配A或B   #(P|p)ython可以匹配'Python'或者'python'
^	表示行开头
$	表示行结束
[]	匹配：
	（1）在[]中“-”两边有数字，来表示范围 
	（2）在[]中，- 转义\- 或者出现在第一个位置，或最后一个。表示-符号本身。eg：[a\-z],[a-]
	（3）特殊字符串在[]中，失去特殊意义。eg： [(+*)] 表示匹配字符'(', '+', '*', 或者 ')'
	（4）在[]中不包括某字符。 eg：[^5]:不包括5
	  #不太懂#（5）要匹配集合中的文字']'，请在其前面加上反斜杠，或将其放在集合的开头。 例如，[（）[\] {}]和[]（）[{}]都将匹配括号。 

(..) :
	（1）匹配括号内的正则表达式，组的开始和结束
	（2）匹配'(',')'本身可以通过 \(,\) 或者[(], [)]来进行


"""
import re


"""
re.compile(pattern, flags=0)
将正则表达式模式编译为正则表达式对象，可以使用其match（）和search（）方法进行匹配。

========================================
prog = re.compile(pattern)
result = prog.match(string)

等价于

result = re.match(pattern, string)
========================================



re.search(pattern, string, flags=0)  
在字符串中搜索并找到第一个与模板匹配的位置，并返回匹配实例， *****MatchObject instance实例******

re.match(pattern, string, flags=0)
如果字符串开头的零个或多个字符与正则表达式模式匹配，则返回相应的*****MatchObject instance实例******。 如果字符串与模式不匹配，则返回None;
在MULTILINE模式下，match（）仅匹配字符串的开头。    eg： re.match('X', 'A\nB\nX', re.MULTILINE)  # No match  虽然格式上，ABX是每一行的开头，但是字符串中X不在开头。

re.search vs  re.match
re.match（）仅在字符串的开头检查匹配，而re.search（）检查字符串中的任何位置

re.split(pattern, string, maxsplit=0, flags=0)
按模式的出现拆分字符串。 如果在模式中使用捕获括号，则模式中所有组的文本也将作为结果列表的一部分返回。 
如果maxsplit非零，则最多发生maxsplit拆分，并且字符串的其余部分将作为列表的最后一个元素返回。

re.findall(pattern, string, flags=0) 
返回字符串中pattern的所有非重叠匹配，返回的是：字符串列表。 a list of strings




*****re.MatchObject instance实例******
group()表示的就是要提取的分组; group(0)永远是原始字符串，group(1)、group(2)……表示第1、2……个子串

groups() 返回包含匹配的所有子组的元组，从1到多个组都在模式中。 默认参数用于未参与匹配的组; 它默认为None。
>>> m = re.match(r"(\d+)\.?(\d+)?", "24")
>>> m.groups()      # Second group defaults to None.
('24', None)
>>> m.groups('0')   # Now, the second group defaults to '0'.
('24', '0')



"""
if __name__ == '__main__':
	"""
	case 1:
	s = 'Ross McFluff: 834.345.1254 155 Elm Street'
	pattern = re.compile(':? ') #匹配的是“ ”和“： ”两种格式，空格 还有 冒号空格
	print re.split(pattern, s, 4)#最多分4下，剩下统一返回为一个字符串
	"""
	"""
	case 2:
	res =  re.findall('(\w+)ly\w*','He was carefully lilys disguised but captured quickly by police.')
	print res
	
	for i in res:
		x = re.match('\w+ly$', i)
		if x:
			x.group(0)
	"""
	"""
	case 3:
	x = re.findall('(\d{4})\.(\d{2})\.(\d{2})','2017.05.31,2018.08.30')
	print x
	#print x.group(1)+'-'+x.group(2)+'-'+x.group(3)

	str1 = '2017.05.31,2018.08.30'
	print str1.replace('.','-')
	"""
	"""


	"""


