def f():

    l=[True, True, True, False,
    True, True, True, True ,
    True, False, True, False,
    True, False, False, True ,
    True, True, True, True ,
    False, False, True, True]
    c=0
    i=0
    c1=0
    while i<len(l):
        if l[i]==True:
            c+=1
        if l[i]!=True:
            c1+=1

        i+=1
    print("present sheep",c)
    print("null",c1)
f()