from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


application = Flask(__name__)

# default limit for each route
limiter = Limiter(
    application,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@application.route('/')
def index():
    """Homepage"""
    return "Hello"



if __name__ == '__main__':
    application.run(port=5000, debug=True)