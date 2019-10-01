from flask import Flask
from redis import Redis
from logging import getLogger, INFO
from handlers import blueprint
import config


def create_app() -> Flask:
    app = Flask(__name__)

    logger = getLogger('Logger')
    logger.setLevel(INFO)

    if config.DB_HOST and config.DB_PORT:
        redis = Redis(host=config.DB_HOST, port=config.DB_PORT)
    else:
        return

    app.redis = redis
    app.logger = logger
    app.register_blueprint(blueprint)
    return app


if __name__ == '__main__':
    app = create_app()
    if config.APP_HOST and config.APP_PORT:
        app.run(host=config.APP_HOST, port=config.APP_PORT, debug=True)
