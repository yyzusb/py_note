#^匹配开头，$匹配结尾

import re

match_result = re.match("^娃{2,4}","娃娃娃娃娃娃娃2")
if match_result:
    result = match_result.group()
    print(result)
else:
    print('匹配失败')


match_result = re.match(".*娃$","哈娃娃")#匹配结尾的时候，要注意前面要通配一下最好用.*
if match_result:
    result = match_result.group()
    print(result)
else:
    print('匹配失败')



match_result = re.match(".*[^47]$","哈娃娃")#不要47结尾
if match_result:
    result = match_result.group()
    print(result)
else:
    print('匹配失败')