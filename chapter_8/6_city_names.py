def city_country(city, country):
    statement = (f"{city.title()}, {country.title()}")
    return(statement)

one = city_country("brasilia", "brazil")
two = city_country("cardiff", "wales")
three = city_country("antananarivo", "madagascar")

print(one)
print(two)
print(three)