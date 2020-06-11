# slack-fw-telegram-bot

I'm using module https://hostbillapp.com/feature/slack-notifications/ to push event (ticket or invoice) from Hostbill to Slack channel. But I also want to push this event to Telegram. 
Therefore, I write a simple Slackbot (using `errbot` framework) to create a Slack bot forward any message (type text or attachments) from Slack channel to Telegram.
## Run Slack bot as daemon on VPS

- Install requirement packages

```bash
pip install errbot && pip install errbot[slack] 
```

- Edit some variables in config file of `errbot`

```bash
vim src/config.py
```

```
BOT_IDENTITY = {
    'token': '<Slack-Token>', # Change Token of your bot on Slack
}

...

BOT_ADMINS = ('@CHANGEME', ) # Change to Admin user
BOT_PREFIX = '!'
BOT_ALT_PREFIXES = ('@slack_bot_name', ) # Change to name of your slack bot

...

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
```

- Start bot on daemon mode

```bash
errbot -d
```

## Using Docker
- Firstly, edit `config.py` like above step

- Secondly, build docker image from source code

```bash
docker build -t slackfw-bot .
```

- Finannly, run container by `docker` or `docker-compose` command

```bash
docker run --name slackfw-bot -d slackfw-bot
```

```bash
docker-compose up -d
```
