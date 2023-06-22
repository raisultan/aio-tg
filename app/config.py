import os

from dotenv import load_dotenv

load_dotenv()


def load_config() -> dict:
    return {
        'bot_token': os.environ['BOT_TOKEN'],
    }
