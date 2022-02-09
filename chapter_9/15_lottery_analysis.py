from random import choice

def winning_ticket():
    winning_ticket = []
    
    lotto = (2, 34, 16, 14, 56, 13, 8, 29, 34, 40, 'F', 'X', 'Q', 'E', 'V')
    while len(winning_ticket) < 4:
        number = choice(lotto)
        if number not in winning_ticket:
            winning_ticket.append(number)
    
    return(winning_ticket)

def check_ticket(my_ticket, winning_ticket):
    for num in my_ticket:
        if num not in winning_ticket:
            return(False)


my_ticket = [14, 8, 'E', 13]
iterator = 0
while check_ticket(my_ticket, winning_ticket()) == False:
    iterator += 1

print(f"My ticket: {my_ticket}")
print(f"It took {iterator} tries before you won.")
