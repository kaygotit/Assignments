temperature = float(input("Enter your current temperature in degrees: ")) #converting the user's input into a float
if temperature >= 30: #checkinh if user's temp is greater than 30 degrees 
    print("It's hot")
elif temperature >19 and temperature <29:
    print("It's warm")
else:
    print("It's cold")