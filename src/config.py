import logging

BACKEND = 'Slack'

CORE_PLUGINS = ('SlackFW', 'Help')

BOT_IDENTITY = {
    'token': '<Slack-Token>', # Change Token of your bot on Slack
}

BOT_DATA_DIR = r'./data'
BOT_EXTRA_PLUGIN_DIR = r'./plugins'

BOT_LOG_FILE = r'./errbot.log'
BOT_LOG_LEVEL = logging.INFO

BOT_ADMINS = ('@CHANGEME', ) # Change to Admin user
BOT_PREFIX = '!'
BOT_ALT_PREFIXES = ('@slack_bot_name', ) # Change to name of your slack bot

HIDE_RESTRICTED_COMMANDS = True

ACCESS_CONTROLS_DEFAULT = {
    'allowprivate': True,
    'allowrooms': ('#your_channel'),
}

ACCESS_CONTROLS = {
    'SlackFW:*': {'allowrooms': ('#your_channel')}, # Change to your channel on slack
}

# Telegram variables
tl_endpoint = 'https://api.telegram.org/bot{token}/sendMessage'
tl_token = '<telegram-token>' # Telegram Token
tl_chatid = '<telegram-chatid>' # Telegram Chat_id
