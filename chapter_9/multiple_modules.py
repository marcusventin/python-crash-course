from multiple_modules_user import User

class Admin(User):
    def __init__(self, first_name, last_name, heightcm, age):
        super().__init__(first_name, last_name, heightcm, age)
        self.privileges = Privileges()

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 
            'can make sticky posts']
        
    def show_privileges(self):
        print("This user has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.capitalize()}")