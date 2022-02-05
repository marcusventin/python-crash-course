glossary = {
    'operator' : '+, -, *, /, **',
    'list comprehension' : 
        '[x ** 2 if x % 2 == 0 for x in list] - make copies of lists',
    'tuples' : 'an immutable list typically denoted using () rather than []',
    'set' : 'a list of unique items, stored in {}'
    }

for keyword, definition in glossary.items():
    print(f"\n{keyword}: {definition}")