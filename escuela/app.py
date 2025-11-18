from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)


def get_db():
    conn = sqlite3.connect("escuela.db")
    conn.row_factory = sqlite3.Row
    return conn


with get_db() as db:
    db.execute("""
               CREATE TABLE IF NOT EXISTS estudiantes(
               id INTEGER PRYMARY KEY AUTOINCREMENT,
               nombre TEXT NOT null,
               apellido TEXT NOT null,
               edad INTEGER NOT null,
               grado TEXT NOT null
""")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        edad = request.form["edad"]
        grado = request.form["grado"]
        db = get_db()
        db.execute(
            "INSERT INTO estudiantes(nombre,apellido,edad,grado) VALUES (????)",
            (nombre, apellido, edad, grado),
        )
        db.commit()
        return redirect(url_for("ver_estudiantes"))
    return render_template("agregar.html")


@app.route("/ver")
def ver_estudiantes():
    db = get_db()
    estudiantes = db.execute("SELECT * FROM estudiantes").fetchall()
    return render_template("ver.html", estudiantes=estudiantes)


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    db = get_db()
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        edad = request.form["edad"]
        grado = request.form["grado"]
        db.execute(
            "UPDATE estudiantes SET nombre=?,apellido=?,edad=?,grado=? WHERE id=?",
            (nombre, apellido, edad, grado),
        )
        db.commit()
        db.close()
        return redirect(url_for("ver_estudiantes"))
    estudiantes = db.execute("SELECT * FROM estudiantes WHERE id=?", (id,)).fetchone()
    return render_template("editar.html", estudiantes=estudiantes)


@app.route("/eliminar/<int:id>")
def eliminar(id):
    db = get_db()
    db.execute("DELETE FROM estudiantes WHERE id=?", (id,))
    db.commit()
    return redirect(url_for("ver_estudiantes"))


if __name__ == "__main__":
    app.run(debug=True)
