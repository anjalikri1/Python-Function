# Q45. Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user and update
# each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1
i=0
l=[]
while i<10:
    a=int(input("enter the number :"))
    l.append(a)
    i+=1
print(l)
def num():
    for i in range(len(l)):
        if l[i]%2==0:
            print(l[i]*100)
        else:
            print(l[i]*-1)
num()
        

 