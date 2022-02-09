class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves"
            f" {self.cuisine_type.title()} food.")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("vitos", "italian")

print(restaurant.number_served)

restaurant.set_number_served(10)
print(restaurant.number_served)

restaurant.increment_number_served(20)
print(restaurant.number_served)