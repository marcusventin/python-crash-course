usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, here are the latest updates.")
        else:
            print(f"Hello {username}, it's good to see you again.")
else:
    print("We need to find some users!")