
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from linebot import LineBotApi, WebhookHandler, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, ImageSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parse = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parse.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        for event in events:
            if isinstance(event, MessageEvent):
                message = None
                text = event.message.text
                print(text)

                if text == '1':
                    message = '早安'
                elif text == '2':
                    message = '午安'
                elif text == '3':
                    message = '晚安'
                elif '早安' in text:
                    message = '早安你好！'
                elif '捷運' in text:
                    mrts = {
                        '台北': 'https://web.metro.taipei/pages/assets/images/routemap2023n.png',
                        '台中': 'https://upload.wikimedia.org/wikipedia/commons/f/f4/%E5%8F%B0%E4%B8%AD%E6%8D%B7%E9%81%8B%E8%B7%AF%E7%B7%9A%E5%9C%96_%282020.01%29.png',
                        '高雄': 'https://upload.wikimedia.org/wikipedia/commons/5/56/%E9%AB%98%E9%9B%84%E6%8D%B7%E9%81%8B%E8%B7%AF%E7%B6%B2%E5%9C%96_%282020%29.png'
                    }
                    image_url = 'https://web.metro.taipei/pages/assets/images/routemap2023n.png'  # 預設值

                    for mrt in mrts:
                        print(mrt)
                        if mrt in text:
                            image_url = mrts[mrt]
                            print(image_url)
                            break

                else:
                    message = '抱歉！我不知道你在說什麼'

                if message is None:
                    message_obj = ImageSendMessage(image_url, image_url)
                else:
                    message_obj = TextSendMessage(text=message)

                line_bot_api.reply_message(
                    event.reply_token, message_obj)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()


def index(request):
    return HttpResponse('Line Bot')
