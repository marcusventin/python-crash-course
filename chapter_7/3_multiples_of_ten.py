prompt = "Enter a number, and I'll tell you "
prompt += "whether it's a multiple of 10: "

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is divisible by ten!")
else:
    print(f"\nThe number {number} is not divisible by ten!")