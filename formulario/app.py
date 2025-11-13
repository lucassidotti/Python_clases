from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def inicio():
    return render_template("index.html")
#Formulario

@app.route('/form',methods=["post"])
def enviar():
    nombre=request.form['nombre']
    edad=request.form['edad']
    tel=request.form['tel']
    return f"Hola {nombre}, sus datos fueron enviados"




if __name__==("__main__"):
    app.run(debug=True)