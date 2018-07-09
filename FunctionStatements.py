def fu_math(x,y):
    z = x * y
    return(z)

def fu_sumNumbers(*args):
    total = 0
    for x in args:
        total = total + x
    return total

def healthcalculator(age,apples,cigretts):
    myage = 100 - age + (3.5 * apples) - (1.5 * cigretts)
    return myage

a = fu_math(15,15)
print(a)

a = fu_math(y=15,x=16)
print(a)

a = fu_sumNumbers(1,2,3,4,5,6,7,8,9)
print(a)

mydata = [41, 7, 1]
print(healthcalculator(*mydata))