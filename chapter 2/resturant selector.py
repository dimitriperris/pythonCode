# Get dietary preferences from the user
vegetarian = input("Is anyone in your party a vegetarian? ")
vegan = input("Is anyone in your party a vegan? ")
gluten_free = input("Is anyone in your party gluten-free? ")

# Define the restaurant options
restaurants = {
    "Joe's Gourmet Burgers": {"vegetarian": "no", "vegan": "no", "gluten_free": "no"},
    "Main Street Pizza Company": {"vegetarian": "yes", "vegan": "no", "gluten_free": "yes"},
    "Corner Café": {"vegetarian": "yes", "vegan": "yes", "gluten_free": "yes"},
    "Mama's Fine Italian": {"vegetarian": "yes", "vegan": "no", "gluten_free": "no"},
    "The Chef's Kitchen": {"vegetarian": "yes", "vegan": "yes", "gluten_free": "yes"}
}

# Create a list to store suitable restaurants
suitable_restaurants = []

# Check dietary preferences and add suitable restaurants to the list
for restaurant, restrictions in restaurants.items():
    if (vegetarian == "yes" or restrictions["vegetarian"] == "yes") and \
       (vegan == "yes" or restrictions["vegan"] == "yes") and \
       (gluten_free == "yes" or restrictions["gluten_free"] == "yes"):
        suitable_restaurants.append(restaurant)

# Display suitable restaurant choices
if suitable_restaurants:
    print("Here are your restaurant choices:")
    for restaurant in suitable_restaurants:
        print(restaurant)
else:
    print("Sorry, there are no suitable restaurants for your party's dietary preferences.")
