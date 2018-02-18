from steganography.steganography import Steganography
from spy_detail import Spy, friends
from spy_detail import spy, ChatMessage
import csv
from termcolor import colored

print (colored("Let\'s get started", "cyan", attrs=["dark", "bold"]))
STATUS_MESSAGES = ['Available', 'Busy', 'Sleeping', 'At school']
chats = []


def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = list(csv.reader(friends_data))

        for row in reader[4:]:
            if row:
                name = row[0]
                age = row[2]
                rating = row[3]
                online = row[4]
                new_spy = Spy(name, age, rating, online)
                friends.append(new_spy)


def show_friends():
    if len(friends) == 0:
        print (colored("You have no friends !", "red", attrs=["dark", "bold"]))
        return 0

    for friend in friends:
        friend_details = friend.salutation + friend.name + " of age " + str(friend.age) + " with rating of " + str(
            friend.rating) + " is online! "
        blue_friend_details = colored(friend_details, "blue")
        print blue_friend_details


def load_chats():
    with open('chats.csv', 'rb') as chats_data:
        reader = list(csv.reader(chats_data))

        for row in reader[4:]:
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


def add_status(C_S_M):
    if C_S_M != None:
        print "your current status is " + C_S_M
    else:
        print "you don't have any status"

    user_choise = raw_input("do you want to select from old status? Y or N: ")

    if user_choise.upper() == 'Y':
        serial_no = 1
        for old_status in STATUS_MESSAGES:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no + 1

        user_status_selection = input("Which one do u want to set this time? ")
        new_status = STATUS_MESSAGES[user_status_selection - 1]

    elif user_choise.upper() == 'N':
        new_status = raw_input("write your status")
        STATUS_MESSAGES.append(new_status)
    else:
        print "invalid entry"
    return new_status


def add_friend():
    new_friend = Spy('', '', 0.0, 0)
    new_friend.name = raw_input("write your friend name: ")
    new_friend.salutation = raw_input("Mr. or Mrs.")
    new_friend.age = input("what's ur friend age :")
    new_friend.rating = input("write your friend rating :")

    if len(new_friend.name) > 2 and 50 >= new_friend.age >= 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow(
                [new_friend.name, new_friend.salutation, new_friend.rating, new_friend.age, new_friend.is_online])
    else:
        print "friend with these value can't be added"
    return len(friends)


def select_friend():
    serial_no = 1
    for friend in friends:
        print str(serial_no) + " " + friend.name
        serial_no = serial_no + 1
    user_selected_friend = int(raw_input("which one do u want to send message to ? "))
    user_index = user_selected_friend - 1
    return user_index


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


def read_message():
    chosen_friend = select_friend()
    output_path = raw_input("name of the image to be decoded:")
    secret_message = Steganography.decode(output_path)
    try:
        secret_message = Steganography.decode(output_path)
        print(colored("your secret message is:", "cyan"))
        print(colored(secret_message, "blue"))
        new_text = (secret_message.upper()).split()
        if 'SOS' in new_text or 'SAVE ME' in new_text or 'HELP ME' in new_text or 'ALERT' in new_text or 'RESCUE' in new_text or 'ACCIDENT' in new_text:
            print colored("!!!EMERGENCY MESSAGE DETECTED!!!", 'grey', ),
            print colored("The friend who sent this message needs your help!", "green")
            new_chat = ChatMessage(spy.name, friends[chosen_friend].name, secret_message, False)
            friends[chosen_friend].chats.append(new_chat)
        else:
            new_chat = ChatMessage(spy.name, friends[chosen_friend].name, secret_message, False)
            friends[chosen_friend].chats.append(new_chat)
    except TypeError:
        print colored("nothing to decode in image....\n Sorry! bhag yha se", 'red')


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


def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice = input(
            "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a message \n 4. Read a message \n 5.View chat history \n 0. Close application")
        if menu_choice == 1:
            updated_status_message = add_status(current_status_message)
            print "your new status is updated to" + updated_status_message
        elif menu_choice == 2:
            no_of_friend = add_friend()
            print "i have " + str(no_of_friend) + " friends"
        elif menu_choice == 3:
            send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice == 5:
            read_chat_history()
        elif menu_choice == 0:
            show_menu = False
        else:
            show_menu = False
            print "Invalid choice"


existing = raw_input("Continue as " + spy.salutation + " " + spy.name + "(Y/N)?")
if existing.upper() == "Y":
    # Continue with the default user/details imported from the helper file.
    print "Welcome %s %s age: %d Rating: %.1f Glad to have you back." % (spy.salutation, spy.name, spy.age, spy.rating)
    start_chat(spy.name, spy.age, spy.rating)

elif existing.upper() == "N":
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 3:
        print "welcome " + spy.name + " glad to meet you."
        spy_salutation = raw_input("what should i cal you ? mr. or ms. ")
        spy.name = spy_salutation + " " + spy.name
        print spy.name
        print "alright" + " " + " " + spy.name + " " + "i'd like to know a little more about u"
        spy.age = input("what is your age? ")
        if spy.age > 12 or spy.age < 50:
            print "spy, your age is perfect"
            spy.rating = input("what is your rating? ")
            if spy.rating >= 5.0:
                print "Great spy"
            elif spy.rating < 5.0 and spy.rating >= 4.5:
                print "nice spy"
            elif spy.rating < 4.5 and spy.rating >= 3.5:
                print "fine spy"
            else:
                print "fuck off"
            spy_is_online = True
            print "Authentication complete. Welcome  %s age: %d and rating of: %.1f Proud to have you onboard" % (
                spy.name, spy.age, spy.rating)



        else:
            print "your age is not valid to be a spy"
    else:
        print "please enter a valid name of atleast 4 letter"
else:
    print "invalid responce"
