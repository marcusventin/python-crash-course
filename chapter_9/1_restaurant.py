class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves"
            f" {self.cuisine_type.title()} food.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")

restaurant = Restaurant("vitos", "italian")

restaurant.describe_restaurant()
restaurant.open_restaurant()