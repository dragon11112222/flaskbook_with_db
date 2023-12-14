from flask import Flask

def create_app():
    app = Flask(__name__)  ## 플라스크 인스턴스(객체) 생성

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix = '/crud')

    return app