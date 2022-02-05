dapple = {
    'name' : 'dapple',
    'species' : 'donkey',
    'owner' : 'sancho panza',
    }

rosinante = {
    'name' : 'rosinante',
    'species': 'horse',
    'owner' : 'don quixote',
    }

richard_parker = {
    'name' : 'richard parker',
    'species' : 'tiger',
    'owner' : 'pi',
    }

pets = [dapple, rosinante, richard_parker]

for pet in pets:
    print(f"\nKey information about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")