from data import jobs_api
from flask_login import LoginManager
from flask import Flask
from data import db_session


PATH_TO_DB = "../db/mars_explorer.db"


app = Flask(__name__)
login_manager = LoginManager(app)


def main():
    db_session.global_init(PATH_TO_DB)
    app.register_blueprint(jobs_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
