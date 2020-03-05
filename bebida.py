import os

class Bebida:
    def __init__(self, nombre, grado, origen): 
        self.nombre = nombre 
        self.grado = grado 
        self.origen = origen 

    def tipo1(self):
        tipo1 = ("Ron con el nombre de {}, su grado de alcohol es {} y pais de origen {}") 
        print(tipo1.format(self.nombre, self.grado, self.origen)) 

    def tipo2(self):
        tipo2 = ("Whisky con el nombre de {}, su grado de alcohol es {} y pais de origen {}") 
        print(tipo2.format(self.nombre, self.grado, self.origen)) 

    def tipo3(self):
        tipo3 = ("Vodka con el nombre de {}, su grado de alcohol es {} y pais de origen {}") 
        print(tipo3.format(self.nombre, self.grado, self.origen)) 

    def tipo4(self):
        tipo4 = ("Bebida de tipo {} con sabores como: {} y viene en 2 presentaciones de {}") 
        print(tipo4.format(self.nombre, self.grado, self.origen)) 

    def presentacion(self):
        presentacion = ("Hola, me presento soy {} el bartender, cual bebida desea tomar, bebida normal o alcoholica como: {}, {}") 
        print(presentacion.format(self.nombre, self.grado, self.origen)) 

def menu():
	os.system('cls')
	print ("Hola, me presento soy Tarek el bartender, cual bebida desea tomar")
	print ("\t")
	print ("\t>>1 - Ron")
	print ("\t>>2 - Whisky")
	print ("\t>>3 - Vodka")
	print ("\t>>4 - Jugo")
	print ("\t")
	print ("\t9 - irse de la barra")
 
 
while True:
	menu()
 
	opcionMenu = input("Elige tu bebida >> ")
 
	if opcionMenu=="1":
		print ("")
		input("Has elegido tomar Ron...\n")
		ron = Bebida("Cacique Leyenda", "40", "Venezuela")
		ron.tipo1()
		input("") 
		input("presiona una tecla para volver a la barra")
	elif opcionMenu=="2":
		print ("")
		input("Has elegido tomar Whisky...\n")
		whisky = Bebida("Old Parr 12 años", "40", "Escocia") 
		whisky.tipo2()
		input("") 
		input("presiona una tecla para volver a la barra")	
	elif opcionMenu=="3":
		print ("")
		input("Has elegido tomar Vodka...\n")
		vodka = Bebida("Grey Goose", "40", "Francia")
		vodka.tipo3()
		input("") 
		input("presiona una tecla para volver a la barra")
	elif opcionMenu=="4":
		print ("")
		input("Has elegido tomar Jugo...\n")
		jugo = Bebida("Jugo", "Manzana", "Carton o Vidrio")
		jugo.tipo4()
		input("") 
		input("presiona una tecla para volver a la barra")
	elif opcionMenu=="9":

		break
	else:
		print ("")
		input("No has elegido la opción de bebida correcta!...\npresiona una tecla para volver a la barra")




