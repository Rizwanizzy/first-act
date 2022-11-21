# fun= lambda a,b,c:(a+b)/c
# print(fun(10,20,5))

def multiply(num):
    return lambda i: i * num


x = multiply(5)
num1=x(10)
print(num1)

y=multiply(6)
num2=y(11)
print(num2)
print(num1+num2)

