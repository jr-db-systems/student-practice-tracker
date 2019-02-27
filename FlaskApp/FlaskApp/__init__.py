from flask import Flask
from flask import render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
#db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = 'localhost' #db['mysql_host']
app.config['MYSQL_USER'] = 'root' #db['mysql_user']
app.config['MYSQL_PASSWORD'] = '' #db['mysql_password']
app.config['MYSQL_DB'] = 'flaskapp' #db['mysql_db']

mysql = MySQL(app)

@app.route('/Form', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('form1.html')

@app.route("/Hello")
def hello():
    return "Hello, I love Digital Ocean!"

@app.route("/")
def main():
    return "DROPLET FOR JR SYSTEMS CLASS PROJECT DEVELOPMENT"

@app.route("/Test")
def the_html():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
