#猜拳游戏
#随机数模块
import random

cp_num = random.randint(1,3);
print(f'随机数是{cp_num}')

player_num = int(input('你出什么:'));
while((player_num) > 3 or (player_num < 0)):
    print("输入错误，请重新输入:")
    player_num = int(input('你出什么:'));

if (cp_num == 1) and (player_num == 1):
    print("都出剪刀，平局了")
elif (cp_num == 1) and (player_num == 2):
    print('电脑出剪刀，你出石头，你赢了')
elif (cp_num == 1) and (player_num == 3):
    print('电脑出剪刀，你出布，你是输了')
elif (cp_num == 2) and (player_num == 1):
    print('电脑出石头，你出剪刀，你输了')
elif (cp_num == 2) and (player_num == 2):
    print('电脑出石头，你石头，平局了')
elif (cp_num == 2) and (player_num == 3):
    print('电脑出石头，你出布，你是赢了')
elif (cp_num == 3) and (player_num == 1):
    print('电脑出布，你出剪刀，你赢了')
elif (cp_num == 3) and (player_num == 2):
    print('电脑出布，你石头，你输了')
else:
    print('电脑出布，你出布，平局了')






