favourite_numbers = {
    'Marcus' : 4,
    'Richard' : 1,
    'Gavin' : 5,
    'Laura' : 12,
    'Kevin' : 15,
}

print(f"Marcus's favourite number is {favourite_numbers['Marcus']}")
print(f"Richard's favourite number is {favourite_numbers['Richard']}")
print(f"Gavin's favourite number is {favourite_numbers['Gavin']}")
print(f"Laura's favourite number is {favourite_numbers['Laura']}")
print(f"Kevin's favourite number is {favourite_numbers['Kevin']}")

# A more concise approach:
for name, number in favourite_numbers.items():
    print(f"{name}'s favourite number is {number}")