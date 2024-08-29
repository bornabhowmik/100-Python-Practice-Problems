# User will input (3ages).Find the oldest one

age1 = int(input('Enter age 1: '))
age2 = int(input('enter age 2: '))
age3 = int(input('enter age 3: '))

if age1>age2 and age1>age3:
    print("Age 1 is oldest.")
elif age2>age3 and age2>age1:
    print("Age 2 is oldest.")
else :
    print("Age 3 is oldest.")