# Q9.Write a Python program to generate and print a list of first and last 5 elements where
# the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]

l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
i=0
a=[]
b=[]
while i<len(l):
    if i<5:
        s=l[i]**2
        a.append(s)
    if i>=25:
        s1=l[i]**2
        b.append(s1)
    i+=1
print(a)
print(b)




