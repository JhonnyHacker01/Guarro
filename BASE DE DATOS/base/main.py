from flask import Flask, render_template, request
from clases.conexion import Conexion
app =Flask(__name__)

@app.route("/")
def hola_mundo():
    return "hola mundo "

@app.route("/usuario/registrar")
def usuario_registrar():
   return render_template("registroUsuario.html")

@app.route("/usuario/guardar", methods=["POST"])
def usuario_guardar():
    username = request.form["username"]
    password = request.form["password"]
    nombres = request.form["nombres"]
    apellidos = request.form["apellidos"]
    tipo = request.form["tipo"]
    id_escuela=1
    conexion = Conexion
    conexion_local = conexion.obtener_conexion()
    with conexion_local.cursor() as cursor:
        cursor.execute("SELECT * FROM usuario(username, password, nombres, apellidos, tipo, id_escuela) VALUES (%s,%s,%s,%s,%s,%s)"
                      (username, password, nombres, apellidos, tipo. id_escuela))
        
        conexion_local.comit()
        conexion_local.close()
        return "usuario registrado"

    return f"usuario {email}"

@app.route("/usuario/mostrar")
def usuario_mostrar():
    conexion = Conexion
    conexion_local = conexion.obtener_conexion()
    with conexion_local.cursor() as cursor:
        cursor.execute("SELECT * FROM usuario")
        usuarios = cursor.fetchall()
        conexion_local.close()
    #usuarios= [" Omar sulca", "norma bartra"]
    return render_template("mostrarUsuario.html", usuarios=usuarios)
