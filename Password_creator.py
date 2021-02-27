#imports
import random

#functions
def pass_creator():
    #this func ask you to create the password.
    character = '1234567890-=!@#$%^&*_+qwertyuiopasdfghjkl><mnbvcxz'
    number_of_pass = int(input('Enter number of password you want to create:'))
    length = int(input('Enter length of your pass:'))
    for _ps in range(number_of_pass):
        password = ''
        for _pwd in range(length):
            password += random.choice(character)
        print(password)
    again()


def again():
    #This func ask you to try again.
    pass_again = input('Do you want to create the password again? enter <y> for yes and <n> for no:')
    if pass_again == 'y':
        pass_creator()
    elif pass_again == 'n':
        print('Goodby my friend')
    else:
        again()

pass_creator()
