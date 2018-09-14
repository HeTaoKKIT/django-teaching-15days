
# 闭包

def func(x):

    return x

a = func(1)
print(a)


#######
# 条件1：外部函数内嵌内部函数。 条件2：内部函数引用外部函数的局部变量
# 条件3：外部函数返回内部函数
def outer(x):

    def inner(y):
        return x + y
    
    return inner

a = outer(1)
print(a)
print(a.__closure__)

print(a(3))






