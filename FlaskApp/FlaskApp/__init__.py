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

@app.route("/")
def main():
    return render_template('HomePage.html')

############# Esudiantes #############

@app.route("/ManejarEstudiantes")
def ManejarEstudiantes():
    return render_template('GUI_Manejar_Estudiantes.html')

'''
# intento de hacer un search
@app.route('/buscarestudiante', methods=['GET', 'POST'])
def buscarEstudiante():
    if request.method == 'POST':
        StudentDetails = request.form
        id_est  = StudentDetails['id']

        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM estudiante WHERE id=%s", (id_est))
        if (resultValue > 0)
            StudentDetails = cur.fetchall()
            return render_template('Mostrar_Estudiantes.html', StudentDetails=StudentDetails)
        #mysql.connection.commit()
        #cur.close()
    return render_template("BuscarEstudiante.html")
'''
@app.route('/MostrarEstudiantes')
def users():
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM estudiante")
	if (resultValue > 0):
		StudentDetails = cur.fetchall()
		return render_template('Mostrar_Estudiantes.html', StudentDetails=StudentDetails)
	else:
		return "DATABASE IS EMPTY: NO USERS FOUND"

@app.route('/actualizarestudiante')
def actualizarHome():
    return render_template('ActualizarEstudianteMenu.html')

@app.route('/actualizarestudiantehoras', methods=['GET', 'POST'])
def actualizar_estudiante():
    if request.method == 'POST':
        StudentDetails = request.form
        id_est  = StudentDetails['id']
        horas = StudentDetails['horas']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE estudiante SET horasAcumuladas = %s WHERE id=%s", (horas, id_est))
        mysql.connection.commit()
        cur.close()
        return render_template('Estudiante_Actualizado.html')
    return render_template("ActualizarEstudianteHoras.html")

@app.route('/actualizarestudiantecurso', methods=['GET', 'POST'])
def actualizar_estudiante_curso():
    if request.method == 'POST':
        StudentDetails = request.form
        id_est  = StudentDetails['id']
        curso = StudentDetails['curso_codigoCurso']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE estudiante SET curso_codigoCurso = %s WHERE id=%s", (curso, id_est))
        mysql.connection.commit()
        cur.close()
        return render_template('Estudiante_Actualizado.html')
    return render_template("ActualizarEstudianteCurso.html")

@app.route('/actualizarestudianteanio', methods=['GET', 'POST'])
def actualizar_estudiante_anio():
    if request.method == 'POST':
        StudentDetails = request.form
        id_est  = StudentDetails['id']
        anio = StudentDetails['anio']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE estudiante SET año = %s WHERE id=%s", (anio, id_est))
        mysql.connection.commit()
        cur.close()
        return render_template('Estudiante_Actualizado.html')
    return render_template("ActualizarEstudianteAnio.html")


@app.route('/AgregarEstudiante', methods=['GET', 'POST'])
def AgregarEstudiante():
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
        return render_template('Estudiante_Agregado.html')
    return render_template('AgregarEstudiante.html')

@app.route("/RemoverEstudiante", methods=['GET', 'POST'])
def remover_estudiante():
    if request.method == 'POST':
        StudentDetails = request.form
        id_est  = StudentDetails['id']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM estudiante WHERE id=%s", (id_est,))
        mysql.connection.commit()
        cur.close()
        return render_template('Estudiante_Removido.html')
    return render_template("RemoverEstudiante.html")

############# Maestros #############

@app.route("/ManejarMaestros")
def ManejarMaestros():
    return render_template('GUI_Manejar_Maestros.html')

@app.route('/actualizarmaestro')
def actualizar_maestro_home():
    return render_template('ActualizarMaestroMenu.html')

@app.route('/actualizarmaestrocurso', methods=['GET', 'POST'])
def actualizar_maestro_curso():
    if request.method == 'POST':
        TeacherDetails = request.form
        id_maest  = TeacherDetails['id']
        curso = TeacherDetails['curso_codigoCurso']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE maestro SET curso_codigoCurso = %s WHERE id=%s", (curso, id_maest))
        mysql.connection.commit()
        cur.close()
        return render_template('Maestro_Actualizado.html')
    return render_template("ActualizarMaestroCurso.html")

@app.route('/MostrarMaestros')
def maestros():
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM maestro")
	if (resultValue > 0):
		TeacherDetails = cur.fetchall()
		return render_template('Mostrar_Maestros.html', TeacherDetails=TeacherDetails)
	else:
		return "DATABASE IS EMPTY: NO USERS FOUND"

@app.route('/AgregarMaestro', methods=['GET', 'POST'])
def index1():
    if request.method == 'POST':
        # Fetch form data
        TeacherDetails = request.form
        id_maest  = TeacherDetails['id']
        nombre  = TeacherDetails['nombre']
        apellido  = TeacherDetails['apellido']
        especializacion  = TeacherDetails['especializacion']
        curso  = TeacherDetails['curso']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO maestro(id, nombre, apellido, especialización, curso_codigoCurso) VALUES(%s, %s, %s, %s, %s)",(id_maest, nombre, apellido, especializacion, curso))
        mysql.connection.commit()
        cur.close()
        return render_template('Maestro_Agregado.html')
    return render_template('AgregarMaestro.html')

@app.route("/RemoverMaestro", methods=['GET', 'POST'])
def remover_maestro():
    if request.method == 'POST':
        TeacherDetails = request.form
        id_maest  = TeacherDetails['id']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM maestro WHERE id=%s", (id_maest,))
        mysql.connection.commit()
        cur.close()
        return render_template('Maestro_Removido.html')
    return render_template("RemoverMaestro.html")

############# Cursos #############

@app.route('/cursos')
def curso():
	cur = mysql.connection.cursor()
	resultValue = cur.execute("SELECT * FROM curso")
	if (resultValue > 0):
		CourseDetails = cur.fetchall()
		return render_template('Cursos.html', CourseDetails=CourseDetails)
	else:
		return "DATABASE IS EMPTY: NO COURSES FOUND"

@app.route('/actualizarcurso', methods=['GET', 'POST'])
def actualizar_curso():
    if request.method == 'POST':
        CourseDetails = request.form
        id_curso  = CourseDetails['codigoCurso']
        curso = CourseDetails['nombre']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE curso SET nombre = %s WHERE codigoCurso=%s", (curso, id_curso))
        mysql.connection.commit()
        cur.close()
        return render_template('Curso_Actualizado.html')
    return render_template("ActualizarCurso.html")

@app.route('/agregarcurso', methods=['GET', 'POST'])
def agregar_curso():
    if request.method == 'POST':
        # Fetch form data
        CourseDetails = request.form
        id_curso  = CourseDetails['codigoCurso']
        curso  = CourseDetails['nombre']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO curso(codigoCurso, nombre) VALUES(%s, %s)",(id_curso, curso))
        mysql.connection.commit()
        cur.close()
        return render_template('Curso_Agregado.html')
    return render_template('AgregarCurso.html')

@app.route("/removercurso", methods=['GET', 'POST'])
def remover_curso():
    if request.method == 'POST':
        CourseDetails = request.form
        id_curso  = CourseDetails['codigoCurso']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM curso WHERE codigoCurso=%s", (id_curso,))
        mysql.connection.commit()
        cur.close()
        return render_template('Curso_Removido.html')
    return render_template("RemoverCurso.html")

@app.route("/Test")
def the_html():
    return render_template('test1.html')

'''
@app.route("/Hello")
def hello():
    return "Hello, I love Digital Ocean!"

@app.route("/Test2")
def the_other_html():
    return render_template('test2.html')

@app.route("/rerouting")
def rerouting():
    return render_template('redirecting_test.html')
'''

if __name__ == '__main__':
    app.run(debug=True)
