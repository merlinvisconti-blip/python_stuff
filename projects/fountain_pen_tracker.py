# This the start of my fountain pen project.
# At the end of it a website will be build that we keep track of my collection of fountain pens along 
# with other details brand, model , cost

fountain_pen_collection = []

fountain_pen_size = input("Please enter how many fountains you have ? ")
int(fountain_pen_size)
print(type(fountain_pen_size))

print(f"That is so cool that you this many {fountain_pen_size}")

pen_0 = input("\nPlease enter your first fountain pen: ")
fountain_pen_collection.append(pen_0)
pen_1 = input("\nPlease enter your second fountain pen: ")
fountain_pen_collection.append(pen_1)


#for pen in fountain_pen_size:
#    pen = input("Please enter your fountain pen name")
#    fountain_pen_collection.append(pen)
for pen in fountain_pen_collection:
    print(f"{pen}")
