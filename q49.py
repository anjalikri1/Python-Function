# Q49. Write a flowchart which takes an input N. Then input N numbers. Then for each of the N numbers, print
# “even” if the number is even or and “odd” if the number is odd.

def check(n):
    if n%2==0:
        print(n,"even")
    else:
        print(n,"odd")
check(5)