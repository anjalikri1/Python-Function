# Q30. Write a function that prints all the prime numbers between 0 and limit where limit is a
# parameter.

def prime(limit):
    a=1
    while a<=limit:
        c=0
        i=1
        while i<=a:
            if a%i==0:
                c+=1
            i+=1
        if c==2:
            print("Prime number",a)
        else:
            print("not prime number",a)
        a+=1
prime(100)            




