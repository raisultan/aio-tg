from aiohttp import web

from app import setup
from app.config import load_config
from app.routes import setup_routes


def init_app(config: dict) -> web.Application:
    app = web.Application()
    app['config'] = config

    on_startup = [
        setup.dispatcher,
        setup.commands,
        setup_routes,
        setup.start_polling,
    ]
    client_context = [
        setup.bot,
    ]
    app.cleanup_ctx.extend(client_context)
    app.on_startup.extend(on_startup)
    app.on_shutdown.extend([setup.stop_polling])

    return app


def start() -> None:
    config = load_config()
    app = init_app(config)

    web.run_app(app, port=8080, access_log=None)


if __name__ == '__main__':
    start()
