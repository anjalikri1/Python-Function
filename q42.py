# Q42. Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
def f():
    l=[12, 67, 98, 34]
    i=0
    l1=[]
    while i<len(l):
        n=l[i]
        s=0
        while n>0:
            r=n%10
            s+=r
            n=n//10
        l1.append(s)
        i+=1
    print(l1)
f()

        


