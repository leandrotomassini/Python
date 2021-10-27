# decodigo.com
import os
# Se define el nombre de la carpeta o directorio a crear
directorio = "E://carpeta"
try:
    os.mkdir(directorio)
except OSError:
    print("La creación del directorio %s falló" % directorio)
else:
    print("Se ha creado el directorio: %s " % directorio)