from flask import Flask,request
import requests
from pymessenger import Bot

app = Flask(__name__)

VERIFY_TOKEN = 'Zigberman Chat Bot'
PAGE_ACCESS_TOKEN = 'EAAReyHs7ORsBACqnwEQ7RHcZBVQh7QcezuZBCfdaWYtVOARu7VZCxJamG1pfkcDbP0LHYEtcIMm9urZBFxP3xZBR48jZBi2M5ZBa3IfwNbXfRs7FNZBuoAr2GYhuSz4MrKfTkbJJ37uQZBMKT8c62qU8VZBZAfI4paHZCaJaLuobV9Kf0jsRM4ZAsZCPRw'
bot = Bot(PAGE_ACCESS_TOKEN)

def handling_message(text):
    adjusted_msg = text
    if adjusted_msg == 'hi' or adjusted_msg == 'Hi':
        response = "Hello"

    elif adjusted_msg == "what's up" or adjusted_msg == "What's up":
        response = "I'm great"

    else:
        response = "It's pleasure to chat with you today, Thank you."

    return response

@app.route('/', methods=["POST", "GET"])

def web_hook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            return request.args.get('hub.challenge')

        else:
            return 'Unable to connect to FaceBook'

    elif request.method == 'POST':
        data = request.json
        process = data['entry'][0]['messaging']
        for msg in process:
            text = msg['message']['text']
            sender_id = msg['sender']['id']
            response = handling_message(text)
            bot.send_text_message(sender_id, response)
        
        return 'message_posted'

    else:
        return ok

if __name__ == '__main__':
    app.run()