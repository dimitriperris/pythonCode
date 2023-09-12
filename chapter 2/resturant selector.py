restaurants = {
    "Joe's Gourmet Burgers": {"Vegetarian": "No", "Vegan": "No", "Gluten-Free": "No"},
    "Main Street Pizza Company": {"Vegetarian": "Yes", "Vegan": "No", "Gluten-Free": "Yes"},
    "Corner Café": {"Vegetarian": "Yes", "Vegan": "Yes", "Gluten-Free": "Yes"},
    "Mama's Fine Italian": {"Vegetarian": "Yes", "Vegan": "No", "Gluten-Free": "No"},
    "The Chef's Kitchen": {"Vegetarian": "Yes", "Vegan": "Yes", "Gluten-Free": "Yes"}
}

vegetarian = input('Is anyone in your party a vegetarian? (yes/no) ').lower()
vegan = input('Is anyone in your party a vegan? (yes/no) ').lower()
gluten_free = input('Is anyone in your party gluten-free? (yes/no) ').lower()

valid_restaurants = []

for restaurant, restrictions in restaurants.items():
    if (vegetarian == 'yes' and restrictions['Vegetarian'] == 'Yes') or \
       (vegan == 'yes' and restrictions['Vegan'] == 'Yes') or \
       (gluten_free == 'yes' and restrictions['Gluten-Free'] == 'Yes'):
        valid_restaurants.append(restaurant)

print('Here are your restaurant choices:')
for restaurant in valid_restaurants:
    print(restaurant)

