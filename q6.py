# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8].
def even():
    l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    a=[]
    for i in range(len(l)):
        if l[i]%2==0:
            a.append(l[i])
    print(a)
even()
    
