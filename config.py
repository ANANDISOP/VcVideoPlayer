import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SOURCE_CODE = getenv("SOURCE_CODE")
OWNER_NAME = getenv("OWNER_NAME", "MR_X_OP_BOLTE")
ALIVE_NAME = getenv("ALIVE_NAME", "VideoPlayer")
BOT_USERNAME = getenv("BOT_USERNAME", "X_VIDEO_PLAYER_BOT)
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "X_VIDEO_PLAYER)
SUPPORT_GROUP = getenv("GROUP_SUPPORT", "INDIAN_NETWORK_OP")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "JANEMAN_UPDATE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/2e300f892c3a240f3fd40.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "190"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/934c5374a6dd495aa5c56.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/934c5374a6dd495aa5c56.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/934c5374a6dd495aa5c56.jpg")
