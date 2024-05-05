#Example Code for Lists, Tuples, and Dictionaries
""" What needs to be improved:
1) more comments
2) allow for duplicate pet names
When trying to add duplicate pet names, the code does not work correctly
The way to fix this is not use a dictonary for pet but use sets
This is an example of using dictionaries which is now clear is not the best way to solve the problem
I can either make both Toms cat or dogs but not one a cat and one a dog.
"""
# The purpose of this program is to keep a list of animals owned
# by two pet owners (currently Alice and Bob)
# They currently own dogs and cats but plan to purchase a bird in the future
# The program can be extended by:
# adding to the list of pet_owners, pet_types, or pet_names
 

# First build the information
pet_owners = ['Alice' , 'Bob']
pet_types = ['Dog' , 'Cat', 'Bird']
pet_names = ['Ralph', 'Tom', 'Blackie', 'Boots', 'Tom']
pets = {pet_names[0]:pet_types[0], pet_names[1]:pet_types[1], pet_names[2]:pet_types[0], pet_names[3]:pet_types[1], pet_names[4]:pet_types[0]}
#
# allow for a change in the number of pet names by getting its length
# rather than hard coding the length
number_of_pets = len(pet_names)
#
# set up the initial values for the number of each type of pet
number_of_dogs  = 0
number_of_cats  = 0
number_of_birds = 0
#
#When we find a pet type, increment its number by one
for pet_count in range (0, number_of_pets) :   # start of for pet_count
    if (pets[pet_names[pet_count]] == pet_types[0]): #start of if
            number_of_dogs = number_of_dogs + 1
    elif (pets[pet_names[pet_count]] == pet_types[1]):
              number_of_cats = number_of_cats +1
    elif (pets[pet_names[pet_count]] == pet_types[2]):
              number_of_birds = number_of_birds +1 # end of if
# end of for pet_count
#
# Now that we know the number of each time of pet, print the information
print (pet_owners[0], 'and', pet_owners[1], 'have:')
print(number_of_dogs,  'animals of type', pet_types[0])
print(number_of_cats,  'animals of type', pet_types[1])
print(number_of_birds, 'animals of type', pet_types[2])

print('Their names are:')
for pet_count in range (0, number_of_pets) :
    print(pet_names[pet_count], 'a',pets[pet_names[pet_count]])
# program finished
