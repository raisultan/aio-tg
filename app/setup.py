import asyncio

from aiogram import Bot, Dispatcher
from aiohttp.web import Application

from app.commands.start import StartCommand


async def start_polling(app: Application) -> None:
    app['polling_task'] = asyncio.create_task(app['dispatcher'].start_polling())


async def stop_polling(app: Application) -> None:
    app['polling_task'].cancel()
    try:
        await app['polling_task']
    except asyncio.CancelledError:
        pass
    await app['dispatcher'].wait_closed()


async def bot(app: Application):
    app['bot'] = Bot(token=app['config']['bot_token'])
    yield
    await app['bot'].close()


async def dispatcher(app: Application):
    app['dispatcher'] = Dispatcher(app['bot'])


async def commands(app: Application):
    start = StartCommand(app['bot'])

    app['dispatcher'].register_message_handler(
        start.execute,
        commands=['start'],
    )
