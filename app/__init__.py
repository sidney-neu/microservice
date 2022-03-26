import os
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.modules.test.extensions import cache
from app.config.log_config import config_log
from app.route import app_route
# caching config
cacheConfig = {
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 5 * 60
}

def create_app():
    app = Flask(__name__)
    config_log()
    limiter = Limiter(
        app,
        key_func=get_remote_address,
        default_limits=["600000 per minute", "10000 per second"],
    )

    # env config
    #todo

    # register api's route
    app_route(app)

    return app
