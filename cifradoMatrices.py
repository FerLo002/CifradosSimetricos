def cif_fil(mensaje, ren):
    # Eliminar espacios y convertir el mensaje a minúsculas
    texto_sin_espacios = ''.join([c for c in mensaje if c != ' '])
    m2 = len(texto_sin_espacios)
    col = (m2 + ren - 1) // ren 

    # Crear una matriz llena de x para el cifrado
    matriz = [["x"] * col for _ in range(ren)]

    # Llenar la matriz con los caracteres del string
    char_index = 0  # Variable para rastrear la posición actual en el string
    for i in range(ren):
        for j in range(col):
            if char_index < len(texto_sin_espacios):
                matriz[i][j] = texto_sin_espacios[char_index]
                char_index += 1

    # Crear una matriz invertida con las dimensiones invertidas
    matriz_invertida = [['' for _ in range(ren)] for _ in range(col)]

    # Variables para rastrear la posición actual en la matriz original y en la matriz invertida
    char_index = 0

    # Llenar la matriz invertida con los elementos de la matriz original
    for i in range(col):
        for j in range(ren):
            if char_index < ren * col:
                matriz_invertida[i][j] = matriz[char_index // col][char_index % col]
                char_index += 1

    # Construir el mensaje cifrado desde la matriz invertida
    encrypted_message = ''
    for i in range(ren):
        for j in range(col):
            encrypted_message += matriz_invertida[j][i]  # Invertir filas y columnas

    return encrypted_message

#descifrado por filas
def desc_fil(mensaje_cifrado, ren):
    # Calcular el número de columnas en función del tamaño del mensaje cifrado y el número de renglones
    col = (len(mensaje_cifrado) + ren - 1) // ren

    # Crear una matriz vacía con las dimensiones adecuadas
    matriz = [[''] * col for _ in range(ren)]

    # Variables para rastrear la posición actual en el mensaje cifrado
    char_index = 0

    # Llenar la matriz en orden de columna desde el mensaje cifrado
    for i in range(ren):
        for j in range(col):
            if char_index < len(mensaje_cifrado):
                matriz[i][j] = mensaje_cifrado[char_index]
                char_index += 1

    # Construir el mensaje original leyendo las columnas en orden
    mensaje_original = ''
    for j in range(col):
        for i in range(ren):
            mensaje_original += matriz[i][j]

    mensaje_original = ''.join([c for c in mensaje_original if c != 'x'])

    return mensaje_original

#Cifrado por renglones
def cif_col(mensaje, col):
    # Eliminar espacios y convertir el mensaje a minúsculas
    texto_sin_espacios = ''.join([c for c in mensaje if c != ' '])
    m2 = len(texto_sin_espacios)
    ren = (m2 + col - 1) // col

    # Crear una matriz llena de x para el cifrado
    matriz = [["x"] * col for _ in range(ren)]

    # Llenar la matriz con los caracteres del string
    char_index = 0  # Variable para rastrear la posición actual en el string
    for i in range(ren):
        for j in range(col):
            if char_index < len(texto_sin_espacios):
                matriz[i][j] = texto_sin_espacios[char_index]
                char_index += 1

    # Construir el mensaje cifrado desde la matriz original
    encrypted_message = ''
    for i in range(col):
        for j in range(ren):
            encrypted_message += matriz[j][i]  # Invertir filas y columnas

    return encrypted_message

#descifrado por renglones
def desc_col(mensaje_cifrado, col):
    # Calcular el número de caracteres en el mensaje cifrado
    m2 = len(mensaje_cifrado)
    # Calcular el número de renglones en función de las columnas y la longitud del mensaje cifrado
    ren = (m2 + col - 1) // col

    # Crear una matriz vacía con las dimensiones adecuadas
    matriz = [[''] * col for _ in range(ren)]

    # Llenar la matriz en orden de renglones desde el mensaje cifrado
    char_index = 0
    for i in range(col):
        for j in range(ren):
            if char_index < m2:
                matriz[j][i] = mensaje_cifrado[char_index]
                char_index += 1

    # Construir el mensaje original desde la matriz original
    mensaje_original = ''
    for i in range(ren):
        for j in range(col):
            mensaje_original += matriz[i][j]
    #Quita las 'x' del mensaje cifrado
    mensaje_original = ''.join([c for c in mensaje_original if c != 'x'])

    return mensaje_original

# Definicion de menú
while True:
    print("Opciones:")
    print("Escribe '1' para cifrar por columnas")
    print("Escribe '2' para descifrar por columnas")
    print("Escribe '3' para cifrar por filas")
    print("Escribe '4' para descifrar por filas")
    print("Escribe '0' para salir")

    opcion = input()
    
    if opcion == "0":
        break
    
    if opcion == "1":
        mensaje = input("Frase a cifrar: ").lower()
        try:
            col = int(input("Número de columnas: "))
        except ValueError:
            print("ERROR: Ingrese un número")
        encrypted_message = cif_col(mensaje, col)
        if encrypted_message: #Valida que haya mensaje cifrado
            print("Mensaje cifrado:", encrypted_message) 
    elif opcion == "2":
        mensaje_cifrado = input("Mensaje cifrado: ").lower()
        try:
            col = int(input("Número de columnas: "))
        except ValueError:
            print("ERROR: Ingrese un número")
        mensaje_descifrado = desc_col(mensaje_cifrado, col)
        if mensaje_descifrado:
            print("Mensaje descifrado:", mensaje_descifrado)
    elif opcion == "3":
        mensaje = input("Frase a cifrar: ").lower()
        try:
            ren = int(input("Número de filas: "))
        except ValueError:
            print("ERROR: Ingrese un número")
        encrypted_message = cif_fil(mensaje, ren)
        if encrypted_message: #Valida que haya mensaje cifrado
            print("Mensaje cifrado:", encrypted_message) 
    elif opcion == "4":
        mensaje_cifrado = input("Mensaje cifrado: ")
        try:
            ren = int(input("Número de filas: "))
        except ValueError:
            print("ERROR: Ingrese un número válido")
        mensaje_descifrado = desc_fil(mensaje_cifrado, ren)
        if mensaje_descifrado:
            print("Mensaje descifrado:", mensaje_descifrado)
    else:
        print("Opción no válida")