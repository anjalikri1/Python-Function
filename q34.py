# Q34. Write a function which converts the input string to uppercase.



# [10, 14, 2, 23, 19] --> 42 (= 23 + 19)
# [99, 2, 2, 23, 19] --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.
def add():
    l= [10, 14, 2, 23, 19]
    max=0
    i=0
    while i<len(l):
        if l[i]>max:
            max=l[i]
        i+=1
    print(max)
    max1=0
    i=0
    while i<len(l):
        if l[i]>max1 and l[i]!=max:
            max1=l[i]
        i+=1
    print(max1)
    s=max+max1
    print(s)
add()
    
    

