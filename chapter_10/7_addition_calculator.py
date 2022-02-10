def addition():
    print("This program adds two user-inputted numbers together.")
    
    first_pass = False
    while first_pass == False:
        first_entry = input("Enter your first number: ")
        try:
            first_num = float(first_entry)
            if first_num.is_integer():
                first_num = int(first_entry)
        except ValueError:
            print(f"'{first_entry}' isn't a number!")
        else:
            first_pass = True
            

    second_pass = False
    while second_pass == False:
        second_entry = input("Enter your second number: ")
        try:
            second_num = float(second_entry)
            if second_num.is_integer():
                second_num = int(second_entry)
        except ValueError:
            print(f"'{second_entry}' isn't a number!")
        else:
            second_pass = True

    if first_pass == True and second_pass == True:
        answer = first_num + second_num
        if type(answer) is float:
            if answer.is_integer():
                answer = int(answer)
        print(f"{first_num} + {second_num} = {answer}")
    else:
        print("Congratulations, you've broken the program.")

addition()