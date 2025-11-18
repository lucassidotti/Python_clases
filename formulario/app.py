from flask import Flask, render_template, request, url_for, redirect
app=Flask(__name__)
#Lista de datos, simulamos una DB
perfiles=[]
@app.route("/")
def inicio():
    return render_template ("index.html")

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre=request.form["nombre"]
    edad=request.form["edad"]
    tel=request.form["tel"]
    perfiles.append({"nombre":nombre,"edad":edad,"tel":tel})
    return redirect(url_for("verPerfil"))

@app.route("/recibir")
def verPerfil():
    return render_template("recibir.html",perfiles=perfiles)

if __name__==("__main__"):
    app.run(debug=True)