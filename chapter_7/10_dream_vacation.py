data = {}

active = True

while active == True:
    name = input("\nEnter your name: ")
    dream = input(f"\n{name}, where is your dream holiday destination? ")
    data[name] = dream

    repeat = input("\nWould someone else like to complete our poll? (y/n) ")
    if repeat == 'n':
        active = False

print("\nThe poll has now closed. Here are the results:")
for name, dream in data.items():
    print(f"{name}'s dream destination is {dream}.")
