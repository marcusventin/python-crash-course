from imported_admin import User, Admin, Privileges

badman = Admin('bad', 'man', 300, 250)

badman.privileges.show_privileges()