# *     匹配前一个自佛出现0次或者无限次，即可有可无
# +     匹配前一个字符出现1次或者无限次，即至少有一次匹配
# ？    匹配前一个字符出现1次或者0次，要么1次，要么0次
# {M}   匹配前一个字符出现m次
# {m,n} 匹配前一个字符出现m到n次

import re

match_result = re.match("娃{2,4}","娃娃娃娃娃娃娃2")
if match_result:
    result = match_result.group()
    print(result)
else:
    print('匹配失败')


match_result = re.match("a+","aaaab")
if match_result:
    result = match_result.group()
    print(result)
else:
    print('匹配失败')