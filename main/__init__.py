#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=13384432, cast=int)
API_HASH = config("API_HASH", default="ea9db4503ed7088b788e06dfd818e00e")
BOT_TOKEN = config("BOT_TOKEN", default="7397532645:AAH7R46hDIQ95j9-5kyVgySCa-A6cHQy6vE")
SESSION = config("SESSION", default="BQGPlygAI4BiNyrBdvwQZq0yotZUfdwMVAmeMl-x7w54XKZa4VrA1DZ6RBJk7ooZGXhh9AR6A9WLTEG61Cq9voBLqoAyGJqJMvudYb_jH3YH15z5X1KKGgkLHntgn_4u8JDQeN3-xNrz6ZHdR69NjGlWw-7DbwkfhFPnWKwP5VREi3R-74-6m3o3Pcyu1cSfZUD5Ve9R769-Gv2_93imHP3iyvNQ9CVtcHhVWjoavhWWF6xTLh3xEDbjqBjpZN9BoCK2aSnXKm7BBmwYsCjNsNe_0SpsEujeooQdAJH12XMv_s7RGrFWLf1X_asA35hZ6uM8Fo1-73tD-iMLfIScR0IaGynXKQAAAAGKe47tAA")
FORCESUB = config("FORCESUB", default="movies0x1")
AUTH = config("AUTH", default=6169288210, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
