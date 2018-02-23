# Importing steganography library for encoding and decoding messages
from steganography.steganography import Steganography

# Importing the default spy objects
from spy_details import spy, friends

# Import the classes
from spy_details import Spy, ChatMessage

# Importing csv files
import csv

# Importing termcolor library for providing colors to different type of text
from termcolor import colored

# Welcome message to the user
print (colored("Hello Let\'s get started ", "cyan", attrs=["dark", "bold"]))

# list for old status messages
status_message = ['coding', 'eating', 'sleeping', 'repeating']

chats = []


# defining a function for loading existing friends when application starts
def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = list(csv.reader(friends_data))

        for row in reader[1:]:
            if row:
                name = row[0]
                age = row[1]
                rating = row[2]
                online = row[3]
                new_spy = Spy(name, age, rating, online)
                friends.append(new_spy)


# defining a function to show existing friends
def show_friends():
    if len(friends) == 0:
        print (colored("You have no friends !", "red", attrs=["dark", "bold"]))
        return 0

    for friend in friends:
        # Printing details of friend
        friend_details = friend.salutation + friend.name + " of age " + str(friend.age) + " with rating of " + str(friend.rating) + " is online! "
        blue_friend_details = colored(friend_details, "blue")
        print blue_friend_details                     # To print details in blue colour


# defining a function for loading chats history between user and a friend when application starts
def load_chats():
    with open('chats.csv', 'rb') as chats_data:
        reader = list(csv.reader(chats_data))

        for row in reader[1:]:
            if row:
                name_of_sender = row[0]
                message_sent_to = row[1]
                text = row[2]
                sent_by_me = row[4]
                new_chat = ChatMessage(name_of_sender, message_sent_to, text, sent_by_me)
                chats.append(new_chat)


print(colored("\nShowing details of existing friend", "yellow", attrs=["dark", "bold"]))

# loading existing friend details
load_friends()
# showing existing friend details
show_friends()
# loading chat history between user and friends
load_chats()


# defining a function for adding status
def add_status(c_s_m):
    # checking if any old status exists or not
    if c_s_m is not None:
        print "Your current status message is " + c_s_m + "\n"
    else:
        print "You don't have any current status"

    status_choice = raw_input("Do you want to add from old status (Y/N)?")

    # Checking whether user has entered anything or not
    if len(status_choice) >= 1:
        # If user selects to add from old status
        if status_choice.upper() == 'Y':
            serial_no = 1
            # showing old status to select from
            for old_status in status_message:
                print str(serial_no) + ". " + old_status
                serial_no = serial_no + 1
            user_status_selection = input("Which one do you want to choose ")
            new_status = status_message[user_status_selection - 1]

        # if user wants to add a new status
        elif status_choice.upper() == 'N':
            new_status = raw_input("write your status")
            # saving the new status
            status_message.append(new_status)
        else:
            print "invalid entry"
    return new_status


# defining a function to add a new friend
def add_friend():
    # using class for new spy details
    new_friend = Spy('', '', 0.0, 0)
    new_friend.name = raw_input("what's your friend name?")
    new_friend.salutation = raw_input("Mr. or Ms.")
    new_friend.age = input("what's your friend age")
    new_friend.rating = input("what's your friend rating")
    # checking eligibility of the new friend
    if len(new_friend.name) > 0 and 50 >= new_friend.age >= 12 and new_friend.rating >= 4.5:
        # saving new friend details
        friends.append(new_friend)
        # writing the details of new friend in csv file
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name, new_friend.salutation, new_friend.rating, new_friend.age, new_friend.is_online])
    else:
        # If new spy details did't meet minimum requirements
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends)


# Defining a function to select a friend from given friends
def select_friend():
    item_number = 0
    # Showing list of existing friends
    for friend in friends:
        print str(item_number + 1) + " " + friend.name
        item_number = item_number + 1
    user_selected_friend = int(raw_input("which friend you wanna select?"))
    user_index = user_selected_friend - 1
    # returning the index of selected friend
    return user_index


# defining a function to send a secret message by encoding
def send_message():
    # select a friend to send secret message to
    selected_friend = select_friend()
    message = raw_input("Write the secret message")
    # asking the user to input an image
    original_image = raw_input("name of image with which you want to encode secret message(with extension)")
    # setting the name of encoded image
    output_path = "output.png"
    # encoding secret_message and image using steganography
    Steganography.encode(original_image, output_path, message)
    message_sent_to = friends[selected_friend].name
    new_chat = ChatMessage(spy.name, message_sent_to, message, True)
    # append the message in chats
    friends[selected_friend].chats.append(new_chat)
    with open('chats.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([spy.name, message_sent_to, new_chat.message, new_chat.time, new_chat.sent_by_me])


# defining a function to read a secret message from a friend
def read_message():
    chosen_friend = select_friend()
    # asking the user for the image to be decoded
    output_path = raw_input("Name of the image you want to decoded the message from(with extension)")
    secret_message = Steganography.decode(output_path)
    try:
        # Using decode() function with file name of encrypted message as parameter
        secret_message = Steganography.decode(output_path)
        print (colored("Your secret message is:", "cyan"))
        print (colored(secret_message, "blue"))

        # Converting secret_text to uppercase and splitting
        new_text = (secret_message.upper()).split()

        # Checking emergency templates for help
        if 'SOS' in new_text or 'SAVE ME'in new_text or 'HELP ME' in new_text or 'ALERT' in new_text or 'RESCUE' in new_text or 'ACCIDENT' in new_text:

            # Emergency alert
            print colored("!!!EMERGENCY MESSAGE DETECTED!!!", 'grey', ),
            print colored("The friend who sent this message needs your help!", "green")

            # Creating new chat
            new_chat = ChatMessage(spy.name, friends[chosen_friend].name, secret_message, False)
            # Appending to chats
            friends[chosen_friend].chats.append(new_chat)

        # If there are no emergency messages
        else:
            new_chat = ChatMessage(spy.name, friends[chosen_friend].name, secret_message, False)
            # Appending
            friends[chosen_friend].chats.append(new_chat)

            print colored("Your secret message has been saved.\n", 'cyan')

    # No message found exception
    except TypeError:
        print colored("Nothing to decode from the image...\n Sorry! There is no secret message", 'red')


def read_chat_history():
    friend_choice = select_friend()

    print '\n'

    for chat in chats:
        if chat.sent_by_me and chat.message_sent_to == friends[friend_choice].name:
            # Date and time is printed in blue
            print (colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", "blue")),
            # The message is printed in red
            print (colored("You : ", "red")),
            # Default black colour for text
            print str(chat.message)
            print '\n'
            break

        # Message sent by another spy
        elif chat.sent_by_me is False:
            # Date and time is printed in blue
            print (colored(str(chat.time.strftime("%d %B %Y %A %H:%M")) + ",", "blue")),
            # The message is printed in red
            print (colored(str(friends[friend_choice].name) + " : ", "red")),
            # Default black colour for text
            print str(chat.message)
            break

    else:
        print (colored("You don't have any chats with this friend", "yellow", attrs=["dark", "bold"]))
        print '\n'


# declaring a function to give different choices to the user
def start_chat():

    current_status_message = None
    show_menu = True
    # asking for the users choice
    while show_menu:
        menu_choice = input("What do you want to do?"
                            "\n 1. Add a status  "
                            "\n 2. Add a friend "
                            "\n 3. Send a secret message " 
                            "\n 4. read a secret message "
                            "\n 5. View chat history"
                            "\n 0. Close application")
        # to add a status
        if menu_choice == 1:
            updated_status_message = add_status(current_status_message)
            print "Your updated status message is: " + updated_status_message
            current_status_message = updated_status_message
        # to add a friend
        elif menu_choice == 2:
            number_of_friends = add_friend()
            print "Total friends: " + str(number_of_friends)
        # to send a secret message
        elif menu_choice == 3:
            send_message()
        # to read a secret message
        elif menu_choice == 4:
            read_message()
        # to read chat history
        elif menu_choice == 5:
            read_chat_history()
        # to exit from application
        elif menu_choice == 0:
            show_menu = False
        else:
            print "Invalid choice"


print '\n'                 # providing space between consecutive lines


# Asking the user to continue as an existing user
existing = raw_input(colored("Continue as " + spy.salutation + " " + spy.name + "(Y/N)?", "green"))

# If user wants to continue as an existing user
if existing.upper() == "Y":
    # Continue with the default user/details imported from the helper file.
    print (colored("Welcome %s %s Glad to have you back." % (spy.salutation, spy.name), "yellow", attrs=["dark", "bold"]))
    print '\n'
    start_chat()

# If user don't wants to continue as an existing user
elif existing.upper() == "N":
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

# Validate the length of spy name to be at least 3 words
    if len(spy.name) >= 3:
            print "welcome " + spy.name + " Glad to meet you"
            spy.salutation = raw_input("what should i call you? Mr. or Ms. ")
            spy.name = spy.salutation + " " + spy.name
            print "Alright " + spy.name + ". I'd like to know a little bit more about you before we proceed..."

            spy.age = input("What is your age?")
            # checking if the spy is of the right age
            if 12 < spy.age < 50:
                print "Well, You are at right age for this"
                spy.rating = input("what is your rating?")

                # different comments according to the spy rating
                if spy.rating >= 4.5:
                    print "Great Ace!"
                elif 3.5 < spy.rating < 4.5:
                    print "You are one of the good ones"
                elif 2.5 < spy.rating < 3.5:
                    print "You have to try to do better"
                else:
                    print "you can always ask someone for help"

                spy.is_online = True
                # displaying the welcome message
                print "Authentication complete. Welcome %s age: %d and rating of: %.1f Proud to have you onboard" \
                      % (spy.name, spy.age, spy.rating)
                # calling the start chat function
                start_chat()
            else:
                # if new user did'nt match our qualifications
                print "Sorry, you are not a match"

    else:
            print "Name must be of atleast 3 characters"

else:
    print "Invalid response"
