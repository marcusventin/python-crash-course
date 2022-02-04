my_toppings = ["mushrooms", "all the cheese", "not pineapple"]

friends_toppings = my_toppings[:]

my_toppings.append("egg")
friends_toppings.append("bacon")

print("My favourite pizzas are:")
for topping in my_toppings:
    print(topping)

print("\nMy friend's favourite pizzas are:")
for topping in friends_toppings:
    print(topping)