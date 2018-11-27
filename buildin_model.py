#coding:utf-8



"""
collections
|__ namedtuple
|__ deque：deque是为了高效实现插入和删除操作的双向列表
|__ defaultdict：使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
|__ 


base64：
***Base64是一种通过查表的编码方法，不能用于加密***
https://blog.csdn.net/leslietuang/article/details/45128799

一种用64个字符来表示任意二进制数据的方法【a-zA-Z0-9,/+】提升版用的是 - _
Base64编码会把3字节的二进制数据编码为4字节的文本数据，
缺点：长度增加33%，
好处：编码后的文本数据可以在邮件正文、网页等直接显示。

如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
Base64用\x00字节在末尾补足后(在二进制数用全零在末尾补足)，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉
去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，
因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了


"""
import base64 as b64
import struct


print b64.b64encode('a')

struct.pack('>I', )

