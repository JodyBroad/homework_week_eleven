# requirements.txt will have all the things you need to install to run your code

# import the flask object instance we just instantiated
from application import app


# main trick
if __name__ == "__main__":
    app.run(debug=True, port="4006")
