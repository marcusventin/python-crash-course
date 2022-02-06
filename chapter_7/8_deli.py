sandwich_orders = ['egg and cress', 'blt', 'cheese']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("\nI've finished the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)