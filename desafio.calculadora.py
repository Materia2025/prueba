#Desafío3 Desafío3 Desarrollar un programa en el cual el Usuario ingrese dos valores enteros por teclado.
#Utilizar el método __init__. Incluir el calculo de la suma, resta, multiplicación y división. 
#Utilizar un método para cada una de las operaciones. Nombrar a la clase Calculadora.

class Calculadora:
    def __init__(self, numero1, numero2):
        self._numero1 = numero1
        self._numero2 = numero2

    @property
    def numero1(self):
        return self._numero1
    
    @numero1.setter
    def numero1(self, numero_1):
        self._numero1=numero_1
    
    @property
    def numero2(self):
        return self._numero2
    
    @numero2.setter
    def numero2(self, numero_2):
        self._numero2=numero_2


    def sumar(self):
        return self.numero1+self.numero2
    
    def restar(self):
        return self.numero1-self.numero2
    
    def multiplicar(self):
        return self.numero1*self.numero2
    
    def dividir(self):
        if self.numero2 !=0:
            return self.numero1/self.numero2
        else:
            return "no es posible dividir un numero por cero(0)"

#demostracion:
n1=int(input("ingresar el primer numero entero: "))
n2= int(input("ingresar el segundo numero entero: "))

mi_calculadora= Calculadora (n1,n2)
    
print("\nresultado: ")
print("suma= ", mi_calculadora.sumar())
print("resta= ", mi_calculadora.restar())
print("multiplicacion= ", mi_calculadora.multiplicar())
print("division= ", mi_calculadora.dividir())