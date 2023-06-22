import logging

from aiogram import Bot
from aiogram.types import Message

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)


class StartCommand:
    def __init__(self, bot: Bot):
        self._bot = bot

    async def execute(self, message: Message) -> None:
        logger.info(f'Received /start command from {message.chat.id}')
        await self._bot.send_message(
            message.chat.id,
            'Hello world! 🚀',
        )
