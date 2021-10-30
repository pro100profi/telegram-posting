from pyrogram import Client, filters
from config import *

app = Client('my_account', APP_ID, APP_HASH, phone_number=PHONE_NUMBER)

@app.on_message(filters.chat(PARSING_CHANNELS))
def send_message(client, message):
    condition_function = PARSING_CHANNELS_CONDITION.get(message.chat.username)
    if condition_function:
        condition_function(message)
    else:
        message.copy(MY_CHANNEL)

app.run()