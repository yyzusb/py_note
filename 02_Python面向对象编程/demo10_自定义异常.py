class InputLengthError(Exception):
    def __init__(self,length,min_length):
        self.length = length;
        self.min_length = min_length;

    def __str__(self):
        return f'您输入的密码长度是{self.length},系统要求最短{self.min_length}'


def main():

    try:
        con = input("请输入密码");
        if(len(con) < 3):
            raise InputLengthError(len(con),3);
    except Exception as result:
        print(result);
    else:
        print('密码设置成功');

main();





