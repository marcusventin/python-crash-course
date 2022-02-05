favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

people = ['marcus', 'nigel', 'edward', 'fiona', 'jessica', 'phil']

for name in people:
    if name in favourite_languages.keys():
        print(f"{name.title()}, thank you for taking our poll.")
    else:
        print(f"{name.title()}, please consider taking our poll.")