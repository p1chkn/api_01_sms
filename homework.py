import time
import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv


def get_status(user_id):
    load_dotenv()
    token = os.getenv('token_vk')
    url = 'https://api.vk.com/method/users.get'
    params = {
        'user_ids': user_id,
        'v': '5.92',
        'access_token': token,
        'fields': 'online'

    }
    r = requests.post(url=url, params=params)
    return r.json()['response'][0]['online']


def sms_sender(sms_text):
    load_dotenv()
    token = os.getenv('token_twilio')
    sid = os.getenv('sid_twilio')
    number_to = os.getenv('number_to')
    number_from = os.getenv('number_from')
    client = Client(sid, token)
    message = client.messages.create(
        body=sms_text,
        from_=number_from,
        to=number_to
    )

    return message.sid


if __name__ == "__main__":

    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
