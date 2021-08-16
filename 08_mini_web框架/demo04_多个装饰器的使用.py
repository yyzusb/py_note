#多个装饰器的时候，执行的顺序是从内到外的装饰顺序

def make_div(fn):
    print('make_div装饰器执行了')
    def inner():
        return '<div>' + fn() + '</div>'
    return inner

def make_p(fn):
    print('make_p装饰器执行了')
    def inner():
        return '<p>' + fn() + '</p>'
    return inner


@make_div
@make_p
def content():
   return '人生苦短，我用python'

print(content())


