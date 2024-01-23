def transposicion_con_clave(mensaje, clave):
    texto_sin_espacios = ''.join([c for c in mensaje if c != ' '])
    m2 = len(texto_sin_espacios)
    columnas = len(clave)
    renglones = (m2 + columnas - 1) // columnas
   
    # Rellenar el texto plano con caracteres de relleno (en este caso 'x')
    texto_sin_espacios += 'x' * (renglones * columnas - m2)
   
    # Crear una lista de columnas y ordenarlas por la clave
    columna = [texto_sin_espacios[i::columnas] for i in range(columnas)]
    columnas_ordenadas = [x for _, x in sorted(zip(clave, columna))]
    #Construir el mensaje cifrado
    texto_cifrado = ''.join([''.join(columnas_ordenadas)])
    return texto_cifrado

def descifrado_transposicion(texto_cifrado, clave):
    columnas = len(clave)
    renglones = len(texto_cifrado) // columnas
    
    # Crear una lista de columnas en el orden original
    columna = [''] * columnas
    
    # Ordenar las columnas con la clave
    for i, letra in enumerate(sorted(clave)):
        index = clave.index(letra)
        columna[index] = texto_cifrado[i * renglones:(i + 1) * renglones]
    
    # Concatenar las columnas en el orden original
    texto = ''.join([''.join(columna)]).rstrip('x')

    # Calcular el número de caracteres en el texto
    m2 = len(texto)
    # Calcular el número de renglones en función de las columnas y la longitud del texto
    ren = (m2 + columnas - 1) // columnas

    # Crear una matriz vacía con las dimensiones adecuadas
    matriz = [[''] * columnas for _ in range(ren)]

    # Llenar la matriz en orden de renglones desde el texto
    char_index = 0
    for i in range(columnas):
        for j in range(ren):
            if char_index < m2:
                matriz[j][i] = texto[char_index]
                char_index += 1

    # Construir el mensaje descifrado 
    texto_descifrado = ''
    for i in range(ren):
        for j in range(columnas):
            texto_descifrado += matriz[i][j]

    #Quita las 'x' del mensaje descifrado
    texto_descifrado = ''.join([c for c in texto_descifrado if c != 'x'])

    return texto_descifrado

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
        texto_plano = input("Frase a cifrar: ").lower()
        clave = input("Palabra clave: ").lower()
        texto_cifrado = transposicion_con_clave(texto_plano, clave)
        if texto_cifrado: #Valida que haya mensaje cifrado
            print("Mensaje cifrado:", texto_cifrado)
    elif opcion == "2":
        texto_cifrado = input("Mensaje cifrado: ").lower()
        clave = input("Palabra clave: ").lower()
        texto_descifrado = descifrado_transposicion(texto_cifrado, clave)
        if texto_descifrado: # Valida que haya mensaje descifrado
            print("Mensaje descifrado:", texto_descifrado)
    else:
        print("Opción no válida")