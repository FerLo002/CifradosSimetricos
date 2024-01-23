def generar_alfabeto_modificado_medio(palabra_clave, alfabeto_original, posicion_insercion):
    # Eliminar espacios y letras duplicadas en la palabra clave
    palabra_clave = palabra_clave.replace(" ", "")
    palabra_clave = "".join(sorted(set(palabra_clave), key=palabra_clave.index))


    tamano_palabra = len(palabra_clave)
    tamano_alfabeto = len(alfabeto_original)
    final = tamano_alfabeto - tamano_palabra


    # Crear el alfabeto modificado
    alfabeto_modificado = ""
    for letra in alfabeto_original:
        if letra not in palabra_clave:
            alfabeto_modificado += letra

    primera_parte = alfabeto_modificado[:posicion_insercion]
    segunda_parte = alfabeto_modificado[posicion_insercion:final]

    alfabeto_modificado = primera_parte + palabra_clave + segunda_parte

    return alfabeto_modificado

def cifrar_mensaje(mensaje, palabra_clave, alfabeto_original, posicion_insercion):

    mensaje = mensaje.replace(" ", "")

    alfabeto_modificado = generar_alfabeto_modificado_medio(palabra_clave, alfabeto_original, posicion_insercion)

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

def descifrar_mensaje(mensaje_cifrado, palabra_clave, alfabeto_original, posicion_insercion):
        
    alfabeto_modificado = generar_alfabeto_modificado_medio(palabra_clave, alfabeto_original, posicion_insercion)

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

# Ejemplo de uso
palabra_clave = input("Palabra Clave: ").lower()
mensaje = input("Mensaje: ").lower()
try:
    posicion_insercion = int(input("Posicion: "))
    mensaje_cifrado = cifrar_mensaje(mensaje, palabra_clave, alfabeto_original, posicion_insercion)
    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, palabra_clave, alfabeto_original, posicion_insercion)
    print("Mensaje cifrado:", mensaje_cifrado)
    print("Mensaje descifrado:", mensaje_descifrado)
except ValueError:
    print("ERROR: Ingrese un número")