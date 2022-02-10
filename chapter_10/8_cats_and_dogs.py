
def read_file(filename):
    try:
        with open(filename) as f:
            lines = f.read()
    except FileNotFoundError:
        print(f"Your file {filename} does not exist in this location.")
    else:
        print(lines)

read_file('chapter_10/cats.txt')
read_file('chapter_10/dogs.txt')