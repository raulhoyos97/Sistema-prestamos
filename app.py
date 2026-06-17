from flask import Flask, render_template
from datetime import datetime
import prestamos

prestamos.cargar_datos()

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/about")
def about():
    return """
    <h1>Raul Hoyos</h1>
    <p>Hola soy Raul, soy de Mérida Yucatán, quiero aprender Python, base de datos e IA</p>
    """


@app.route("/clientes")
def ver_clientes():
    return render_template("clientes.html", clientes=prestamos.clientes)

@app.route("/prestamos")
def ver_prestamos():
    return render_template("prestamos.html", prestamos=prestamos.prestamos)

@app.route("/vencidos")
def ver_vencidos():
    hoy = datetime.now()
    vencidos = []
    for prestamo in prestamos.prestamos:
        vencimiento = datetime.strptime(prestamo["vencimiento"], "%d/%m/%Y")
        if vencimiento < hoy:
            vencidos.append(prestamo)
    return render_template("vencidos.html", prestamos=vencidos)


@app.route("/resumen")
def ver_resumen():
    total = 0
    for prestamo in prestamos.prestamos:
        total += prestamo["total"]
    return render_template("resumen.html", prestamos=prestamos.prestamos, total=total)

if __name__ == "__main__":
    app.run(debug=True)