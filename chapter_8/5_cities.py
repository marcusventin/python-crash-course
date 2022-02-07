def describe_city(city, country = "Italy"):
    print(f"\n{city.title()} is in {country.title()}.")

describe_city("florence")
describe_city("paris", "france")
describe_city(country = "Spain", city = "Barcelona")
