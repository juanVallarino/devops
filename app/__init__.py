from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    from config import config
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    
    from app.resources.ping_pong import PingPong
    from app.resources.blacklist import BlacklistResource, BlacklistEmailResource
    
    api = Api(app)
    api.add_resource(PingPong, '/ping')
    api.add_resource(BlacklistResource, '/blacklists')
    api.add_resource(BlacklistEmailResource, '/blacklists/<string:email>')
    
    return app
