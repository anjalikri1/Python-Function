# Q40. Write a function For example, if we give 9119 the function should return 811181, as the square of 9
# is 81 and square of 1 is 1.

def sqr(num):
    i=0
    s=""
    while num>0:
        r=num%10
        a=r**2
        s+=str(a)
        num=num//10
    print(s)
sqr(232)
    