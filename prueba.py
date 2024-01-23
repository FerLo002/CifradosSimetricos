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

def generar_alfabeto_modificado_medio(palabra_clave, alfabeto_original):
    # Eliminar espacios y letras duplicadas en la palabra clave
    palabra_clave = palabra_clave.replace(" ", "")
    palabra_clave = "".join(sorted(set(palabra_clave), key=palabra_clave.index))
    tamano_palabra = len(palabra_clave)
    tamano_alfabeto = len(alfabeto_original)
    mitad = round((tamano_alfabeto - tamano_palabra)/2)
    final = tamano_alfabeto - tamano_palabra
    print(mitad, final)
    # Crear el alfabeto modificado
    alfabeto_modificado = ""
    for letra in alfabeto_original:
        if letra not in palabra_clave:
            alfabeto_modificado += letra

    primera_parte = alfabeto_modificado[:mitad]
    print(primera_parte)
    segunda_parte = alfabeto_modificado[mitad:final]
    print(segunda_parte)

    alfabeto_modificado = primera_parte + palabra_clave + segunda_parte

    return alfabeto_modificado

def generar_alfabeto_modificado_final(palabra_clave, alfabeto_original):
    # Eliminar espacios y letras duplicadas en la palabra clave
    palabra_clave = palabra_clave.replace(" ", "")
    palabra_clave = "".join(sorted(set(palabra_clave), key=palabra_clave.index))
    alfabeto_modificado = ""
    # Crear el alfabeto modificado
    for letra in alfabeto_original:
        if letra not in palabra_clave:
            alfabeto_modificado += letra
    
    alfabeto_modificado = alfabeto_modificado + palabra_clave
    return alfabeto_modificado

def cifrar_mensaje(mensaje, palabra_clave, alfabeto_original, posicion_insercion):
    if posicion_insercion == 0:
        alfabeto_modificado = generar_alfabeto_modificado(palabra_clave, alfabeto_original)
    elif posicion_insercion == 1:
        alfabeto_modificado = generar_alfabeto_modificado_medio(palabra_clave, alfabeto_original)
    elif posicion_insercion == 2:
        alfabeto_modificado = generar_alfabeto_modificado_final(palabra_clave, alfabeto_original)

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
    if posicion_insercion == 0:
        alfabeto_modificado = generar_alfabeto_modificado(palabra_clave, alfabeto_original)
    elif posicion_insercion == 1:
        alfabeto_modificado = generar_alfabeto_modificado_medio(palabra_clave, alfabeto_original)
    elif posicion_insercion == 2:
        alfabeto_modificado = generar_alfabeto_modificado_final(palabra_clave, alfabeto_original)

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
    posicion_insercion = int(input("Posicion 0:inicio | 1:enmedio | 2:final | : "))
    mensaje_cifrado = cifrar_mensaje(mensaje, palabra_clave, alfabeto_original, posicion_insercion)
    mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, palabra_clave, alfabeto_original, posicion_insercion)
    print("Mensaje cifrado:", mensaje_cifrado)
    print("Mensaje descifrado:", mensaje_descifrado)
except ValueError:
    print("ERROR: Ingrese un número")