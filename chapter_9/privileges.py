class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 
            'can make sticky posts']
        
    def show_privileges(self):
        print("This user has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.capitalize()}")