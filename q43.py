# Q43. Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last ‘N’ elements of the given list. ‘N’ is accepted from
# the user.
# Sample Input:
# 1
# Sample Output:
# q
# Sample Input:
# 3
# Sample Output:
# 5
# b
# q
def f():
    l=["a",1,"2",5,"6","q"]
    a=len(l)
    n=int(input("enter the num"))
    while n<len(l):
        print(l[a-n])
        n-=1
f()



