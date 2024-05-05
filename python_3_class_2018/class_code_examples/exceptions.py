"""
This code presents examples for serveral types of exception handling.
The goal is to keep the code running smoothly in the presence of problems
like poor user input
unknown errors
"""

# try except example
for i in range(1,3):
    try:
        y= input("Please enter a number: ")
        x = int(y)
        print("thank you, that was a valid number of value: ",x)
    except ValueError:
        print("Oops!  That was not a valid number. You entered \" ", y,  "\" Try again...")
    print(" ")

# try except finally example
for i in range(1,3):
    x= input("Please enter the numerator  : ")
    x=int(x)
    y= input("Please enter the denominator: ")
    y=int(y)
    try:
        result = x/y
        print("The result of the division is ",result)
    except ZeroDivisionError:
        print("Oops! dividing by zero Try again...")
    finally:
        print("finally runs whether there is an exception or no exception")
    print(" ")

# assert example
for i in range(1,2):
    try:
        y= input("Please enter a number: ")
        x = int(y)
        assert int("a")
        print("thank you, that was a valid number of value: ",x)
    except ValueError:
        print("Oops!  That was not a valid number. You entered \" ", y,  "\" Try again...")
    print(" ")

# try except finally example with raise
for i in range(1,2):
    x= input("Please enter the numerator  : ")
    x=int(x)
    y= input("Please enter the denominator: ")
    y=int(y)
    try:
        result = x/y
        raise ZeroDivisionError
        print("The result of the division is ",result)
    except ZeroDivisionError:
        print("Oops! dividing by zero Try again...")
    finally:
        print("finally runs whether there is an exception or no exception")
    print(" ")

# raise example without being handled
print("now we raise an exception without it being handled")
raise ZeroDivisionError
