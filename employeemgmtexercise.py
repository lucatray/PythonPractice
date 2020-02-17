
# create a list for part time and full time employees
full_time_employees = ['John Jackson', 'Debra Walters', 'Jason Peters', 'Laura Holly', 'Jack Johnson']

part_time_employees = ['Kalie Straight', 'Holly Right', 'Eric Landers', 'Cory Count']

# create the main fuction
def main():

#prompt user to add an employee
    add_new = str(input('Would you like to add a new employee '
                        'to the system (yes or no): '))
# create a loop
    while add_new == 'yes':

        hours_working = str(input('Is this new employee working Full-Time'
                              ' or Part-Time: ').lower())

        full_name = str(input('Please enter the name of the new employee: '))

        if hours_working == 'full time':

            full_time_employees.append(full_name)

        elif hours_working == 'part time':

            part_time_employees.append(full_name)



        add_new = str(input('Would you like to add another employee '
                        'to the system(yes or no): '))

        print('Current Employees: ')

        for i in part_time_employees + full_time_employees:
            print(i)

        print()
        print()


        removing_employees()



def removing_employees():

    remove_employee = str(input('Do any previous employees need to be removed from '
                            'the system: '))

    if remove_employee == 'yes':

        name_of_former = str(input('What is the name of this former employee: '))

        system_names = full_time_employees + part_time_employees

        system_names.remove(name_of_former)

        print()

        print('Current Employees: ')

        for i in part_time_employees + full_time_employees:
            print(i)




main()
