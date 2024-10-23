archivo = open('prueba.txt', 'a')

archivo.write('bienvenido')


archivo.close()


''''''''''''''
mi_archivo = open('mi_archivo.txt', 'w')
mi_archivo.write('Nuevo texto')
mi_archivo.close()
mi_archivo = open('mi_archivo.txt', 'r')
print(mi_archivo.read())
mi_archivo.close()

'''''''''''''
file = open('mi_archivo.txt', 'a')
file.write('Nuevo inicio de sesión')
file.close()
file = open('mi_archivo.txt', 'r')
print(file.read())
file.close()

'''''''''''''
file = open('registro.txt', 'a')
registro_ultima_sesion = ["Federico", "\t20/12/2021", "08:17:32 hs", "Sin errores de carga"]
file.writelines(registro_ultima_sesion)
file.close()
file = open('registro.txt', 'r')
print(file.read())
file.close()