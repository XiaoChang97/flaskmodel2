from flask import Flask
from setting import Dvelopment
from exit import db
from apps.user.user_view import blueprint_us
def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config.from_object(Dvelopment)
    db.init_app(app)
    app.register_blueprint(blueprint_us)
    #print(app.url_map)
    return app