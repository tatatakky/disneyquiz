from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage,ImageSendMessage
)
from random_select import random_image

app = Flask(__name__)

line_bot_api = LineBotApi('ezgPBB2UPeshx6guDRc1RfYTXFd37q1U49JcsrX6zFbYCBj4O7ee/TE2EucseV6ho8bPC9B41t8bFsnfCespYaogG7sSnFS8swWBQnDMSmHmfkG9SPMFgd2FiCNKsxOPKdFyilVCwPhPSL42lH320wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f6731cbde7b8c980107dc00a82303764')


@app.route("/")
def hello_world():
    return "hello world!"

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
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    url=random_image()
    if event.message.text is "pass":
        pass
    else:
        line_bot_api.reply_message(event.reply_token,
        ImageSendMessage(
        original_content_url=url,
        preview_image_url=url)
        )

if __name__ == "__main__":
    app.run()
