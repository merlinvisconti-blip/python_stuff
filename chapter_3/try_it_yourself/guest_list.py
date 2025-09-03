dinner_guest = []

dinner_guest.append('marcus auralies')
dinner_guest.insert(0,'rollo tomassi')
dinner_guest.insert(1,'jesus')
print(dinner_guest)

print(f"\n{dinner_guest[0].title()} thank you for accepting my dinner invitation.")
print(f"\n{dinner_guest[1].title()} thank you for accepting my dinner invitation.")
print(f"\n{dinner_guest[2].title()} thank you for accepting my dinner invitation.")

uninvitaded = dinner_guest.pop(0)
print(f"\n Sorry {uninvitaded.title()} wont be able to make after all.")
dinner_guest[1] = 'marcos gonalez'
print(f"\n{dinner_guest[1].title()} thank you for accepting my invitation last minute. ")

print("\nFYI people I was able to get a bigger table so there will be more guest")
dinner_guest.insert(0,'joe')
dinner_guest.insert(2,'mark')
dinner_guest.append('solo')

print(f"\n{dinner_guest[0].title()} I cant wait to see you guys tonight. ")
print(f"\n{dinner_guest[1].title()} I cant wait to see you guys tonight. ")
print(f"\n{dinner_guest[2].title()} I cant wait to see you guys tonight. ")
print(f"\n{dinner_guest[3].title()} I cant wait to see you guys tonight. ")
print(f"\n{dinner_guest[4].title()} I cant wait to see you guys tonight. ")

print("There was an issue with the table it wont be ready and I can only invit two people. ")
uninvitaded_guest = dinner_guest.pop()
print(f"\nSorry {uninvitaded_guest.title()} you wont be able to come tonight")
uninvitaded_guest = dinner_guest.pop()
print(f"\nSorry {uninvitaded_guest.title()} you wont be able to come tonight")
uninvitaded_guest = dinner_guest.pop()
print(f"\nSorry {uninvitaded_guest.title()} you wont be able to come tonight")


print(dinner_guest)

print(f"\n{dinner_guest[0].title()} you are still invited.")
print(f"\n{dinner_guest[1].title()} you are still invited.")

del dinner_guest[0]
dinner_guest.remove('jesus')
print(dinner_guest)
print(len(dinner_guest))