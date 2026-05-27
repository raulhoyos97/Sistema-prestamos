texto = input("Ingresa un texto: ")
letras = []

text = texto.lower()
letras.append(input("Ingresa la primera letra ").lower())
letras.append(input("Ingresa la segunda letra ").lower())
letras.append(input("Ingresa la tercera letra ").lower())

print("\n")
print("Cantidad de letras")

cantidaddeletras1 = texto.count(letras[0])
cantidaddeletras2 = texto.count(letras[1])
cantidaddeletras3 = texto.count(letras[2])

print(f"Hemos encontrado {cantidaddeletras1} veces en la letra {letras[0]}")
print(f"Hemos encontrado {cantidaddeletras2} veces en la letra {letras[1]}")
print(f"Hemos encontrado {cantidaddeletras3} veces en la letra {letras[2]}")

print("\n")
print("Cantidad de palabras")

palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en el texto")

letra_inicio = texto[0]
letra_final = texto[-1]

print(f"La letra de inicio es {letra_inicio}")
print(f"La letra de final es {letra_final}")

print("\n")
print("Texto al reves")

palabras.reverse()
texto_invertido = " ".join(palabras)

print(f"el texto invertido es {texto_invertido}")

print("\n")
print("Buscar python")

buscar_palabra = "Python" in texto
dic = {True : "si", False : "No"}
print(f"La palabra 'ptyhon' {dic[buscar_palabra]} se encuentra en el texto")
