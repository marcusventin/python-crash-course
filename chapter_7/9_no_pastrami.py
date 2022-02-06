sandwich_orders = ['pastrami', 'egg and cress', 'pastrami',
    'blt', 'pastrami', 'cheese']
finished_sandwiches = []

print("We regret to inform you that we have run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print("\nI've finished the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)