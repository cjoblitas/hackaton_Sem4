from objeto import Docente,Archivo,Alumno
from os import remove,system

cursos = [i.split(',')[1] for i in Archivo.leer_archivo('Cursos') if i != '']
if len(cursos) == 0:
    Archivo.escribir_archivo('Cursos','python')
    cursos = [i.split(',')[1] for i in Archivo.leer_archivo('Cursos') if i != '']

ejecucion = True

while ejecucion:
    
    print("""MENU
    1. Ingresar datos del Profesor.
    2. Ingresar datos del Alumno.
    3. Editar base cursos.
    4. Salir""")

    opc = input("Ingrese opc: ").strip()

    if opc == "1":
        nombre = input("Ingrese nombre: ").strip()
        apellido = input("Ingrese apellido: ").strip()
        dni = input("Ingrese DNI: ").strip()
        edad = input("Ingrese edad: ").strip()
        print("Los cursos son: ")
        index = 1
        for i in cursos:
            print(f'{index}. {i}')

        print('**********')
        while True:
            curso = input("Ingrese curso: ")
            if curso in cursos:
                break
            else:
                print("Elija un curso existente")

        docente = Docente(nombre,apellido,edad,dni,curso)

        datos_formato = docente.obtener_datos()

        Archivo.escribir_archivo('Docentes',datos_formato)

    elif opc == "2":
        nombre = input("Ingrese nombre: ").strip()
        apellido = input("Ingrese apellido: ").strip()
        dni = input("Ingrese DNI: ").strip()
        edad = input("Ingrese edad: ").strip()
        print("Los cursos son: ")
        index = 1
        for i in cursos:
            print(f'{index}. {i}')

        print('**********')
        while True:
            curso = input("Ingrese curso: ")
            if curso in cursos:
                break
            else:
                print("Elija un curso existente")
        while True:
            nro_notas = input("Ingrese numero de notas: ").strip()
            if nro_notas.isdigit():
                nro_notas = int(nro_notas)
                break
        else:
            print("Ingrese un numero valido")
            
        alumno = Alumno(nombre,apellido,edad,dni,curso,nro_notas)

        index = 0

        while index < nro_notas:
            try:
                valor = float(input("Ingrese la nota: ").strip())
                alumno.anadir_nota(valor)
                index += 1
            except ValueError:
                print("Ingrese una nota valida")

        alumno_formato = alumno.obtener_estructura_alumno()
        notas_formato = alumno.obtener_estructura_nota()

        Archivo.escribir_archivo('Alumnos',alumno_formato)

        Archivo.escribir_archivo('Notas',notas_formato)
                
    elif opc == "3":
        dni = input("Ingresa tu dni: ")
        resultado = Archivo.comprobar_docente(dni)

        if resultado != None:
            if resultado:
                
                while True:
                    cursos = [i.split(',')[1] for i in Archivo.leer_archivo('Cursos') if i != '']
                    print("Los cursos son: ")
                    index = 1
                    for i in cursos:
                        print(f'{index}. {i}')

                    print('**********')
                
                    print("""a. Añadir Curso\nb. Eliminar Curso.\nc. Salir""")
                    opcion_curso = input("Ingrese opcion: ").strip()

                    if opcion_curso == 'a':
                        curso = input("Ingrese el curso: ").strip()

                        if curso in cursos:
                            print("Ese curso ya existe")
                        else:
                            Archivo.escribir_archivo('Cursos',curso)

                    elif opcion_curso == 'b':
                        nombre_curso = input("Ingrese el nombre del curso: ").strip()

                        if nombre_curso not in cursos:
                            print("ese curso no existe")
                        else:
                            cursos.remove(nombre_curso)
                            remove('Cursos.txt')
                            for i in cursos:
                                Archivo.escribir_archivo('Cursos',i)
                    elif opcion_curso == 'c':
                        break
                    else:
                        print("Opcion ingresada incorrecta")

                    seguir = input("Desea volver a ejecutar las opiones de añadir y eliminar?: s/n").strip()

                    if seguir != 's':
                        break
            else:
                print("No tienes acceso.")

    elif opc == 4:
        break
    else:
        print("Opcion incorrecta.")

    decision = input("Desea seguir? s/n: ").strip()

    if decision != 's': ejecucion = False