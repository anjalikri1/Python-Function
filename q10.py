# Q10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the
# sum (also as a string):
# "4", "5" --> "9"
# "34", "5" --> "39"
# Notes:
# If either input is an empty string, consider it as zero.

def stringS(a,b="12"):
    sum=int(a)+int(b)
    return sum
x=input("enter the no :")
r=stringS(x)
print(r)

