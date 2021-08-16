#三目运算符
a,b = 3,21;
c = a if a > b else b;
print(c)

#while
count = 0;
result = 0;
while(count <= 100):
    result+=count;
    count += 1;
print(result)

count = 0;
result = 0;
while(count <= 100):
    if count % 2 == 0:
        result+=count;
    count += 1;
print(result)

count = 0;
result = 0;
while(count <= 100):
    if count > 50:
        break
    result+=count;
    count += 2;
print('break',result)

count = 0;
result = 0;
while(count <= 100):
    if(5< count <96):
        count += 1
        continue
    result+=count;
    count += 1;
else:
    print('countinue',result)


a = 'apple'
for i in a:
    print(a)
else:
    print('finish')



