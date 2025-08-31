motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')


motorcycles.insert(0,'ducati')
del motorcycles[0]
print(motorcycles)

motorcycles.insert(0,'honda')
print(motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles.insert(2,'suzuki')
print(motorcycles)

first_owned = motorcycles.pop(0)
print(f"The first motorcycle that I owned was a {first_owned}.")
print(motorcycles)

motorcycles.insert(2,'suzuki')
motorcycles.append('ducati')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive of me.")