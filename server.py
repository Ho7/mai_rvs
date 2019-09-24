from flask import Flask
from redis import Redis
from logging import getLogger, INFO
from handlers import blueprint


def create_app() -> Flask:
    app = Flask(__name__)

    redis = Redis(host='redis', port=6379, db=0)

    logger = getLogger('Logger')
    logger.setLevel(INFO)

    app.redis = redis
    app.logger = logger
    app.register_blueprint(blueprint)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)
