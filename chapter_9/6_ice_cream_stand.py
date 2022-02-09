class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['chocolate', 'strawberry', 'vanilla']
    
    def display_flavours(self):
        print(f"{self.restaurant_name.title()} is serving the following"
            " flavours:")
        for flavour in self.flavours:
            print(f"- {flavour.title()}")

cart = IceCreamStand("eye scream")
cart.display_flavours()