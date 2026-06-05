from flask import Flask
import prestamos

prestamos.cargar_datos()

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola, este es mi sistema de préstamos!"

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

if __name__ == "__main__":
    app.run(debug=True)