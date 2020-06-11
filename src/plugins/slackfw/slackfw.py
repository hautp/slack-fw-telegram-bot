import re
from errbot import BotPlugin, botcmd
from modules.common import sendMsgTelegram

class SlackFW(BotPlugin):
    """
    This plugin to help us forward any message (like ticket or invoice) from Slack channel to Telegram
    """

    def callback_message(self, mess):
        if mess.is_group is True:
            # Case 1: message is text format and does not start with ! character
            if mess.body and not mess.body.startswith("!"):
                msg = mess.body
            elif mess.extras['attachments']:
                body = mess.extras['attachments'][0]['text']
                # Case 2.1: attachments include fields
                if mess.extras['attachments'][0]['fields']:
                    desc = ""
                    fields = mess.extras['attachments'][0]['fields']
                    for field in fields:
                        sub_title = field['title']
                        sub_value = re.sub('[<>]', '', field['value']).split("|")[0]
                        desc += """- %(sub_title)s %(sub_value)s
""" % {'sub_title': sub_title, 'sub_value': sub_value} 
                    msg = """%(body)s

Descriptions: 
%(desc)s""" % {'body': body, 'desc': desc}
                # Case 2.2: attachments do not include fields
                else:
                    msg = "%(body)s" % {'body': body}
            # Push message to Telegram
            sendMsgTelegram(msg)
