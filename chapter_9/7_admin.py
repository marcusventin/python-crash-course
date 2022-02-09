from privileges import Privileges

class User():
    def __init__(self, first_name, last_name, heightcm, age):
        self.first_name = first_name
        self.last_name = last_name
        self.heightcm = heightcm
        self.age = age

class Admin(User):
    def __init__(self, first_name, last_name, heightcm, age):
        super().__init__(first_name, last_name, heightcm, age)
        self.privileges = Privileges()
    
    # def show_privileges(self):
    #     print(f"{self.first_name.title()} {self.last_name.title()} has the"
    #         " following privileges:")
    #     for privilege in self.privileges.privileges:
    #         print(f"- {privilege.capitalize()}")

badmin = Admin('bad', 'min', 160, 36)

badmin.privileges.show_privileges()