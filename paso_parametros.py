"""
PROGRAMA  SEIS DE LENGUAJES DE PROGRAMACION GRUPO: 4
"""
import string
from math import sqrt, atan
"""
El tipo de paso de parametros se hará por referencia
ya que es la forma en que se trabaja en python 
"""

def obten_lista(limite):
	conta=0
	lista=[]
	while conta < limite:
		elemento=input("ingresa el elemento "+str(conta+1)+": ")
		lista.append(elemento)
		conta+=1
	return(lista)

def invierte_lista(lista):
	lista.reverse()
	return(lista)
	
def distancias_angulos(lista):
	dis_ang=[]
	conta=0
	limite_inter=len(lista)
	while True:
		if conta == limite_inter-1:
			break
		x=lista[conta]
		coma=x.find(",")
		par_cierre=x.find(")")
		corx=float(x[1:coma])
		cory=float(x[coma+1:par_cierre])
		x2=lista[conta+1]
		coma=x2.find(",")
		par_cierre=x2.find(")")
		cor2x=float(x2[1:coma])
		cor2y=float(x2[coma+1:par_cierre])
		distancia=round(sqrt(((cor2x - corx)**2)+((cor2y - cory)**2)),2)
		try:
			angulo=round((atan((cor2y - cory)/(cor2x - corx)))*57.29577951,2)
		except ZeroDivisionError:
			angulo=90
		#angulo se multiplica por 57.2957.. para mostrar el resultado en GRADOS!!
		elem="Para los puntos "+x+" y "+str(x2)+" la distancia es: "+str(distancia)+" y su ángulo es: "+str(angulo)
		dis_ang.append(elem)
		conta+=1
	return(dis_ang)

def opcion(numero):
	if numero == '1':
		limite=int(input("Ingresa el numero de elementos de tu lista: "))
		lista=obten_lista(limite)
		invertida=invierte_lista(lista)
		print("La lista invertida es: ")
		for x in invertida:
			print(x, end="  ")
	elif numero == '2':
		limite=int(input("Ingresa el numero de puntos a calcular: "))
		if limite < 2:
			print("Para calcular distancia y ángulo, necesitamos por lo menos dos puntos..!")
		else:
			print("Los puntos deber ingresarse bajo el formato (x,y) (incluyendo los parentesis)")
			lista=obten_lista(limite)
			dis_ang=distancias_angulos(lista)
			for x in dis_ang:
				print(x)
	else:
		print("Opción invalida..!!")

def control():
	while True:
		print("\n 1 ==> Invertir una lista")
		print(" 2 ==> Obtener la distancia y ángulos de puntos en el plano")
		print(" 0 ==> salir")
		numero=input("Selecciona una opción: ")
		if numero == '0':
			break
		opcion(numero)

control()
