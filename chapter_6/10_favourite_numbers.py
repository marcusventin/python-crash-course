favourite_numbers = {
    'marcus' : [4, 8],
    'richard' : [1],
    'gavin' : [5, 58],
    'laura' : [12, 34, 100],
    'kevin' : [15],
    }


for name, numbers in favourite_numbers.items():
    if len(numbers) == 1:
        print(f"\n{name.title()}'s favourite number is:")
        print(f"{numbers[0]}")
    else:
        print(f"\n{name.title()}'s favourite numbers are:")
        for number in numbers:
            print(number)