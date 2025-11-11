from flask import Flask, render_template
app=Flask(__name__)

#@app.route("/")
#def inicio():
#    return render_template("index.html" )

@app.route("/saludar")
def saludar():
    return render_template("saludar.html")

@app.route("/usuario")
def usuario():
    nombre="Lucas"
    return render_template("usuario.html",
                                          nombre=nombre)

@app.route("/")
def curso():
    datos={
        "nombre":"Lucas",
        "curso":"Python",
        "nota":5
    }
    return render_template("index.html",info=datos)











if __name__==("__main__"):
    app.run(debug=True)

