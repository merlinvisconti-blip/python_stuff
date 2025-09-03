# Here is a list of three items that will the following functions
# len() sort() remove()

fountain_pens = ['lamy','visconti']
print(len(fountain_pens))
fountain_pens.insert(3,'pilot')
print(fountain_pens)
fountain_pens.sort(reverse=True)
print(fountain_pens)
fountain_pens.remove('pilot')
fountain_pens.reverse()
print(fountain_pens)
print(len(fountain_pens))