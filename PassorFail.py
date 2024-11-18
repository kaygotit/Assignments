score = float(input("Enter your score(0-100): ")) #using float cos user might give a value with a decimal included.
if score >= 50 and score<=100: #checking if the score is between 50 and 100
    print("Pass")
elif score>100:
    print("Enter your score in the range (0-100)")
else:
    print("Fail")