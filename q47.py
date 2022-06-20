# Q47. Draw a flowchart to take a list of 7 numbers from the user, print True if the complete list consists of
# consecutive numbers with any constant difference between numbers. Print False otherwise.
l=[]
for i in range(7):
    n=int(input("number"))
    l.append(n)
print(l)
k=1
s=l[1]-l[0]
count=0
while(k<len(l)):
    if (l[k]-l[k-1])==s:
        count+=1
    k+=1
if count==(len(l)-1):
    print(s,"True")
else:
    print("False")

