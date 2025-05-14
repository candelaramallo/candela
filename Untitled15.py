import os

archivo_lenguajes = "lenguajes.txt"

try:
    if os.access(archivo_lenguajes, os.W_OK):
        with open(archivo_lenguajes, "a") as archivo:
            archivo.write("nuevo lenguaje agregado\n")
    else:
        print(f"No hay permisos de escritura para el archivo '{archivo_lenguajes}'")
except Exception as e:
    print(f"Error al escribir en {archivo_lenguajes}:", e)


try:
    resultados = [9, 20, 28, 38, 44, 45]  # ejemplo
    with open("resultados.txt", "w") as archivo:
        archivo.write("Resultados del Quini 6:\n")
        archivo.write(", ".join(map(str, resultados)))
    print("Archivo 'resultados.txt' generado con éxito.")
except Exception as e:
    print("Error al guardar resultados.txt:", e)