#if条件，网吧上网
age =  int(input('请输入年龄：'));

if age > 18:
    print('刷卡成功 ');

elif (age < 18) and (age > 16):
    print(f'{age}这个年龄需要家长陪着 ');
else:
    print('未成年不让玩');
