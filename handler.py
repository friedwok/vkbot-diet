# handle_state: 0 - before diet; 1 - after diet; 2 - answer 'yes'; 3 - years; 4 - height; 5 - weight
# 6 - after answer 'lifestyle';

from random import randint
import messages
from mainfile import vk


def write_msg(user_id, random_id, message):
    vk.method('messages.send', {
        'user_id': user_id,
        'random_id': random_id,
        'message': message
    })


def get_random(ids: set):
    r = randint(0, 9999999999)
    if r not in ids:
        ids.add(r)
        return r
    else:
        get_random(ids)


def get_help_message(arguments):
    with open("helplist.txt", 'r') as f:
        if 'weather' not in arguments:
            data = f.readline()[:-1]
        else:
            data = f.read()

    return data


class Handler:
    identificators = set()

    def __init__(self, arguments_list):

        self.arguments = arguments_list
        self.handle_state = 0

    def handle(self, user_id, message_in):
        print(self.handle_state)
        msg = message_in.lower()

        if self.handle_state == 0:
            if msg == "привет":
                # write_msg(user_id, get_random(Handler.identificators), messages.message1)
                if not Handler.identificators:
                    write_msg(user_id, get_random(Handler.identificators), messages.message1)
                    write_msg(user_id, get_random(Handler.identificators), messages.message2)
            if msg == "помощь":
                write_msg(user_id, get_random(Handler.identificators), get_help_message(self.arguments))
            if msg == "диета":
                write_msg(user_id, get_random(Handler.identificators), messages.message4)
                write_msg(user_id, get_random(Handler.identificators), messages.message4_1)
                self.handle_state = 1
        elif self.handle_state == 1:
            if msg == "да":
                write_msg(user_id, get_random(Handler.identificators), messages.message5)
                self.handle_state = 2
            elif msg == "нет":
                self.handle_state = 0
        elif self.handle_state == 2:
            try:
                years = float(msg)
                if (years > 0) and (years < 100):
                    write_msg(user_id, get_random(Handler.identificators), messages.message6)
                    self.handle_state = 3
                else:
                    write_msg(user_id, get_random(Handler.identificators), "Значение должно быть целым от 0 до 100")
            except ValueError:
                write_msg(user_id, get_random(Handler.identificators), messages.message5_1)
            # доделать схему с цепочкой сообщений(переделать то, что снизу)
        elif self.handle_state == 3:
            try:
                height = float(msg)
                if (height > 0) and (height < 230):
                    write_msg(user_id, get_random(Handler.identificators), messages.message7)
                    self.handle_state = 4
                else:
                    write_msg(user_id, get_random(Handler.identificators), "Значение должно быть целым от 0 до 230")
            except ValueError:
                write_msg(user_id, get_random(Handler.identificators), messages.message5_1)
        elif self.handle_state == 4:
            try:
                weight = float(msg)
                if (weight > 0) and (weight < 250):
                    write_msg(user_id, get_random(Handler.identificators), messages.message8)
                    self.handle_state = 5
                else:
                    write_msg(user_id, get_random(Handler.identificators), "Значение должно быть целым от 0 до 250")
            except ValueError:
                write_msg(user_id, get_random(Handler.identificators), "Ответ должен быть простым числом")
        elif self.handle_state == 5:
            try:
                lifestyle = float(msg)
                if (lifestyle >= 1) and (lifestyle <= 5):
                    write_msg(user_id,
                              get_random(Handler.identificators),
                              "Вам рекомендовано подождать пока я допишу бота...")
                    self.handle_state = 0
                else:
                    write_msg(user_id, get_random(Handler.identificators), "От 0 до 5")
            except ValueError:
                pass
