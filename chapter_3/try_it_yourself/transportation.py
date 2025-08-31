# this is a list a my favorite modes of transportation

transportation_mode = ['car','scooter','airplane','bus']
print(f"\n I own a {transportation_mode[0].upper()}.")
print(f"\nI once got hurt on a {transportation_mode[1]}.")
print(f"\nI've only been once on a {transportation_mode[2]}.")
print(f'\n{transportation_mode[3]} can carry alot of people at one time.')

print("\nAfter this line a for loop starts")
for trans in transportation_mode:
    print(f"\n{trans.upper()} is a mode of transportation.")