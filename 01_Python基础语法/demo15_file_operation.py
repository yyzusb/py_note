'''f = open('test.txt','a')
f.write('123456789  ')
f.close()


#read函数返回str，readlines返回列表,readline一次读取一行内容
f = open('test.txt','r')
str = f.read()
print(type(str),'str = ',str)
f.close()

print()
print()

f = open('test.txt','r')
list_1 = f.readlines()
print(type(list_1),'list_1 = ',list_1)
f.close()
'''

#seek 函数
f = open('test.txt','a+')
f.seek(2,0)
list_1 = f.read()
print('list_1 = ',list_1)
f.close()



