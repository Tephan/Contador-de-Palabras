# Función para contar la frecuencia de palabras en un texto
def contar_palabras(texto):
    # Dividir el texto en palabras
    palabras = texto.split()
    # Crear un diccionario para almacenar la frecuencia de palabras
    frecuencia_palabras = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        # Eliminar signos de puntuación alrededor de la palabra
        palabra = palabra.strip('.,!?()[]{}":;')
        # Convertir la palabra a minúsculas para evitar diferencias entre mayúsculas y minúsculas
        palabra = palabra.lower()
        # Contar la frecuencia de la palabra y actualizar el diccionario
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    
    # Imprimir el diccionario de frecuencia de palabras
    print("Frecuencia de palabras:")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"{palabra}: {frecuencia}")

# Pedir al usuario que ingrese un texto
texto = input("Ingrese un texto: ")

# Llamar a la función contar_palabras con el texto ingresado
contar_palabras(texto)

