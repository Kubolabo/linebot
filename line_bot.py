# -*- coding: utf-8 -*-
"""Line_bot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T_8upgOtu5jv1A40OAp7EBL3jYXM8keh
"""


from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage
import pya3rt


app=Flask(__name__)


linebot_api = LineBotApi("SbIgxa9YVIfTqccMpa+60yVmAH9PQaL7182qqghO6o7iLpGxf0Z/03SCCb1hfz1oot7ocCE3qj4kjOHrRWaVDqAOSBnrxzFmcpvoPsRrG8xqgC/BYc5WCR5UrXdE0AxigvVCGFI+AHfy8yToAulPRAdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("e5ccc9fb005cd00922a52fbd1de83eac")
@app.route("/callback",methods=['POST'])
def callback():
  signature = request.headers["X-Line-Signature"]
  body = request.get_data(as_text=True)

  try:
    handler.handle(body,signature)
  except InvalidSignatureError:
    abort(400)
  
  return 'OK'

@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
  ai_message =talk_ai(event.message.text)
  linebot_api.reply_message(event.reply_token,TextSendMessage(text=ai_message))

def talk_ai(word):
  apikey="DZZzRAqeZZKKeA0zy6H7whiahaEF0rb7"
  client=pya3rt.TalkClient(apikey)
  reply_message=client.talk(word) 
  return reply_message["results"][0]["reply"]

if __name__ =='__main__':
  app.run()