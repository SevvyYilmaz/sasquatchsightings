
from flask_app import app #basic import to run the file
from flask import Flask
from flask_mysqldb import MySQL
from flask_app.controllers import sightings, users  # Importing controllers/routes after MySQL configuration

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'  # MySQL server hostname
app.config['MYSQL_USER'] = 'your_username'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'Xavi123'  # MySQL password
app.config['MYSQL_DB'] = 'your_database'  # MySQL database name

mysql = MySQL(app)

# Importing controllers/routes after MySQL configuration
from flask_app.controllers import sightings, users

if __name__ == '__main__':
    app.run(debug=True)
