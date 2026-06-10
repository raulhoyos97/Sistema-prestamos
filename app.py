from flask import Flask
from datetime import datetime
import prestamos

prestamos.cargar_datos()

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Sistema de Préstamos</h1>
    <a href="/clientes">Ver Clientes</a>
    <a href="/prestamos">Ver Prestamos</a>
    <a href="/vencidos">Ver Vencidos</a>
    <a href="/resumen">Ver Resumen</a>
    """


@app.route("/clientes")
def ver_clientes():
    html = "<h1>Lista de Clientes</h1>"
    for cliente in prestamos.clientes:
        html += f"<p>{cliente['nombre']} - Edad: {cliente['edad']}</p>"
    return html

@app.route("/prestamos")
def ver_prestamos():
    html = "<h1>Prestamos</h1>"
    for prestamo in prestamos.prestamos:
        html += f"<p>{prestamo['id_cliente']} - monto: {prestamo['monto']}</p>"
    return html

@app.route("/vencidos")
def ver_vencidos():
    hoy = datetime.now()
    html = "<h1>Préstamos Vencidos</h1>"
    for prestamo in prestamos.prestamos:
        vencimiento = datetime.strptime(prestamo["vencimiento"], "%d/%m/%Y")
        if vencimiento < hoy:
            html += f"<p>Cliente ID: {prestamo['id_cliente']} | Monto: ${prestamo['monto']} | Venció: {prestamo['vencimiento']}</p>"
    return html


@app.route("/resumen")
def ver_resumen():
    html = "<h1>Resumen</h1>"
    total = 0
    for prestamo in prestamos.prestamos:
        html += f"<p>{prestamo['id_cliente']} - monto: {prestamo['monto']}</p>"
        total += prestamo["total"]
    html += f"<h2>Total general: ${total}</h2>"
    return html


if __name__ == "__main__":
    app.run(debug=True)