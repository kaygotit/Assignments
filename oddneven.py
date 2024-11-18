number = float(input("Enter any number: ")) #I'm converting the user's input into a decimal
if not number.is_integer():  #Check if the number is not an integer
    print("""Invalid Input: Please enter a whole number.
Such as 1,2,88,42""")
elif number % 2 == 0:  
    print(f'{int(number)} is an even number')
else:  #so if it's not even, it's definitely odd
     print(f'{int(number)} is an odd number')



