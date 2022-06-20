# Q25. Given a list of numbers, write a Python program to count positive and negative numbers in a List using
# function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
# from __future__ import print_function

def f():
    l=[2, -7, 5, -64, -14]
    c=0
    c1=0
    for i in range(len(l)):
        if l[i]>0:
            c+=1
        if l[i]<0:
            c1+=1

    print("positive",c)
    print("negative",c1)
f()