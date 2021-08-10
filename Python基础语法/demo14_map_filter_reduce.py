
import functools

def fn(num):
    return num + 2

list1 = [1,2,3,4,5]

result = map(fn,list1)
print(list(result))


def fn2(a,b):
    return a+b
result2 = functools.reduce(fn2,list1)
print(result2)
print(list(list1))

list2 = [1,2,3,4,5,6,7,8,9,10]
def fn3(x):
    return x % 2 == 0
result3 = filter(fn3,list2)
print(result3)
print(list(result3))


