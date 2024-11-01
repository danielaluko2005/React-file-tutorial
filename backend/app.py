from flask import Flask
from flask_sqlalchemy import SQLAlchemy #sqlalchemy is a relational mapping database 
from flask_cors import CORS

app=Flask(__name__) #create an instace of Flask and if i add __name__== main it makes this script only execute directly and not when imported.

CORS(app)
# app.config: This is a dictionary-like object in Flask where you can set configuration variables for the application.
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///friends.db" #This specific configuration key tells SQLAlchemy which database to connect to.# "sqlite:///friends.db": This is the database URI. It specifies that SQLAlchemy should use SQLite and create/use a database file named friends.db in the current directory. The format for SQLite database URIs is sqlite:///path_to_db, where path_to_db is the relative or absolute path to the database file.

app.config["SQLALACHEMY_TRACK_MODIFICATIONS"]=False #disables the modification tracking feature of SQLAlchemy. 
    
db=SQLAlchemy(app)


import routes

with app.app_context():
    db.create_all()


if __name__=="__main__":
    app.run(debug=True)  #This method starts the Flask web server.It's typically called at the end of a Flask application to begin serving HTTP requests.
    # debug=True: This argument enables Flask's debug mode.
    # When debug=True, the Flask application will:
    # Reload Automatically: The server will automatically restart if it detects any changes in the source code