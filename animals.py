# read animals.txt
# and write animals_new.txt

animal_file = open('animals.txt', 'r')
animals_content = animal_file.readlines()
animal_file.close()

# print(animals_content)
animals_list = []
for animal in animals_content:
    animals_list.append(animal.strip())

# print(' '.join(animals_list))

animals_new = open('animals_new.txt', 'w')
animals_new.write(' '.join(animals_list))
animals_new.close()