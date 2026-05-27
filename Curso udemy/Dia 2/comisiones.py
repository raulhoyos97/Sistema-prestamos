nombre = input("Ingrese su nombre: ")
ventas = int(input("Ingrese su monto vendido en el mes: "))

comisiones = round(ventas * 13 / 100, 2)

print(f"El empleado {nombre} ha vendidio ${ventas} y su comision es ${comisiones}")