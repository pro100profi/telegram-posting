from env import *

MY_CHANNEL = 'FoodPorn'
PARSING_CHANNELS = [
    'my_poster_channel',
    'eda2021',
]

def eda2021(message):
    if 'Real Food | ' in str(message.caption):
        message.caption = message.caption.replace('Real Food | ', '')
        message.caption_entities = None
        message.copy(MY_CHANNEL)

def my_poster_channel(message):
    forward_chat = message.forward_from_chat
    if not forward_chat:
        return
    forward_username = forward_chat.username
    if forward_username == 'eda2021':
        eda2021(message)

PARSING_CHANNELS_CONDITION = {
    'eda2021': eda2021,
    'my_poster_channel': my_poster_channel
}