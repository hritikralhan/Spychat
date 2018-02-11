from spy_details import spy
print 'Hello!'
print 'Let\'s get started..'

STATUS_MESSAGES = ['Available','Busy','Sleeping','Typing','At School']
friends = [{'name' : 'Deep', 'age': 20,'rating':5.8,'is online':True  },{'name' : 'Kavish', 'age': 19,'rating':4.5,'is online':True  }]



def add_status(C_S_M):
    if C_S_M !=None:
        print 'Your current status is' + C_S_M
    else:
        print "You don't have status currently"

    user_choice = raw_input("Do you want to select from old status? Y or N : ")
    if user_choice.upper() == 'Y':
        serial_no = 1
        for old_status in STATUS_MESSAGES:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no +1
        user_status_selection = input('Which one do you want to set this time?')
        new_status = STATUS_MESSAGES[user_status_selection-1]

    elif user_choice.upper() == 'N':
         new_status = raw_input('Write your status: ')
         STATUS_MESSAGES.append(new_status)

    else:
        print 'Invalid Entry'
    return new_status


def add_friend():
    frnd = {
        'name': ' ',
        'age': 0,
        'rating': 0.0,
        'is_online': True
    }
    frnd['name'] = raw_input("Write your frnd's name: ")
    frnd_sal = raw_input('Mr or Miss: ')
    frnd['name'] = frnd_sal  + " "  + frnd['name']
    frnd['age'] = input('Write the age of your frnd: ')
    frnd['rating'] = input('Write the rating of frnd: ')

    if len(frnd['name'])>=2 and 50>frnd['age']>=12 and frnd['rating'] >= spy['rating']:
        friends.append(frnd)

    else:
        print "Friend with these values cannot be added "
    return len(friends)




def start_chat(spy_name,spy_age,spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice = input('What do you want to do? \n  1. Add a status \n  2. Add a friend \n  0. Exit \n')
        if menu_choice==1 :
            updated_status_message = add_status(current_status_message)
            print 'Your new status is updated to '+ updated_status_message
        elif menu_choice==2:
            no_of_frnds = add_friend()
            print  "I have " +  str(no_of_frnds) + " friends."
        elif menu_choice==0:
            show_menu= False
        else:
            print 'Invalid choice'

question = raw_input('Are you a new user? Y or N: ')
if question.upper() == 'N':
    print 'We already have your details'
    start_chat(spy['name'],spy['age'],spy['rating'])
elif question.upper() =='Y':
    spy = {
        'name':'' ,
        'age':0 ,
        'rating':0.0 ,
        'is_online': True
    }

    spy['name'] =  raw_input('What is your name? ')
    if len(spy['name'])> 3:
        print 'Welcome ' + spy['name'] + ' glad to meet you'
        spy_salutation = raw_input('What should i call you Mr or Miss or Mrs?')
        spy['name'] = spy_salutation + " " + spy['name']
        print 'Alright' + " " + spy['name'] + " " + 'i would like to know little more about you before we proceed...'


        spy['age'] = input('What is your age? ')

        if spy['name']>12 and spy['name']<50:
            print 'You age is perfect to be a spy.'
            spy['rating'] = input('What is rating of spy? ')

            if spy['rating']>=5.0:
                print 'Great spy'
            elif spy['rating']<5.0 and spy['rating']>=4.5:
                print 'You are one of the good ones.'
            elif spy['rating']<4.5 and spy['rating']>=3.5:
                print'Fine spy'
            else:
                print 'Useless spy'

            spy_status_online = True
            print 'Authentication complete. Welcome ' + spy['name'] + ' age: ' +  str(spy['age']) + ' and rating of: ' + str(spy['rating'] + ' Proud to have you onboard'
            start_chat(spy['name'], spy['age'], spy['rating'])

        else:
            print 'You age is not perfect to be a spy. '

    else:
        print 'Please enter valid name'
else:
    print 'Invalid Entry'
