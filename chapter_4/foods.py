my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My first two favorite foods are:")
for food in my_foods[:2]:
    print(food)

print("\nMy friend's last two favorite foods are:")
for food in friend_foods[-2:]:
    print(food)
