common_animals = []
common_animals.append('dog')
common_animals.insert(0,'cat')
common_animals.insert(1,'bird')

print(common_animals)

for animals in common_animals:
    print(f"All of these animals make great house pets {animals.upper()}.\n")
print("All of the animals have fur")