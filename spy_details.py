from datetime import datetime


class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


spy = Spy('Bond', 'Mr.', 24, 4.7)

friend_one = Spy('Drake', 'Dr.', 37, 4.95)


friends = [friend_one]


class ChatMessage:

    def __init__(self, sender, message_sent_to, message, sent_by_me):
        self.name_of_sender = sender
        self.message_sent_to = message_sent_to
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
