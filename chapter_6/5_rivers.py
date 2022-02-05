rivers = {
    'thames' : 'london',
    'wear' : 'durham',
    'tyne' : 'newcastle',
    }

for river, city in rivers.items():
    print(f"\nThe {river.title()} runs through {city.title()}.")

for river in rivers.keys():
    print(f"This is a river: {river.title()}")

for city in rivers.values():
    print(f"This is a city: {city.title()}")