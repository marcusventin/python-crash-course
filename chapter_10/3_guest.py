def get_name():
    name = input("Enter your name: ")
    filename = 'chapter_10/name.txt'
    with open(filename, 'w') as file_object:
        file_object.write(name)

get_name()