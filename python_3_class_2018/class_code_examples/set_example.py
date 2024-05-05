# example of use of sets
mens_names = set(["Carol", "Drew", "John", "James", "Jodi", "Kelly", "Lynn", "Tracy", "Joe", "Bill", "Frank"])
womens_names = set(["Carol", "Lois", "Joanne", "Christine", "Anne", "Drew", "Jodi", "Kelly", "Lynn", "Tracy", "Olivia"])
print("The Men's names are:", mens_names)
print("The Women's names are:",womens_names)
mens_names.add("Paul")
print("The updated Men's names are:", mens_names)
common_names = mens_names.intersection(womens_names)
print("The names common to men and women are:" ,common_names)
all_names = womens_names.union(mens_names)
print("All of the names are:")
for n in all_names:
    print(n)

