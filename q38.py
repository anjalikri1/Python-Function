# Q38. Your task is to create function is Divided By (or is_divide_by) to check if an integer
# number is divisible by each out of two arguments.
# A few cases:
# (-12, 2, -6) -> true
# (-12, 2, -5) -> false
# (45, 1, 6) -> false
# (45, 5, 15) -> true
# (4, 1, 4) -> true
# (15, -5, 3) -> true

def dividedby(a,b,c):
    if a%b==0 and a%c==0:
        print(True)
    elif b%a==0 and b%c==0:
        print(True)
    elif c%a==0 and c%b==0:
        print(True)
    else:
        print(False)
x=int(input("enter the number :"))
y=int(input("enter the number :"))
z=int(input("enter the number :"))
dividedby(x,y,z)

