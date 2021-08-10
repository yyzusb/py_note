def sum_result(num):
    if num == 1:
        return 1;
    return  num + sum_result(num - 1)

a = sum_result(3)
print(a)