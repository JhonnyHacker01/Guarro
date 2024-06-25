from flask import Flask, render_template, request
from clases.conexion import Conexion

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hola mundo"

@app.route("/usuario/registrar")
def usuario_registrar():
    return render_template("registroUsuario.html")

@app.route("/usuario/guardar", methods=["POST"])
def usuario_guardar():
    email = request.form["email"]
    password = request.form["password"]
    username = request.form["username"]
    nombres = request.form["nombres"]
    apellidos = request.form["apellidos"]
    tipo = request.form["tipo"]
    id_escuela = request.form["id_escuela"]

    conexion = Conexion()
    conextion_local = conexion.obtener_conexion()
    with conextion_local.cursor() as cursor:
        cursor.execute('INSERT INTO `usuario` (`email`, `password`, `nombres`, `apellidos`, `tipo`, `id_escuela`, `password`) VALUES (%s, %s)')
    conextion_local.close()


    return f"usuario: {email}"

@app.route("/usuario/mostrar")
def usuario_mostrar():
    usuarios = []
    conexion = Conexion()
    conextion_local = conexion.obtener_conexion()
    with conextion_local.cursor() as cursor:
        cursor.execute('SELECT * FROM usuario')
        usuarios = cursor.fetchall()
    conextion_local.close()
    return render_template("mostrarUsuario.html", usuarios=usuarios)
