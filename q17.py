# Q17. Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting
# to be 18.
def voter(age):
    if age>=18:
        print("can vote")
    else:
        print('can not vote')
voter(23)