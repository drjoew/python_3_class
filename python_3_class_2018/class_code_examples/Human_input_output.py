#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# example of getting user input and checking to make sure it is valid
while(1):
    user_input = input("Please enter a number: ")
    print("You entered ", user_input)
    try:                                            #check for valid input
        user_input=float(user_input)                  #convert number rather than string
    except ValueError:
        print("not a valid input")
    else:
        user_input_sqrd = user_input**2
        user_input_sqrt = user_input**(1.0/2.0)
        print("For the number", user_input, "\nthe square is", user_input_sqrd,"\nthe square root is", user_input_sqrt)

