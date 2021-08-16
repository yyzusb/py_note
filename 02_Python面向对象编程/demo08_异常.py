try:
    f = open('a.txt','r');
except:
    print('打开文件错误');

###################################################################################
#捕获指定异常
try:
    print(num);
except NameError:
    print('捕获指定异常类');


###################################################################################
#捕获多个指定异常
try:
    print(1/0);
except (NameError,ZeroDivisionError):
    print('捕获多个指定异常类');


###################################################################################
try:
    print(1/0);
except (NameError,ZeroDivisionError) as result:#捕获异常描述信息
    print(result);


###################################################################################
number = 1
try:
    print(number);
#捕获所有异常
except Exception as result:
    print(result);
else:
    print('exception测试，没有任何异常：');

###################################################################################
try:
    f = open('test.txt','r');
except Exception as result:
    print(result,'没有文件，现在开始创建');
    f = open('test.txt','w');
else:
    print('没有异常');
finally:
    f.close();


###################################################################################
try:
    f = open('test.txt','r');
except Exception as result:
    print(result,'\n没有文件，现在开始创建');
    f = open('test.txt','w');
else:
    print('没有异常');
finally:
    f.close();
    print('文件创建成功')

###################################################################################














