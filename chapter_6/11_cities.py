cities = {
    'durham' : {
        'country' : 'united kingdom',
        'population' : 50_000,
        'fact' : 'It has a beautiful cathedral.',
        },
    'rome' : {
        'country' : 'italy',
        'population' : 2_900_000,
        'fact' : 'The Roman Forum is a must-see!',
        },
    'paris' : {
        'country' : 'france',
        'population' : 2_100_000,
        'fact' : 'Also known as the city of love.'
        },
    }

for city, data in cities.items():
    print(f"\n{city.title()}:")
    for key, value in data.items():
        if key == 'country':
            print(f"{key.title()}: {value.title()}")
        else:
            print(f"{key.title()}: {value}")