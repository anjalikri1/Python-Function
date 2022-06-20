# Q29. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit
# (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18,
# 20.

from re import I


def f(limit):
    s=0
    for i in range(limit+1):
        if i%3==0:
            s+=i
        if i%5==0:
            s+=i
    print("sum: ",s)
f(45)