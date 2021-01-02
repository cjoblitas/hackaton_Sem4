from os import path

class Persona:
    def __init__(self,nombre,apellido,edad,dni,curso):#constructor
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.curso = curso


class Docente(Persona):
    def __init__(self,nombre,apellido,edad,dni,curso):
        super().__init__(nombre,apellido,edad,dni,curso)

    def obtener_datos(self):
        return f'Docente:{self.nombre} {self.apellido},Edad:{self.edad},Dni:{self.dni},Curso:{self.curso}'

class Alumno(Persona):
    def __init__(self,nombre,apellido,edad,dni,curso,nro_notas):
        super().__init__(nombre,apellido,edad,dni,curso)

        self.notas = list()
        self.nro_notas = nro_notas

    def anadir_nota(self,valor):
        self.notas.append(valor)

    def obtener_estructura_alumno(self):

        return f'Alumno:{self.nombre} {self.apellido},Edad:{self.edad},DNI:{self.dni}'

    def obtener_estructura_nota(self):

        nota_maxima = max(self.notas)
        nota_minima = min(self.notas)
        promedio = sum(self.notas)/len(self.notas)

        return f'Alumno:{self.nombre} {self.apellido},Curso:{self.curso},Notas:{str(self.notas)},Nota maxima:{nota_maxima},Nota minima:{nota_minima},Promedio:{promedio}'

class Archivo():

    @classmethod
    def leer_archivo(clc,nombre):
        f = open(nombre+'.txt','r')
        datos = f.read()
        f.close()

        return datos.split('\n')

    @classmethod
    def obtener_id(clc,nombre):
        if not path.exists(nombre):
            tamano = 0    
        else:   
            f = open(nombre,'r')
            f.seek(0)
            tamano = len(f.readlines())
            f.close()

        return tamano+1

    @classmethod
    def escribir_archivo(clc,nombre,value):
        nombre = nombre +'.txt'
        if not path.exists(nombre):
            f = open(nombre,'w')
        else:
            f = open(nombre,'a')
        id_b = clc.obtener_id(nombre)
        f.write(f'Id:{id_b},'+value+'\n')

        f.close()

    @classmethod
    def comprobar_docente(clc,dni):
        nombre = 'Docentes.txt'
        if not path.exists(nombre):
            print("Aun no se ha registrado ningun docente")
            return None
        else:
            f = open(nombre,'r')
            datos = f.read()
            f.close()

            if dni in datos:
                return True
            else:
                return False