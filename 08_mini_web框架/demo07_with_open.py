#为了简化文件读写，提供了with open方式，文件操作完成后，自动关闭，即使有异常也会关闭文件，使代码继续执行

with open('1.txt','w') as filea:
    filea.write('hello python')
with open('1.txt', 'r') as filea:
    print(filea.read())
