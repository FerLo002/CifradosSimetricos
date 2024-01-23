def generar_alfabeto_modificado(palabra_clave, alfabeto_original):
    # Eliminar espacios y letras duplicadas en la palabra clave
    palabra_clave = palabra_clave.replace(" ", "")
    palabra_clave = "".join(sorted(set(palabra_clave), key=palabra_clave.index))


    # Crear el alfabeto modificado
    alfabeto_modificado = palabra_clave
    for letra in alfabeto_original:
        if letra not in palabra_clave:
            alfabeto_modificado += letra


    return alfabeto_modificado

def cifrar_mensaje(mensaje, palabra_clave, alfabeto_original):
    alfabeto_modificado = generar_alfabeto_modificado(palabra_clave, alfabeto_original)
    print("Alfabeto Original  :", alfabeto_original)
    print("Alfabeto Modificado:", alfabeto_modificado)
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra in alfabeto_modificado:
            # Obtener la posición de la letra en el alfabeto original y reemplazarla en el alfabeto modificado
            posicion = alfabeto_original.index(letra)
            mensaje_cifrado += alfabeto_modificado[posicion]
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado

def descifrar_mensaje(mensaje_cifrado, palabra_clave, alfabeto_original):
    alfabeto_modificado = generar_alfabeto_modificado(palabra_clave, alfabeto_original)
    print("Alfabeto Original  :", alfabeto_original)
    print("Alfabeto Modificado:",alfabeto_modificado)
    mensaje_descifrado = ""
    for letra in mensaje_cifrado:
        if letra in alfabeto_modificado:
            # Obtener la posición de la letra en el alfabeto original y reemplazarla en el alfabeto modificado
            posicion = alfabeto_modificado.index(letra)
            mensaje_descifrado += alfabeto_original[posicion]
        else:
            mensaje_descifrado += letra
    return mensaje_descifrado


# Alfabeto original con la letra "ñ" incluida
alfabeto_original = "abcdefghijklmnñopqrstuvwxyz"

# Definicion de menú
while True:
    print("Opciones:")
    print("Escribe '1' para cifrar")
    print("Escribe '2' para descifrar")
    print("Escribe '0' para salir")

    opcion = input()
    
    if opcion == "0":
        break
    
    if opcion == "1":
        palabra_clave = input("Palabra Clave: ").lower()
        mensaje = input("Mensaje: ").lower()
        mensaje_cifrado = cifrar_mensaje(mensaje, palabra_clave, alfabeto_original)
        if mensaje_cifrado: #Valida que haya mensaje cifrado
            print("Mensaje cifrado:", mensaje_cifrado)
    elif opcion == "2":
        palabra_clave = input("Palabra Clave: ").lower()
        mensaje_cifrado = input("Mensaje Cifrado: ").lower()
        mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, palabra_clave, alfabeto_original)
        if mensaje_descifrado: # Valida que haya mensaje descifrado
            print("Mensaje descifrado:", mensaje_descifrado)
    else:
        print("Opción no válida")
