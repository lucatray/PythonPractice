# Lucas Traynor
# CSCI 1060-02, 4/8/2018
# This program is used to calculate monthly interest rate
# for the user.

# create a main function
def main():

# set parameter for while loop
    another = 'yes'

    print('This program is used to calculate your '
          'monthly interest rate.')

    while another == 'yes':


# prompt user to enter necessary inputs
        present_value = float(input('To start, please enter the present value '
                                'of your account: '))

        interest_rate = float(input('Please enter your monthly interest rate: '))

        time_duration = int(input('Please enter the number of months the money will be'
                              ' left in this account: '))

        futurevalue(present_value, interest_rate, time_duration)

        another = str(input('Would you like to calculate another set of values'
                            ' (yes or no): ').lower())



# create function to process the entered information
def futurevalue(argument1, argument2, argument3):


        future_value = argument1 * (1 + argument2) ** argument3

        print('The future balance in this account will be: $',
              format(future_value, ',.2f'), sep='')


# call the main function
main()



