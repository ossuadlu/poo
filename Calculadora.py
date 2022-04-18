class Calculadora:
    #constructor
    #metodo o funcion especial encargado de inicializar los atributos de una clase
    #todo constructor recibe los atributos

    def __init__(self,numero1,numero2):
        #creamos los atributos de la clase
        #ATRIBUTOS=DATOS=VARIABLES
        self.numero1=numero1
        self.numero2=numero2
        
#Declaro los metodos o funciones de mi clase
    def sumar(self):
        return(self.numero1+self.numero2)

    def restar(self):
        return(self.numero1-self.numero2)

    def multiplicar(self):
        return(self.numero1*self.numero2)

    def dividir(self):
        return(self.numero1/self.numero2)

          