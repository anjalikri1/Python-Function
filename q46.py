# Q46. Draw a flowchart to take a list of N numbers from the user, print True if the complete list consists of
# consecutive numbers with a difference of one. Print False otherwise.
# Sample Input:
# 1 2 3 4 5 6 7
# Sample Output:
# True
# Sample Input:
# 45 46 47 48 49 51 52
# Sample Output:
# False
# Sample Input:
# 4 5 6 7 8 9 10
# Sample Output:

a=int(input("enter the no of element that you want to add: "))
i=1
l=[]
while i<=a:
    num=int(input('enter the value: '))
    l.append(num)
    i+=1
print(l)

k=1
s=l[1]-l[0]
count=0
while(k<len(l)):
    if (l[k]-l[k-1])==s:
        count+=1
    k+=1
if count==(len(l)-1):
    print(s,"same difference")
else:
    print("not same")

    
    


