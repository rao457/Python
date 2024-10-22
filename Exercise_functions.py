def city_country(city, country):
    """ It takes a city and country name and format it nicely"""
    formatted = f"{city}, {country}"
    return formatted.title()
city = input("Enter the name of your city: ")
country = input("Enter the name of your country: ")
location = city_country(city, country)
print(location)