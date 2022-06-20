# Q41. Write a Python program to find the list with maximum and minimum length.
# Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0]
def max():
    l=[[0],[0,7], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
    i=0
    max=0
    min=len(l[i])
    k=[]
    n=[]
    while i<len(l):
        if len(l[i])>max:
            max=len(l[i])
            k=l[i]
        if len(l[i])<min:
            min=len(l[i])  
            n=l[i]  
        
        i+=1
    print(max,k)
    print(min,n)
max()    
        

