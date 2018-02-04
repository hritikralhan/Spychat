from spy_details import spy_name,spy_age,spy_rating
print 'Hello!'
print 'Let\'s get started..'

def start_chat(spy_name,spy_age,spy_rating):
    show_menu = True
    while show_menu:
        menu_choice = input('What do you want to do? \n  1. Add a status \n  2. Add a friend \n  0. Exit \n')
        if menu_choice==1 :
            status = raw_input('Write your status:')
            print 'Your status is ' + status
        elif menu_choice==2:
            print 'Will add a friend'
        elif menu_choice==0:
            show_menu= False
        else:
            print 'Invalid choice'

question = raw_input('Are you a new user? Y or N: ')
if question.upper() == 'N':
    print 'We already have your details'
    start_chat(spy_name,spy_age,spy_rating)
elif question.upper() =='Y':

    spy_name =  raw_input('What is your name? ')
    if len(spy_name)> 3:
        print 'Welcome ' + spy_name + ' glad to meet you'
        spy_salutation = raw_input('What should i call you Mr or Miss or Mrs?')
        spy_name = spy_salutation + " " + spy_name
        print 'Alright' + " " + spy_name + " " + 'i would like to know little more about you before we proceed...'
        spy_age = 0
        spy_rating = 0.0
        spy_status_online = False
        spy_age = input('What is your age? ')

        if spy_age>10 and spy_age<50:
            print 'You age is perfect to be a spy.'
            spy_rating = input('What is rating of spy? ')

            if spy_rating>=5.0:
                print 'Great spy'
            elif spy_rating<5.0 and spy_rating>=4.5:
                print 'You are one of the good ones.'
            elif spy_rating<4.5 and spy_rating>=3.5:
                print'Fine spy'
            else:
                print 'Useless spy'

            spy_status_online = True
            print 'Authentication complete. Welcome ' + spy_name + ' age: ' +  str(spy_age) + ' and rating of: ' + str(spy_rating) + ' Proud to have you onboard'
            start_chat(spy_name, spy_age, spy_rating)

        else:
            print 'You age is not perfect to be a spy. '

    else:
        print 'Please enter valid name'
else:
    print 'Invalid Entry'
