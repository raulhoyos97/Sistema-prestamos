def calcularPrestamos():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Que edad tienes: "))


    if edad < 18:
        print("No Tiene derecho a prestamo")
        exit()
    elif edad > 18:
        print("tiene derecho a prestamo")
    else:
        print("No se ingreso ninguna edad")

    monto = int(input("Que monto de prestamo oucpa: "))        

    if monto == 1000:
        dias = 10
    elif monto == 2000:
        dias = 20
    elif monto == 3000:
        dias = 30
    else:
        print("No ingreso cantidad")  
    total = monto + (monto * 0.15)
        

    print(f"Hola {nombre} la cantidad de su prestamo es {monto} y devera pagar {total} en {dias} dias")

calcularPrestamos()


def prestamos_vencidos():
    hoy = datetime.now()
    for prestamo in prestamos:
        vencimiento = datetime.strptime(prestamo["vencimiento"], "%d/%m/%Y")
        if vencimiento < hoy:
            print(f"VENCIDO | Cliente ID: {prestamo['id_cliente']} | Monto: ${prestamo['monto']} | Venció: {prestamo['vencimiento']}")
         
