def cifrar_cesar(texto, llave):
    texto_cifrado = ""

    for letra in texto:
        if letra.isalpha():
            alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
            # Realiza el cifrado César
            posicion = alfabeto.index(letra)
            nueva_posicion = (posicion + llave) % 27
            nueva_letra = alfabeto[nueva_posicion]

            texto_cifrado += nueva_letra
        else:
            # Si no es una letra, se mantiene sin cambios
            texto_cifrado += letra
    return texto_cifrado

def descifrar_cesar(texto, llave):
    texto_descifrado = ""

    for letra in texto:
        if letra.isalpha():
            alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

            # Realiza el descifrado César
            posicion = alfabeto.index(letra)
            nueva_posicion = (posicion - llave) % 27
            nueva_letra = alfabeto[nueva_posicion]
            texto_descifrado += nueva_letra
        else:
            # Si no es una letra, se mantiene sin cambios
            texto_descifrado += letra
    return texto_descifrado

# Definicion de menú
while True:
    print("Opciones:")
    print("Escribe 'cifrar' para cifrar el texto")
    print("Escribe 'descifrar' para descifrar el texto")
    print("Escribe 'salir' para salir")

    opcion = input().lower()
    
    if opcion == "salir":
        break
    
    if opcion == "cifrar":
        m = input("Texto a cifrar: ").lower()
        k = input("Llave de cifrado: ")
        try:
            k=int(k)
        except ValueError:
            print("Error: Debes ingresar números válidos")
            continue
        c = cifrar_cesar(m, k)
        print("Texto cifrado: ", c)
    elif opcion == "descifrar":
        c = input("Texto a descifrar: ").lower()
        k = input("Llave de cifrado: ")
        try:
            k=int(k)
        except ValueError:
            print("Error: Debes ingresar números válidos")
            continue
        m = descifrar_cesar(c, k)
        print("Texto descifrado:", m)
    else:
        print("Opción no válida")