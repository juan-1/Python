pila=[]
paquetes=0
print("Sistema de almacen")
while True:
	conta=0
	print("Menú")
	print("1 para ingresar paquetes")
	print("2 para extraer paquetes")
	print("3 ver total de paquetes")
	print("4 ver pila de inventario")
	print("0 salir")
	select=input("# ")
	if(select=='1'):
		#ingresa paquetes
		dia=input("Día: ")
		paquetes=int(input("Número de paquetes: "))
		costo=float(input("Costo de paquetes: "))
		while(conta < paquetes):
			pila.append([dia, paquetes, costo])
			conta+=1
	if(select=='2'):
		#extraer paquetes
		paquetes=int(input("Número de paquetes vendidos: "))
		total=len(pila)
		if(total >= paquetes):
			while(conta < paquetes):
				pila.pop()
				conta+=1
		else:
			print("elementos insuficientes")		
	if(select == '3'):
		total=len(pila)
		print("Quedan ", total, " paquetes")
	if(select == '4'):
		print(pila)
	if(select == '0'):
		break
