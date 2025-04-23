from flask import Flask
from flask_caching import Cache

cache = Cache()

def create_app():
    app = Flask(__name__)

    app.config['CACHE_TYPE'] = 'SimpleCache'
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300 

    cache.init_app(app)

    app.cache = cache

    from .routes import main
    app.register_blueprint(main)

    return app
