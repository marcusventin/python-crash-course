person = {
    'first_name' : 'marcus',
    'last_name' : 'ventin',
    'pet' : 'jumble',
    }

person2 = {
    'first_name' : 'monty',
    'last_name' : 'python',
    'pet' : 'parrot',
    }

person3 = {
    'first_name' : 'sancho',
    'last_name' : 'panza',
    'pet' : 'dapple',
    }

people = [person, person2, person3]

# for person in people:
#     print(f"\nFirst name: {person['first_name'].title()}.")
#     print(f"Surname: {person['last_name'].title()}.")
#     print(f"Pet: {person['pet'].title()}.")

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    pet = person['pet'].title()

    print(f"\n{name} lives with {pet}.")