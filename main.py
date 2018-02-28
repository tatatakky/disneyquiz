from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction,StickerMessage
)
from random_select import random_image
from quiz import *

app = Flask(__name__)

line_bot_api = LineBotApi('**********')
handler = WebhookHandler('*********')

@app.route("/")
def hello_world():
    return "hello world!"

flag=0
@app.route("/callback", methods=['POST'])
def callback():
    global count
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
    global QData
    global flag
    flag+=1
    # print(count)
        # else:
    #     line_bot_api.reply_message(event.reply_token,
    #     ImageSendMessage(
    #     original_content_url=url,
    #     preview_image_url=url)
    #     )
    print(flag)
    if flag==1:
        QData=ChooseQustion()
        flag+=1
    else:
        pass
    print(flag)

    if event.message.text == "quiz":
        line_bot_api.reply_message(event.reply_token,
            TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url=QData[6],
                title="ミッキーからの質問",
                text=QData[0],
                actions=[
                    PostbackTemplateAction(
                        label="1." + QData[1],
                        text='Chose 1',
                        data='action=buy&itemid=1'
                        ),
                    PostbackTemplateAction(
                        label="2." + QData[2],
                        text='Chose 2',
                        data='action=buy&itemid=1'
                        ),
                    PostbackTemplateAction(
                        label="3." + QData[3],
                        text='Chose 3',
                        data='action=buy&itemid=1'
                        ),
                    PostbackTemplateAction(
                        label="4." + QData[4],
                        text='Chose 4',
                        data='action=buy&itemid=1'
                        ),
                    ]
                )
            )
        )
        flag+=1
    elif event.message.text == "Chose 1" or event.message.text == "Chose 2" or event.message.text == "Chose 3" or event.message.text == "Chose 4":
        if flag==4:
            line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text=Solve(event.message.text,QData[5]))
            )
        else:
            line_bot_api.reply_message(event.reply_token,
            TextSendMessage(text="押しすぎだよ、、")
            )
        flag=0
    else:
        if flag>=4:
            flag=2
        else:
            flag=0
        line_bot_api.reply_message(event.reply_token,
        TextSendMessage(text=event.message.text)
        )

if __name__ == "__main__":
    app.run()
