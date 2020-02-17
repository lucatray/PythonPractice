

print('------------------------------------')


add_another_user = str(input('Would you like to add a user (yes or no)? '))


while add_another_user != 'no':

    student_name = str(input('Name: '))
    section = str(input('Section: '))
    height = float(input('Height: '))
    number_of_classes = int(input('Number of Classes: '))

    list = [student_name, section, height, number_of_classes]

    print('Name: ', list[0].lower(), sep='')
    print('Section: ', list[1], sep='')
    print('Height: ', list[2], sep='')
    print('Number of Classes: ', list[3], sep='')


    add_another_user = str(input('Would you like to add another user (yes or no)? ').lower())


print('------------------------------------')

animal_list = ['cat', 'dog', 'horse', 'fish']

animal_list.append('Cow')

print(animal_list)

print(animal_list[1:4])

print(animal_list[-4])


# negative numbers start counting from the back of the list
num_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(num_list[-4])
print(num_list[-5])
print(num_list[4])

# prints length of the list
print(len(animal_list))



print('------------------------------------')


# list electronics

# create list with different data types (heterogeneous lists)
# python lists are also mutable

electronics = ['TV', 2, 'Phone', 'Phone', 'Phone', 'Keyboard', 'Mouse', 5.67]

electronics[2] = 'mobile phone'

print(electronics)


# tuples use parenthesis instead of brackets. Tuples make lists immutable and cannot be changed or altered
technology_products = ('Tv', 'Phone', 'Xbox', 'ps4')

print(technology_products)



# the '.count()' command will count the number of specific elements in a list
print(electronics.count('Phone'))


# list numbers
numbers = [3, 5, 8, 22, 33, 22, 65]

print((numbers))


# 2-dimentional lists

