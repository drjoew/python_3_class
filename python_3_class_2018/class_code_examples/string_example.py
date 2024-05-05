# Example of use of strings and string manipulation
#
string_1 = 'Hello Students'                 # ' and ' defines string
string_2 = "Welcome to the Python Class"    # " and " can also define string

print(string_1)
print(string_2)

string_3 = string_1[0:6]+"and " + string_2
print(string_3)

string_4 = "Hello"                          # hello is stored as 5 elements
for i in range(0,5):                        # we can address each element
    print(string_4[i])
for i in range(1,6):                        # we can also print a range of elements
    print(string_4[0:i])                    # [0:B] addresses 0 to B-1 elements
