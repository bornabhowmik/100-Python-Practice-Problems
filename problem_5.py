# Write a program that will reverse a four digit number.Also it checks whether the reverse is true

number = int(input('Enter a four digit number: '))

revNumber = int(str(number)[::-1])

if number == revNumber :
    print('Your given number is pellindrome!')
else :
    print('Your given number is not pelindrome!')