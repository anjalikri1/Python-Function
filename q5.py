# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5].

def unque():
    l=[1,2,3,3,3,3,4,5]
    a=[]
    for i in range(len(l)):
        if l[i] not in a:
            a.append(l[i])
    print(a)
unque()
