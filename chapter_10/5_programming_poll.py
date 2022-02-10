def programming_poll():
    filename = 'chapter_10/programming_reasons.txt'
    while True:
        reason = input("Why do you like programming?"
            " Enter 'I've run out of reasons' when"
            " you can't come up with any more. ")
        if reason == "I've run out of reasons":
            return False
        else:
            with open(filename, 'a') as file_object:
                file_object.write(f"{reason}\n")

programming_poll()