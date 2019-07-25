import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import handler
import argparse
import sys


# API-key
# HERE SHOULD BE YOUR TOKEN!!!
token = ""

# authorization as community

vk = vk_api.VkApi(token=token)

# working with messages
longpoll = VkLongPoll(vk)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--weather", action="store_true", help="weather display function")
    args = parser.parse_args()

    arg_list = []
    if args.weather:
        arg_list.append("weather")
    handler_object = handler.Handler(arg_list)

    try:
        for event in longpoll.listen():
            # new message income
            if event.type == VkEventType.MESSAGE_NEW:
                # if this has mark for me(for bot)
                if event.to_me:
                    # message from user
                    request = event.text
                    print(request)
                    handler_object.handle(event.user_id, request)
    except KeyboardInterrupt:
        print("Goodbye...")
        sys.exit()


if __name__ == "__main__":
    main()
