import re

'''
1、倒入模块
2、re.match（）第一个参数是正则规则，第二个参数是要匹配的表达式
3、返回一个对象
4、通过 返回对象的.gourp()函数来获取正则结果

1、[]    匹配[]中列举的字符
2、\d    匹配数字0-9
3、\D    匹配非数字
4、\s    匹配空格，table
5、\S    匹配非空格，table
6、\w    匹配普通字符a-z，A-Z,0-9
7、\W    匹配非特殊字符
'''
match_result = re.match("葫芦娃[12]","葫芦娃2")#葫芦娃后面匹配1或者2中的一个字符
if match_result:
    result = match_result.group()
    print(result)
else:
    print('匹配失败')


match_result = re.match("[\D]","asd")
if match_result:
    result = match_result.group()
    print(result)
else:
    print('匹配失败')





