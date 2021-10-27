f = open('E://1 - Desarrollo Web/Escuela de Desarrollo Web/holamundo.txt','a')
f.write('Hola Mundo' + '\n')
f.close()

f = open ('E://1 - Desarrollo Web/Escuela de Desarrollo Web/holamundo.txt','r')
mensaje = f.read()
print(mensaje)
f.close()