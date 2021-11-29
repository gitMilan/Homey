import os
from flask import Flask
from flask import render_template, blueprints
from flask import jsonify
from flask import Response, stream_with_context
from os import environ
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from qbittorrent import Client





def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    app.config['threaded'] = True

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    from flaskr.esp import esp
    app.register_blueprint(esp.bp)


    from flaskr.torrent import torrent
    app.register_blueprint(torrent.bp)


    return app