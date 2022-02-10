import json

def get_favourite_number():
    filename = 'chapter_10/favourite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        number = input("What's your favourite number? ")
        with open(filename, 'w') as f:
            json.dump(number, f)
    else:
        read_favourite_number()

def read_favourite_number():
    filename = 'chapter_10/favourite_number.json'
    with open(filename) as f:
        number = json.load(f)
    print(f"I know your favourite number - it's {number}!")

get_favourite_number()