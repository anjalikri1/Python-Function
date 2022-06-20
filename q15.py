# Q15.Write a function to calculate power of a number raised to other ( a b ) .
def power(n,p):
    r=n**p
    return r
a=int(input("enter the no: "))
b=int(input("enter the power :"))
x=power(a,b)
print(x)
