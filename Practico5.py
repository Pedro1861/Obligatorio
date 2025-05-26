#1
#  class Bombilla: 
#     def estado(self, prendido, apagado):
#         self.esta_prendida = False
    
#     def encender(self):
#         self.esta_prendida = True
    
#     def apagar(self):
#         self.esta_prendida = False

#     def estado(self):
#         return "Esta prendida" if self.esta_prendida == True else "Esta apagada"
       
 
    

# if __name__ =="__main__":
#     bomb = Bombilla()
#     bomb.apagar()
#     print(bomb.estado())

# 2
# import math
# class Círculo:

#     def __init__(self, radio):
#         self.radio = radio
    
#     def área(self):
#         return math.pi*self.radio**2

# if __name__ =="__main__":
#     c1 = Círculo(0)
#     print(c1.radio)
#     print(c1.área())

# 3

# class CuentaCorriente:

#     def __init__(self, saldo):
#         self.saldo = saldo
    
#     def saldo(self):
#         return self.saldo
    
    

#     def nuevo_saldo(self, nuevo_saldo):
#         nuevo_saldo += self.saldo
#         return nuevo_saldo



#     def saldo_reintegro(self, reintegro):
#         self.saldo_reintegro = 0.0 - reintegro

# if __name__ == "__main__":
#     cc1 = CuentaCorriente(10000)
#     print("Saldo inicial:", cc1.saldo)

#     cc1.nuevo_saldo(5000)
#     print("Nuevo Saldo:", cc1.nuevo_saldo(5000))

#     cc1.saldo_reintegro(3000)



# 4.
# class Emisora:
    
#     def __init__(self, frecuencia):
#         self.frecuencia = frecuencia
    
#     def down(self):
#         self.frecuencia -= 0.5      
#         if self.frecuencia < 80:
#             self.frecuencia = 108
    
#     def up(self):
#         self.frecuencia += 0.5
#         if self.frecuencia > 108:
#             self.frecuencia = 80

# if __name__ == "__main__":
#     MiEmisora = Emisora(80)
#     print("Frecuencia", MiEmisora.frecuencia, "Mhz.")
    
#     MiEmisora.up()
#     print("Frecuencia:", MiEmisora.frecuencia, "Mhz.")


class Calc:
    def __init__(self, suma, resta, mult, div):
        self.suma = suma
        self.resta = resta
        self.mult = mult
        self.div = div
    
    def sum(self):
        a = int(input("Ingrese un valor:"))
        b = int(input("Ingrese un valor:"))
        c = a+b

    def res(self):

