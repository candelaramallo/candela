import random
import os


resultados = random.sample(range(0, 46), 6)
print("3) Resultados del Quini 6:")
print("Números sorteados:", resultados)


try:
    with open("resultados.txt", "w") as archivo:
        archivo.write("Resultados del Quini 6:\n")
        archivo.write(", ".join(map(str, resultados)))
    print("\nArchivo 'resultados.txt' generado con éxito.")
except Exception as e:
    print("Error al guardar resultados.txt:", e)


archivo_lenguajes = "lenguajes.txt"


if not os.path.exists(archivo_lenguajes):
    open(archivo_lenguajes, "w").close()

try:
    if os.access(archivo_lenguajes, os.W_OK):
        with open(archivo_lenguajes, "a") as archivo:
            archivo.write("nuevo lenguaje agregado\n")
    else:
        print(f"\nNo hay permisos de escritura para el archivo '{archivo_lenguajes}'")
except Exception as e:
    print(f"\nError al escribir en {archivo_lenguajes}:", e)