# Lucas Traynor
# CSCI-1060-02; 2/19/18


print('This program is used to make restaurant recommendations\n'
      'based on dietary restrictions.')


# create lists of restaurants and their dietary options
restaurant_list = ["Joe's Gourmet Burgers", "Main Street Pizza", "Corner Cafe", "Mama's Fine Italian",
                   "The Chef's Kitchen"]

vegetarian_list = ["Main Street Pizza", "Corner Cafe", "Mama's Fine Italian", "The Chef's Kitchen"]

vegan_list = ["Main Street Pizza", "The Chef's Kitchen"]

glutenfree_list = ["Joe's Gourmet Burgers", "Main Street Pizza", "Corner Cafe", "The Chef's Kitchen"]


# ask the user for the inputs
vegetarian = str(input('To start, is anyone in your party a vegetarian (yes or no)? '))

vegan = str(input('Is anyone in your party vegan (yes or no)? '))

gluten_free = str(input('Lastly, is anyone in your party Gluten-Free (yes or no)? '))


# reassign restaurant_list to results
results = restaurant_list


if vegetarian == 'yes':
    result = (set(results) and set(vegetarian_list))

if vegan == 'yes':
    result = (set(results) and set(vegan_list))

if gluten_free == 'yes':
    result = (set(results) and set(glutenfree_list))



print(results)

