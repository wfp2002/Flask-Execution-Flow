from flask import Flask
from random import randint


app = Flask(__name__)


@app.before_first_request
def before_first_request_func():

    """ 
    This function will run once before the first request to this instance of the application.
    You may want to use this function to create any databases/tables required for your app.
    """

    print("This function will run once ")


@app.before_request
def before_request_func():

    """ 
    This function will run before every request. Let's add something to the session & g.
    It's a good place for things like establishing database connections, retrieving
    user information from the session, assigning values to the flask g object etc..
    We have access to the request context.
    """
    print("before_request is running!")


@app.route("/")
def index():

    """ 
    A simple route that gets a session value added by the before_request function,
    the g.username and returns a string.
    Uncommenting `raise ValueError` will throw an error but the teardown_request
    funtion will still run.
    """

    print("index is running!")
    return "Hello world"


@app.after_request
def after_request_func(response):

    """ 
    This function will run after a request, as long as no exceptions occur.
    It must take and return the same parameter - an instance of response_class.
    This is a good place to do some application cleanup.
    """

    print("after_request is running!")
    return response


@app.teardown_request
def teardown_request_func(error=None):

    """ 
    This function will run after a request, regardless if an exception occurs or not.
    It's a good place to do some cleanup, such as closing any database connections.
    If an exception is raised, it will be passed to the function.
    You should so everything in your power to ensure this function does not fail, so
    liberal use of try/except blocks is recommended.
    """

    print("teardown_request is running!")
    if error:
        # Log the error
        print(str(error))


if __name__ == "__main__":
    app.run(port = 8081, host = '127.0.0.1', threaded = True)