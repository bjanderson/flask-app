# Flask App

## Setup


### Clone the project

    git clone https://github.com/bjanderson/flask-app.git

### Open the project in VS Code

    code flask-app

In your terminal

    cd flask-app

### Create and activate the python virtual environment
In VS Code, open a new terminal in the flask-app folder.

First create a virtual environment

    python3 -m venv venv

Then activate that virtual environment

Mac/Linux

    source venv/bin/activate

Windows

    venv\Scripts\activate

### Install Flask
Now install flask with pip

    pip install flask
    pip install python-dotenv

## Run the App
You can run the app with:

    flask run

Once the app is running you can view it in the browser at
http://localhost:5000/

## Stop the app
You can stop the server by clicking in the terminal and pressing CTRL+C.

You can exit the virtual environment by running the deactivate command.

    deactivate

## References

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

https://www.youtube.com/watch?v=MwZwr5Tvyxo

REST API METHODS:  https://restfulapi.net/http-methods/

HTTP STATUS CODES: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
