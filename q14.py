# Q14.Write a function to check if a number is prime or not.

def prime():
    n=int(input("enter the number :"))
    c=0
    i=1
    while i<=n:
        if n%i==0:
            c+=1
        i+=1
    if c==2:
        print("Prime number")
    else:
        print("not prime")
prime()