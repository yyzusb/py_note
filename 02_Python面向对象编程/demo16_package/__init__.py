#当使用from * import *的方法导入包和模块的时候，可以在__init__模块中控制可以导入的模块
#使用包的时候，必须要要设置__all__来控制可导入的模块

__all__ = ['my_module_1']