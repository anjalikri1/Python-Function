# Q7.Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(w,h):
    bmi=w/(h**2)
    if bmi<=18.5:
        op="Underweight"
    elif bmi<=25.0:
        op="Normal"
    elif bmi<=30.0:
        op="Overweight"
    else:
        op="Obese"
    return op
a=int(input("enter the weight : "))
b=int(input("enter the height : "))
r=bmi(a,b)
print(r)

