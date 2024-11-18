number1, number2 = input("Enter two numbers separated by space: ").split()

# Converting the inputs given from string into float
num1 = float(number1)  
num2 = float(number2)  

print(f"First number: {number1}")
print(f"Second number: {number2}")

if num1 > num2:
    print("The first number is greater")
elif num2 > num1:
    print("The second number is greater")
elif num1 == num2:
    print("Both numbers are equal") 
 