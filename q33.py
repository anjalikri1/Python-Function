# Q33. Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi > 30 return "Obese"
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"

def bmi(w,h):
    bmi=w/(h**2)
    if bmi>30:
        op="obese"
    elif bmi<=18.5:
        op="underweight"
    elif bmi<=25.0:
        op="Normal"
    elif bmi<=30.0:
        op="Overweight"
    return op
a=eval(input("enter weight : "))
b=eval(input('enter height'))
f=bmi(a,b)
print(f)



