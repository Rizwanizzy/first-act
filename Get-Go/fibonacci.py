num = int(input("enter a number:"))
num1 = 0
num2 = 1
fib = 0
if num <= 0:
    print("please enter a valid number")
else:
    print(num1,end=" ")
    for i in range(num - 1):
        num1 = num2
        num2 = fib
        fib = num1 + num2
        print(fib,end=" ")
