import time
import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TOKEN_VK = os.getenv('TOKEN_VK')
TOKEN_TWILIO = os.getenv('TOKEN_TWILIO')
SID_TWILIO = os.getenv('SID_TWILIO')
NUMBER_FROM = os.getenv('NUMBER_FROM')
NUMBER_TO = os.getenv('NUMBER_TO')


def get_status(user_id):

    url = 'https://api.vk.com/method/users.get'
    params = {
        'user_ids': user_id,
        'v': '5.92',
        'access_token': TOKEN_VK,
        'fields': 'online'
    }
    r = requests.post(url=url, params=params)
    return r.json()['response'][0]['online']


def sms_sender(sms_text):

    client = Client(SID_TWILIO, TOKEN_TWILIO)
    message = client.messages.create(
        body=sms_text,
        from_=NUMBER_FROM,
        to=NUMBER_TO
    )

    return message.sid


if __name__ == "__main__":

    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
