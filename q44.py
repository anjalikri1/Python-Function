# Q44. Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last ‘N’ elements of the given list. ‘N’ is accepted from
# the user.
# Sample Input:
# 2
# Sample Output:
# q
# b
# Sample Input:
# 3
# Sample

def f():
    l=["a",1,"2",5,"b","q"]
    i=len(l)-1
    n=int(input("enter the value:"))
    while i>n:
        print(l[i])
        i-=1
f()

