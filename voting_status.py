def age_verification(status):
    if  status >= 18:
        print("Congratulations! You can vote")
    else:
        Print("Sorry you can not vote")

inp = input("Please enter your age to check if you can vote")
try:
    age = float(inp)
except:
    print("Wrong! Please enter a number")

age_verification(age)
    
