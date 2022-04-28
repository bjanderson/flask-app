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

## Git Pull
In your terminal

    git status
    git add -A
    git commit -m "commit message"
    git checkout master
    git pull
    git checkout -b edits

## Git login

https://stackoverflow.com/a/68921750

Go to your Github Settings -> Developer Settings -> Personal Access Tokens page in GitHub (https://github.com/settings/tokens/new), and generate a new Token with all Repo permissions

Search Keychain Access in your mac -> search for github.com -> click Show password then paste the token you just copied.

Go to the CLI, it will ask again for username and password, enter your Github username and paste the token as password, and you should be good to go for the rest of the times you are using the CLI.

## References

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

https://www.youtube.com/watch?v=MwZwr5Tvyxo

REST API METHODS:  https://restfulapi.net/http-methods/

HTTP STATUS CODES: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
