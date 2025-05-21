import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 14050586))
API_HASH = getenv("API_HASH", "42a60d9c657b106370c79bb0a8ac560c")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7772470067:AAGXddFFPdqRt5TEAkzGvZMfZNc8_zHrXaY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://riyu:riyu@cluster0.kduyo99.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 9999))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002411662634))

# Get this value from @MissRose_bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7306823475))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
API_KEY = getenv("API_KEY", None) # youtube song api key, get it from https://t.me/RahulTC

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/StormBeatz/AudifyMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/GrayBots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GrayBotSupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGuxbEANAgL72Q43GMmsvpJkeL6Ese3tFapt9EAxbamXF01dnWtl06-bx8Vfa7LoEYsH6HJOadYxF-tB6XSkHYTA-YU0Dl7LJ1Joc1JppbEozmfmSBkUFLgn0Xd8qZJiyk24ZDHW_5yx9ysB6EWUnMv9lIOcEkWVNstlcNLDVANvmU-vOhEvJfK9gkW-rABfsbs8pKat6UloezX-2nSvxcj8AHPkATgPQ2dtcTemD4Xd8gBpvsMeoozBOFWhT0r6YFbRbqoKhnjyvwwkkpRhvAasjw3Dv6vTI6OcGClKJV-j2hq4Ki8AYvzJTVCeCUcSwYKyoyZqxqO_LKVe-Gmgiw5NULyQQAAAAGuANNkAA")
STRING2 = getenv("STRING_SESSIONN2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/7a5bdfcf40189ea450ed0-c1fd755b77e93c2d7a.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org//file/389a372e8ae039320ca6c.png"
)
PLAYLIST_IMG_URL = "https://graph.org/file/40581c7048b1ee71209a2-3fc027862ecf64213d.jpg"
STATS_IMG_URL = "https://graph.org/file/cf84606db2e13b5cb19cc-2b375f36e4dcec4055.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/40581c7048b1ee71209a2-3fc027862ecf64213d.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/40581c7048b1ee71209a2-3fc027862ecf64213d.jpg"
STREAM_IMG_URL = "https://graph.org/file/40581c7048b1ee71209a2-3fc027862ecf64213d.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/40581c7048b1ee71209a2-3fc027862ecf64213d.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/40581c7048b1ee71209a2-3fc027862ecf64213d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/40581c7048b1ee71209a2-3fc027862ecf64213d.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/40581c7048b1ee71209a2-3fc027862ecf64213d.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/40581c7048b1ee71209a2-3fc027862ecf64213d.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
