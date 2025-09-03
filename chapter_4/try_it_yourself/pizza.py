favorite_pizza = ['pepperoni','cheese','meat lovers']
print(len(favorite_pizza))
friends_pizza = favorite_pizza[:]
favorite_pizza.insert(0,'veggie')
friends_pizza.append('pineapple')

print(f"My favorite pizzas are: ")
for pizza in favorite_pizza:
    print(f"{pizza.upper()}\n")


print(f"My friends favorite pizzas are:")
for pizza in friends_pizza:
    print(f"{pizza}\n")



