#拆包
def return_tuple():
    return 100,200
a,b = return_tuple()
print(a,b)

dict_1 = {'name':'bill','age':18}
c,d = dict_1
print(c,d)

e = 3
f = e
print(id(e))
print(id(f))