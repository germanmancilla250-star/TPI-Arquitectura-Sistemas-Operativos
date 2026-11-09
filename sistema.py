
import platform
import os
import multiprocessing
import sys

print("================================================")
print("          SISTEMA DE INFORMACION VIRTUAL")
print("================================================")

print()
print("INFORMACION DEL SISTEMA")

print("Sistema operativo:", platform.system())
print("Version:", platform.version())
print("Nombre del equipo:", platform.node())
print("Procesadores disponibles:", multiprocessing.cpu_count())
print("Version de Python:", sys.version.split()[0])
print("Directorio actual:", os.getcwd())

print()
print("================================================")
print("INFORMACION OBTENIDA CORRECTAMENTE")
