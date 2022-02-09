from multiple_modules_user import User
from multiple_modules import Admin, Privileges

moomin = Admin('moo', 'min', 70, 90)

moomin.privileges.show_privileges()