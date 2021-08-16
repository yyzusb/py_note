#__name__ 系统变量，显示当前模块的名字 ，如果在当前模块中打印，会显示__main__ 如果在其他模块导入后打印，会显示模块的名字

def test(a,b):
    return a+b;

if __name__ =='__main__':
    print(__name__)

def print_module_name():
    print(__name__)




