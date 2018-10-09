list = []
for item in range(0,11):
    list.append(item)

print("The first three items in this list are: " + str(list[0:3]))
print("Three middle items: " + str(list[4:7]))
print("The last three items: " + str(list[8:11]))

pizzas = ["pepperoni", "cheese", "meat"]
friend_pizzas = pizzas
friend_pizzas.append("veggie")

for item in pizzas:
    print("My favorite pizzas include " + item)

for item in friend_pizzas:
    print("My friends favorites include: " + item)

