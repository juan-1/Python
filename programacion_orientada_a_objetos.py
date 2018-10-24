#Programa 8 LP

"""
Con este programa usando un lenguaje de programación orientada a objetos buscamos demostrar la forma en que se realiza 
la elección y el encadenamiento de constructores. El uso de los diferentes tipos de vista que provee el lenguaje. 
La forma en que se realiza la busqueda dinámica de métodos.
"""
"""
La clase vehiculos es la superclase de nuestro programa, sus atributos y métodos describen el comportamiento
de un vehiculo.
"""
class vehiculos():

	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
		self.__placas=True

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("marca: ", self.marca, "\nModelo:", self.modelo, "\nEn marcha: ",
			self.enmarcha, "\nacelerando: ", self.acelera, "\nFrenado: ", self.frena, "\nTraigo placas: ", self.__placas)

"""
La clase Furgoneta hereda de la clase vehiculos. Con ello la clase Furgoneta puede hacer uso de los métodos y
atributos de la clase vehiculos. Pero también se pueden agregar métodos propios de la clase Furgoneta.
"""
class Furgoneta(vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return("La furgoneta esta cargada")
		else:
			return("La furgoneta no esta cargada")
"""
En la clase Moto también se hereda de la clase vehiculos, se definen métodos propios de la clase, pero aqui 
podemos observar que se pueden sobre escribir métodos. Cuando se crea un objeto instanciado a la clase Moto
y este quisiera hacer uso del método estado cuando el interprete hiciera la busqueda dinámica de 
métodos usaria el método (estado) de la clase Moto, ya no haría uso del método (estado) de la
super clase vehiculos.
"""
class Moto(vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="voy haciendo el caballito"
	def estado(self):#sobre escritura de metodos
		print("marca: ", self.marca, "\nModelo:", self.modelo, "\nEn marcha: ",
			self.enmarcha, "\nacelerando: ", self.acelera, "\nFrenado: ", self.frena, "\n", self.hcaballito)

"""
En la clase Velectricos también se hereda de la clase vehiculos y se sobre escribio el método constructor, como ya se 
explico en la función anterior al tener un objeto instanciado a la clase Velectricos el interpetre usaria el
 método constructor definido en la clase Velectricos y no el de la super clase vehiculos, sin embargo como se
 ejemplifica en la clase Velectricos es posible usar el constructor de la super clase, pero se tiene que indicar
 explicitamente al interprete de python haciendo uso de super(), y asi se puede hacer uso de ambos métodos.
"""
class Velectricos(vehiculos):
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True
		print("Bateria cargada", self.cargando)



#creación de objetos instanciados a las clases definidas
print("\n\n...Creando Moto...\n\n")
miMoto=Moto("toyota", "4567")	
miMoto.caballito()	
miMoto.estado()

print("\n\n...Creando Furgoneta...\n\n")
miFurgoneta=Furgoneta("Renault", "king")
miFurgoneta.arrancar()
"""
Aqui se puede observar que se trata de cambiar el valor del atributo (__placas) de la clase Furgoneta
sin embargo al ejecutar se observa que dicho valor no cambia, esto se debe que en la clase original
vehiculos (__placas) se encapsulo, es decir esta variable es privada y no puede ser accedida fuera de la clase,
por ello aunque se trata de cambiar el valor, este permanece igual. En python para poner atributos de 
de forma privada, se debe hacer uso de dos guiones bajos (__).
Podriamos decir que el lenguaje python solo maneja dos tipos de vista, la publica y la privada.
"""
miFurgoneta.__placas=False
miFurgoneta.estado()
print(miFurgoneta.carga(True))

print("\n\n...Creando Carro eléctrico...\n\n")
coche_elec=Velectricos("Tesla", "alien")
coche_elec.estado()
coche_elec.cargarEnergia()
pausa=input("presiona una tecla para finalizar el programa...!")




