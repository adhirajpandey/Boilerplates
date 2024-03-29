import os
from flask import Flask


def create_app():
    app = Flask(__name__, template_folder="templates")

    app.secret_key = os.urandom(12)

    app.debug = True    

    app.app_context().push()


    return app


app = create_app()


from application.controllers import *


if __name__ == '__main__':
    app.run()