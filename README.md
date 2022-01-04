# Flask App

## Setup


### Clone the project

    git clone https://github.com/bjanderson/flask-app.git

### Open the project in VS Code

    code flask-app

### Create and activate the python virtual environment
In VS Code, open a new terminal in the flask-app folder.

First create a virtual environment

    python3 -m venv venv

Then activate that virtual environment

Max/Linux

    source venv/bin/activate

Windows

    venv\Scripts\activate

### Install Flask
Now install flask with pip

    pip install flask
    pip install python-dotenv

## Run the App

If you did not install python-dotenv, make sure to export an environment variable to tell flask where to find the app entry file. If you did install python-dotenv, it does this for you.

Only run the export/set commands if you didn't install python-dotenv.

Mac/Linux

    export FLASK_APP=flask-app.py

Windows

    set FLASK_APP=flask-app.py


Now you can run the app with:

    flask run

Your app can now be viewed from the browser at
http://localhost:5000/

## Stop the app
You can stop the server by pressing clicking in the terminal and pressing CTRL+CY.

You can exit the virtual environment by running the deactivate command.

    deactivate

## References

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
