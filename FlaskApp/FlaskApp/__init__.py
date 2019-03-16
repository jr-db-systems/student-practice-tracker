from flask import Flask
from flask import render_template, request
from flask_mysqldb import MySQL
#import yaml

app = Flask(__name__)

# Configure db
#db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = '167.99.225.139' #db['mysql_host']
app.config['MYSQL_USER'] = 'chepo' #db['mysql_user']
app.config['MYSQL_PASSWORD'] = 'jrsys' #db['mysql_password']
app.config['MYSQL_DB'] = 'studentpracticetracker' #db['mysql_db']

mysql = MySQL(app)

@app.route('/form', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        StudentDetails = request.form
        id_est  = StudentDetails['id']
        nombre  = StudentDetails['nombre']
        apellido  = StudentDetails['apellido']
        horas  = StudentDetails['horasAcumuladas']
        anio  = StudentDetails['anio']
        curso  = StudentDetails['curso']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO estudiante(id, nombre, apellido, horasAcumuladas, año, curso_codigoCurso) VALUES(%s, %s, %s, %s, %s, %s)",(id_est, nombre, apellido, horas, anio, curso))
        mysql.connection.commit()
        cur.close()
        return render_template('est_agregado.html')
    return render_template('form1.html')

@app.route('/estudiantes')
def users():
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM estudiante")
	if (resultValue > 0):
		StudentDetails = cur.fetchall()
		return render_template('users.html', StudentDetails=StudentDetails)
	else:
		return "DATABASE IS EMPTY: NO USERS FOUND"

@app.route("/Hello")
def hello():
    return "Hello, I love Digital Ocean!"

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/Test")
def the_html():
    return render_template('test1.html')

@app.route("/Test2")
def the_other_html():
    return render_template('test2.html')

@app.route("/remover", methods=['GET', 'POST'])
def remover_estudiante():
    if request.method == 'POST':
        StudentDetails = request.form
        id_est  = StudentDetails['id']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM estudiante WHERE id=%s", (id_est,))
        mysql.connection.commit()
        cur.close()
        return render_template('est_removido.html')
    return render_template("remover.html")

if __name__ == '__main__':
    app.run(debug=True)
