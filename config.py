from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/7c9c1831099058beca9e9.png")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/0f9612b2f385dcd9dbc5e.png")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/worstpartyinc")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/hero4in")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://telegra.ph/file/0f9612b2f385dcd9dbc5e.png"
