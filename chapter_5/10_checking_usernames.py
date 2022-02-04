current_users = ["test_User", "fiRst", "aLso_first", "me_toO", "Honk"]
new_users = ["also_fiRst", "hoNk", "generic_uSername", "not_fifth", "fifth"]

low_case = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in low_case:
        print(f"The username '{new_user}' has already been registered.")
    else:
        print(f"The username '{new_user}' is available.")