import requests
from config import tl_endpoint, tl_token, tl_chatid

def sendMsgTelegram(msg):
    resq = requests.post(tl_endpoint.format(token=tl_token), \
                        data={'chat_id': tl_chatid, \
                            'text': msg}).json()
    print (resq)


