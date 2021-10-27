import json

with open("1.json") as mis_datos:
    datos = json.loads(mis_datos.read())
    print(datos)
    print(datos['nombre'])
    print(datos['apodo'])
    print(datos['clubes'])
    print(datos['clubes'][0])
    print(datos['clubes'])