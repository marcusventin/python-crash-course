from random import choice

lotto = (2, 34, 16, 14, 56, 13, 8, 29, 34, 40, 'F', 'X', 'Q', 'E', 'V')

first_value = choice(lotto)
second_value = choice(lotto)
third_value = choice(lotto)
fourth_value = choice(lotto)

print(f"The results are in. Any ticket with the following characters is"
    f" a winner: {first_value} {second_value} {third_value} {fourth_value}.")