#Join @dev_gagan

from telethon.errors import FloodWaitError
from datetime import datetime as dt, timedelta
import asyncio
import sys
from pyrogram import Client
import asyncio
import uvloop
from pyrogram.errors import FloodWait
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config
import logging, time
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

uvloop.install()
MDB = "mongodb+srv://ludlux:ludlux@cluster0.dte8fqy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
API_ID = "25018366" #config("API_ID", default=None, cast=int)
API_HASH = "03194f91ff9af028447f66c0d62e7e77" #config("API_HASH", default=None)
BOT_TOKEN = "7471620307:AAHhWGZd8tcvg1M2_A5kJxWSGVEKz_QHuuw" #config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
FORCESUB = "veer_bots" #config("FORCESUB", default=None)
AUTH = "7333826463" #config("AUTH", default=None)
MONGODB = config("MONGODB", default=MDB)
OWN = 7333826463 # edit this
GROUP = -1002190460821 # edit this
OWNER_ID = int(config("OWNER_ID", default=OWN))
LOG_GROUP = int(config("LOG_GROUP", default=GROUP))

SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "ggnbot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    sys.exit(1)
