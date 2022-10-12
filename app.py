# Web app development

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('UEB2uR3LWhIJANTxa2LJk2aqnxe9ubuBwXPJ4zWtqHdI+cpHGoteZAZ5rETqHnAWkYer6MWKxW6H2gkGp7JPBUkCBagSeaeYsV+j2qnefN5SAVIp3yJcSPnZ2FFBTtZrexVSm8cJNrHMW0kcqx0LOwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0182a70eaf48c6f2b42dd9d1cf37944d')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    reply = "I can't understand you, please reply another message."
    
    if msg == 'Hi' or msg == 'hi':
        reply = 'Hi'
    elif msg == 'How is your day':
        reply = 'It is wonderful, and yop?'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply))


if __name__ == "__main__":
    app.run()