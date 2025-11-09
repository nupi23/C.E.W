from flask import Flask, render_template, request

app = Flask(__name__)
me_paso = "No"
paises = {"europa": 1, "america del norte": 1, "asia": 2, "africa": 0.5, "america del sur": 0.5, "oceania": 2}
@app.route("/")
def pag_cal():
    return render_template("index.html")
@app.route("/result", methods = ["GET", "POST"])
def result():
    global me_paso
    nombre = request.form['nombre']
    pais = request.form["País"]
    pantalla = int(request.form["Pantalla"])
    bombillashoras = int(request.form["Bombillashoras"])
    bombillascant = int(request.form["Bombillascant"])
    if pais in paises:
        multipaises = paises[pais]
    else:
        # Si el país no está registrado, mostrar una alerta en el navegador y volver atrás
        return "<script>alert('El país no se encuentra registrado'); window.history.back();</script>"
    suma = bombillashoras * 3.9 * bombillascant
    suma += pantalla * 10
    suma *= multipaises
    if suma >= 14.7:
        me_paso = "Si"
    else:
        me_paso = "No"
    return render_template("Result.html", suma=suma, pantalla=pantalla, bombillashoras=bombillashoras, bombillascant=bombillascant, nombre=nombre, me_paso=me_paso)
@app.route("/calculadora")
def pag_cal2():
    return render_template("index.html")
app.run(debug=True)