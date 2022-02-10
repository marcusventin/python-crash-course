def guestbook():
    filename = 'chapter_10/guest_book.txt'

    while True:
        name = input("Add your name to the guestbook - enter 'quit' to quit: ")
        if name == "quit":
            return(False)
        else:
            with open(filename, 'a') as file_object:
                file_object.write(f"\n{name}")


guestbook()