# Q35. Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)
# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky".

def drinks(age):
    if age<=14:
        print("drink toddy")
    elif age>=14 and age<18:
        print("drink coke")
    elif age>=18 and age<21:
        print("drink beer")
    elif age>=21:
        print("drink whisky")
n=int(input("enter the age"))
drinks(n)
    