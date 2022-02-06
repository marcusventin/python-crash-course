prompt = "\nEnter your age, and I'll tell you how much your cinema ticket costs: "

age = ''
while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            price = 'nothing'
        elif age < 12:
            price = '£10'
        else:
            price = '£15'
        print(f"\nYour ticket will cost {price}.")

