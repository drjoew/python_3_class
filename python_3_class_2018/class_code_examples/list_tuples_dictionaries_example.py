#Example Code for Lists, Tuples, and Dictionaries
pet_owners = ['Alice' , 'Bob']
pet_types = ['Dog' , 'Cat', 'Bird']
pet_names = ['Ralph', 'Tom', 'Blackie', 'Boots']
pets = {pet_names[0]:pet_types[0], pet_names[1]:pet_types[1], pet_names[2]:pet_types[0], pet_names[3]:pet_types[1]}
#
number_of_pets = len(pet_names)
#
number_of_dogs  = 0
number_of_cats  = 0
number_of_birds = 0

for pet_count in range (0, number_of_pets) :
    if (pets[pet_names[pet_count]] == pet_types[0]):
            number_of_dogs = number_of_dogs + 1
    elif (pets[pet_names[pet_count]] == pet_types[1]):
              number_of_cats = number_of_cats +1
    elif (pets[pet_names[pet_count]] == pet_types[2]):
              number_of_birds = number_of_birds +1
#
print (pet_owners[0], 'and', pet_owners[1], 'have:')
print(number_of_dogs,  'animals of type', pet_types[0])
print(number_of_cats,  'animals of type', pet_types[1])
print(number_of_birds, 'animals of type', pet_types[2])

print('Their names are:')
for pet_count in range (0, number_of_pets) :
    print(pet_names[pet_count], 'a',pets[pet_names[pet_count]])
