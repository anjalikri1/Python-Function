# Q2. Write a Python function to find the Max of three numbers.
def max(a,b,c):
    if a>b and a>c:
        print("greater",a)
    elif b>c:
        print("greater",b)
    else:
        print("greater",c)
n1=int(input("enter the number1: "))
n2=int(input("enter the number2: "))
n3=int(input("enter the number3: "))
max(n1,n2,n3)

