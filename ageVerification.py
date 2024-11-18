age = int(input("Enter your age without the years: ")) #I'm converting the user's input in to an integer
if age < 18: #checking to see if user is below 18 years of age
    print("You are a minor")
else:
    print("You are an adult")