'''
正则表达式：是一种字符串的处理方式，用于字符串的匹配
字符串的匹配有两种：
    内容匹配：python re
        通过描述要匹配的内容和数量来实现匹配
    结构匹配：xpath
        通过描述要匹配的内容在整体中的结构来实现匹配
'''
import re
string='hello \n \t world 12h33 _ _'
# 格式：res=re.findall('正则表达式',字符串)

'''
类型匹配
'''
# . 除\n之外的所有内容
# res = re.findall('.',string)
# print(res)
# \d 匹配数字
# res = re.findall('\d\d\d',string)
# print(res)
# \D 非数字
# res = re.findall('\D',string)
# print(res)
# \w 匹配数字字母_
# res = re.findall('\w',string)
# print(res)
# \W 除数字字母_
# res = re.findall('\W',string)
# print(res)
# [] 返回括号中的任意一个字符
# res = re.findall('[a-zA-Z0-9]',string)
# print(res)
# 取反
# res = re.findall('[^a-zA-Z0-9]',string)
# print(res)
# | 匹配任意一边的字符
# res = re.findall('[hello|world]',string)
# print(res)
# () 组匹配
# 匹配两个数字
# res = re.findall('\d\d',string)
# print(res)    # ['12', '34']
# 匹配一个后面有数字的数字（分组后面的是条件）
# res = re.findall('(\d)\d',string)
# print(res)    # ['1', '3']

# res = re.findall('(\d)',string)
# print(res)
# 给分组写一个祖名id，实际内容完全相同
# res = re.findall('(?P<id>\d)',string)
# print(res)
# (?P=id)是对前面组名id匹配结果的引用
# res = re.findall('(?P<id>\d)(?P=id)',string)
# print(res)

'''
原样匹配
'''
# res = re.findall('l',string)
# print(res)

'''
长度匹配
'''
# * 匹配0个或多个数字，贪婪
# res = re.findall('\d*',string)
# print(res)
# + 匹配1个或多个数字，贪婪
# res = re.findall('\d+',string)
# print(res)
# {} 匹配指定次数
# res = re.findall('\d{2}',string)
# print(res)
# res = re.findall('\d{0,2}',string)
# print(res)
# ? 匹配0个或1个，禁止贪婪
# res = re.findall('\d?',string)
# print(res)

'''
特殊匹配
'''
# ^ 匹配开头
res = re.findall('^\w',string)
print(res)
# $ 匹配结尾
res = re.findall('\w$',string)
print(res)