from datetime import datetime, timedelta
import json
clientes = []
prestamos = []

def registrar_cliente():
    nombre = input("¿Cual es tu nombre?: ")
    apellido = input("Cual es su apellido?: ")
    edad = int(input("Edad: "))
    
    cliente = { 
        "id": len(clientes) + 1,      
        "nombre": nombre + " " + apellido,
        "edad": edad
    }
    clientes.append(cliente)

    print("Cliente registrado correctamente")
    

def inicio():
    nombre = input("¿Cual es tu nombre?: ")
    apellido = input("Cual es su apellido?: ")
    edad = int(input("¿Cual es su edad?: "))
    nombreCompleto = nombre + " " + apellido

    if edad < 18:
        print("No tienes derecho a préstamo")
        exit()
    else:
        print("Tiene derecho a préstamo con identificación")

    print(f"Hola joven, su nombre es {nombreCompleto} y su edad es {edad}")

    cliente = {
        "id": len(clientes) + 1,
        "nombre": nombreCompleto,
        "edad": edad
    }
    clientes.append(cliente)

    return nombreCompleto


tasa = 0.15


def buscar_cliente(id_buscado):
    for cliente in clientes:
        if cliente["id"] == id_buscado:
            return cliente
    return None    

def buscar_prestamo(id_cliente):
    resultados = []
    for prestamo in prestamos:
        if prestamo["id_cliente"] == id_cliente:
            resultados.append(prestamo)
    return resultados


def registrar_prestamo(id_cliente, monto, dias):
    hoy = datetime.now()
    vencimiento = hoy + timedelta(days=dias)
    prestamo = { 
        "id_cliente": id_cliente,      
        "monto": monto,
        "dias": dias,
        "interes": monto * tasa,
        "total": monto + (monto * tasa),
        "vencimiento": vencimiento.strftime("%d/%m/%Y"),
    }
    prestamos.append(prestamo)

def guardar_datos():
    datos = {
        "clientes": clientes,
        "prestamos": prestamos
    }
    with open("datos.json", "w") as archivo:
        json.dump(datos, archivo)
    print("Datos guardados")  

def cargar_datos():
    global clientes, prestamos
    try:
        with open("datos.json", "r") as archivo:
            datos = json.load(archivo)
            clientes = datos["clientes"]
            prestamos = datos["prestamos"]
    except:
        clientes = []
        prestamos = []     


def prestamos_vencidos():
    hoy = datetime.now()
    for prestamo in prestamos:
        vencimiento = datetime.strptime(prestamo["vencimiento"], "%d/%m/%Y")
        if vencimiento < hoy:
            print(f"VENCIDO | Cliente ID: {prestamo['id_cliente']} | Monto: ${prestamo['monto']} | Venció: {prestamo['vencimiento']}")
         

def menu():
    while True:

        print("\nOpciones de Préstamos")
        print("0-Registrar nuevo cliente")
        print("1- $1000 a 10 días")
        print("2- $2000 a 20 días")
        print("3- $3000 a 30 días")
        print("4- Clientes")
        print("5- Ver clientes registrados")
        print("6- Salir")
        print("7- Ver préstamos de cliente")
        print("8- Ver préstamos vencidos")

        opcion = input("Ingresa un numero: ")
        
        if opcion == "0":
            registrar_cliente()
            continue
            
        elif opcion == "1":
            monto = 1000
            dias = 10

        elif opcion == "2":
            monto = 2000
            dias = 20

        elif opcion == "3":
            monto = 3000
            dias = 30

        elif opcion == "4":
            print(f"Actualmente hay {len(clientes)} clientes")  
            continue 

        elif opcion == "5":
            if len(clientes) == 0:
                print("Lista vacía")
            else:
                for cliente in clientes:
                    print(f"ID: {cliente['id']} | Nombre: {cliente['nombre']}")
            continue 
        
        elif opcion == "6":
            print("Saliendo del sistema...")
            guardar_datos()
            break 
        
        elif opcion == "7":
            id_cliente = int(input("Ingresa el ID del cliente: "))
            cliente_encontrado = buscar_cliente(id_cliente)

            if cliente_encontrado is None:
                print("Cliente no encontrado")
                continue

            print(f"Préstamos de {cliente_encontrado['nombre']}:")

            prestamos_encontrados = buscar_prestamo(id_cliente)
            for prestamo in prestamos_encontrados:
                print(f"- ${prestamo['monto']} a {prestamo['dias']} días | Total: ${prestamo['total']} | Vence: {prestamo['vencimiento']}")

            continue
        elif opcion == "8":
            prestamos_vencidos()
            continue

        else:
            print("Opción no válida")
            continue

        # SOLO entra aquí si eligió 1, 2 o 3
        if opcion in ["1", "2", "3"]:
            id_cliente = int(input("Ingresa el ID del cliente: "))
            cliente_encontrado = buscar_cliente(id_cliente)

            if cliente_encontrado is None:
                print("Cliente no encontrado")
                continue

            registrar_prestamo(id_cliente, monto, dias)
            print(f"Total a pagar: ${monto + (monto * tasa)} en {dias} días")


def resumen(prestamos):
    print("Lista de préstamos registrados:")
    total_general = 0

    for prestamo in prestamos:
        cliente = buscar_cliente(prestamo["id_cliente"])
        print(f"Nombre: {cliente['nombre']} | Total: ${prestamo['total']}")
        total_general += prestamo["total"]

    print("Total general prestado: ", total_general)

    if len(prestamos) > 0:
        promedio = total_general / len(prestamos)
        print("Promedio de préstamos: ", promedio)
    else:
        print("No hay préstamos para calcular promedio")


# EJECUCIÓN
cargar_datos()
nombreCompleto = inicio()
menu()
resumen(prestamos)