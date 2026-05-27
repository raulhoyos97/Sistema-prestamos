productos = []
total_general = 0
def registrar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    stock = int(input("Stock: "))

    producto = {
        "id": len(productos) + 1,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    productos.append(producto)
    print("Producto registrado")

def menu():
    global total_general
    while True: 
        print("\n---MENU---")
        print("1. Registrar productos")
        print("2. Ver productos")
        print("3. Salir")
        print("4. Vender producto")
        print("5.Total vendido")

        opcion = input("Ingrese una opción")

        if opcion == "1":
            registrar_producto()
            continue

        elif opcion == "2":

            if len(productos) == 0:
                print("No hay productos")
                continue

            for producto in productos:
                print(f"Nombre: {producto['nombre']}")
                print(f"Precio: {producto['precio']}")
                print(f"Stock: {producto['stock']}")
                print("------")

        elif opcion == "3":
            print("Saliendo del punto")
            break     

        elif opcion == "4":
            nombre_buscar = input("¿Qué producto quieres vender?: ")
            cantidad = int(input("¿Cuántos quieres vender?: "))
            encontrado = False

            for producto in productos:
                if producto["nombre"].lower() == nombre_buscar.lower():
                    encontrado = True

                    if producto["stock"] >= cantidad:
                        total = producto["precio"] * cantidad

                        print(f"Total a pagar: {total}")
                        pago_cliente = float(input("¿Con cuánto paga el cliente?: "))
                        if pago_cliente >= total:
                            total_general = total_general + total
                            producto["stock"] = producto["stock"] - cantidad
                            print("Stock restante:", producto["stock"])

                            print("Venta realizada")
                            print("Total acumulado:", total_general)
                            if pago_cliente == total:
                                print("Pago exacto")
                            else:
                                cambio = pago_cliente - total
                                print("Tu cambio es:", cambio)
                            break

                        else:
                            print("No tienes suficiente dinero")
                            break
                    else:
                        print("No hay suficiente stock")
                        break


            if not encontrado:
                print("Producto no encontrado")


        elif opcion == "5":
            print("Total vendido:", total_general)

menu()                    