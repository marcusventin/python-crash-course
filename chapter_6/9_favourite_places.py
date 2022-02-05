favourite_places = {
    'marcus' : ['durham', 'london', 'manchester'],
    'cris' : ['spain', 'portugal', 'italy'],
    'nigel' : ['romania', 'poland', 'bulgaria'],
    }

for name, places in favourite_places.items():
    print(f"\n{name.title()}'s favourite places are:")
    for place in places:
        print(f"{place.title()}")