class Personaje:
    #constructor
    #metodo o funcion especial encargado de inicializar los atributos de una clase

    def __init__(self,nombre,tipo,casaEditorial):
        #creamos los atributos de la clase
        #ATRIBUTOS=DATOS=VARIABLES
        self.nombre=nombre
        self.tipo=tipo
        self.casaEditorial=casaEditorial
        
#Declaro los metodos o funciones de mi clase
    def saludar(self):
        print("hola como estas....")        