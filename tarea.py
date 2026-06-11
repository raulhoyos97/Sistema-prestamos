clientes = []

menu_platillos = {
    1: "Enchiladas Verdes",
    2: "Tacos de Asada",
    3: "Chilaquiles con Pollo",
    4: "Pozole Rojo",
    5: "Cochinita Pibil"
}

def registrar_clientes():
    nombre = input("Escribe tu nombre: ")
    apellido = input("Escribe tu apellido: ")
    edad = int(input("Cual es su edad?: "))

    print("\n--- MENÚ DE PLATILLOS ---")
    print("1. Enchiladas Verdes")
    print("2. Tacos de Asada")
    print("3. Chilaquiles con Pollo")
    print("4. Pozole Rojo")
    print("5. Cochinita Pibil")

    opcion = int(input("Selecciona el número de platillo (1 al 5): "))

    platillo_elegido = menu_platillos.get(opcion, "Platillo no válido")

    cliente = {
        "id": len(clientes) + 1,
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "platillo": platillo_elegido
    }

    clientes.append(cliente)
    print(f"\n¡Cliente registrado con éxito! Eligió: {platillo_elegido}\n")

registrar_clientes()