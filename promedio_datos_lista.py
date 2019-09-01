lista=[1,2,3]
conta=0
def sueldos_prom():
	while(True):
		print("desea calcular el promedio de sueldos?")
		continuar=int(input("ingrese 1 para continuar, ingrese 2 para terminar: "))
		if(continuar == 2):
			print("Bye...!")
			break
		def datos():
			global lista, conta	
			while(conta<3):
				print("¿Cuanto te gustaria ganar?")
				lista[conta]=int(input("compañero "+ str(conta+1) +": "))
				conta+=1
		def prom(lista):
			global conta
			promedio=0
			for i in lista:
				promedio=promedio+i
			print(promedio)
			promedio=promedio/conta
			print("el promedio es: ",promedio)
			conta=0
		datos()
		prom(lista)

sueldos_prom()