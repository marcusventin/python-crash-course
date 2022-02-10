import json

def get_stored_username():
    filename = 'chapter_10/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'chapter_10/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return(username)

def greet_user():
    username = get_stored_username()
    if username:
        answer = input(f"Are you {username}? ")
        if answer == 'yes':
            print(f"Welcome back, {username}")
        if answer == 'no':
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()