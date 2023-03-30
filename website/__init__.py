from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'

    from .views import views
    from .attendance import attendance

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(attendance, url_prefix='/attendance')

    return app


