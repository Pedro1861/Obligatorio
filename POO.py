# class Estudiante:
#     def __init__(self, Nombre, Edad, Grado):
#         self.Nombre = Nombre
#         self.Edad = Edad
#         self.Grado = Grado
#     def estudiar(self):
#         print(f'El estudiante {self.Nombre} esta estudiando.')  

# print("INGRESE SUS DATOS:")
# Nombre = input("Digame su nombre:")
# Edad = input("Digame su edad:")
# Grado = input("Digame su grado:")

# estudiante1 = Estudiante(Nombre, Edad, Grado)

# print('DATOS DEL ESTUDIANTE:')
# print('')
# print(f'Nombre: {Nombre}')
# print('')
# print(f'Edad: {Edad}')
# print('')
# print(f'Grado: {Grado}')

# print(estudiante1.estudiar)


# class Club:
#     def __init__(self, nombre, planteles, fundación):
#         self.nombre = nombre
#         self.planteles = planteles
#         self.fundación = fundación
    
#     def comunicado(self):
#         print("Emitir informe sobre el jugador.")

# class Selección(Club):
#     pass
# montevideo_cricket = Club("Montevideo Cricket Club", 3, "1861")
# uruguay = Selección("Union de Rugby del Uruguay", 4, "1970")


# uruguay.comunicado()


# Ejercicio II
# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

# class Estudiante(Persona):
#     def __init__(self,nombre, edad, grado):
#         super().__init__(nombre, edad)
#         self.grado = grado
    
#     def mostrar_grado(self):
#         return f'El grado de {self.nombre} es: {self.grado}'
    
    
# ramiro = Estudiante("Ramiro", 23, 4)
# print (ramiro.mostrar_grado())

class Animal:
    def __init__(self, comer):
        self.comer = comer
class Mamifero:
    def __init__(self, amamantar):
        self.amamantar = amamantar
class Ave:
    def __init__(self, volar):
        self.volar = volar
class Murciélago(Mamifero, Ave):
    def __init__(self, amamantar, volar):
        super().__init__(amamantar, volar)