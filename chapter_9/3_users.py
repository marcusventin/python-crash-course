class User():
    def __init__(self, first_name, last_name, heightcm, age):
        self.first_name = first_name
        self.last_name = last_name
        self.heightcm = heightcm
        self.age = age
    
    def describe(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is" 
            f" {self.age} years old and {self.heightcm}cm tall")
    
    def greet(self):
        print(f"Hello, {self.first_name.title()}!")

user = User('sancho', 'panza', 150, 35)

user.describe()
user.greet()