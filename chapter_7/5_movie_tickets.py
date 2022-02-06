prompt = "\nEnter your age, and I'll tell you how "
prompt += "much your cinema ticket costs. Enter quit when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        price = 'nothing'
    elif age < 12:
        price = '£10'
    else:
        price = '£15'
    print(f"\nYour ticket will cost {price}.")

