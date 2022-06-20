# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and
# lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12
def count(str):
    c1=0
    c2=0
    for i in str:
        if i>="A" and i<="Z":
            c1+=1
        if i>="a" and i<="z":
            c2+=1
    print("upper case :",c1)
    print("lower case :",c2)
str=input("enter the string :")
count(str)

            
