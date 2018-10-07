"""
programa que convierte decimales a punto flotante y de punto flotante a decimal...
"""

print("\tPROGRAMA QUE DADO UN NUMERO EN BASE 10 EN PUNTO DECIMAL\n\tOBTIENE SU REPRESENTACION EN PUNTO FLOTANTE DE SIMPLE PRECISION")
print("\n\n\t1 ====> Pasar de base 10 a flotante de simple precision")
print("\t2 ====> Pasar de flotante de simple precision a base 10\n\n")
opcion=input("Elige una opcion: ")
if(opcion == '1'):

	print("\n\nSi tu numero es entero, ingresalo del siguiente modo:\nn.0: donde n es el numero entero")
	numero=input("\n\ningresa el numero de punto decimal a convertir a binario: ")
	list(numero)
	punto=numero.index(".")#se busca la posicion del punto decimal
	parte_entera=numero[:punto]#se toman todos los numeros antes del punto
	parte_decimal=numero[punto+1:]#se toman todos los numeros despues del punto
	def signo (parte_entera):#funcion para definir el signo del numero en binaro
		signo_numero=[]
		if(parte_entera[0] == '-'):
			signo_numero.append('1')
		else:
			signo_numero.append('0')
		return(signo_numero)

	def entero_decimal(parte_entera):#funcion para convertir un numero entero a binario
		binario=[]
		if(parte_entera =='0'):#si el primer elemento es cero  en binario tambien es cero
			binario.append('0')
		else:
			decimal=int(parte_entera)#convertir la cadena parte_entera a un numero entero
			if(decimal < 0):#por si es un numero negativo
				decimal*=-1
			if(decimal == 0):#por si el decimal es un cero 
				binario.append('0')
			while(decimal > 0):#se convierte a binario 
				residuo=int(decimal % 2) #modulo??
				binario.append(str(residuo))
				decimal=int(decimal/2)
		binario.reverse()#se invierte el orden de la lista binario
		return(binario)
	def fraccion_binario(parte_decimal):#funcion para convertir la parte fraccionaria a binario
		cero_punto='0.'#cadena que sirve para agregarla a la parte_decimal
		cero_punto=cero_punto+parte_decimal
		binario2=[]
		elementos=len(parte_decimal)
		contador=0
		todosceros=0
		while (contador < elementos):
			if (parte_decimal[contador] != '0'):
				todosceros=1
			contador+=1
		if(parte_decimal == '0'):#si la parte fraccionaria es un cero
			binario2.append('0')
		elif(todosceros == 0):
			binario2.append('0')
		else:
			decimal=float(cero_punto)#se convierte la cadena cero_punto a un flotante
			while(decimal != 1):#se convierte la parte fraccionaria a binario
				decimal=abs(decimal)-abs(int(decimal))#para solo obtener la parte decimal del numero
				decimal*=2
				factor=int(decimal)
				binario2.append(str(factor))
		return(binario2)
	def exceso(elementos):#funcion para determinar el exponente del numero
		exponente=[]
		elementos-=1
		exp=127+elementos#el exceso es a 127 por ello se le suma el numero de lugares que tuvo que recorrerse el punto
		str(exp)
		exponente=entero_decimal(exp)#se convierte el numero exp a binario
		return(exponente)
	def agregar_ceros(completar):#funcion para agregar los ceros faltantes al numero y que quede de 32 bits
		contador=0
		ceros=[]
		agrega=32-completar
		while (contador < agrega):
			ceros.append('0')
			contador+=1
		return(ceros)

	dec_convert="".join(entero_decimal(parte_entera))#convierte a cadena lo que se recibio de la funcion entero_decimal
	dec_convert2="".join(fraccion_binario(parte_decimal))#convierte en cadena lo que se recibio de la funcion fraccion_binario
	elementos=len(dec_convert)#obtiene el numero de elementos de la cadena 
	exponente="".join(exceso(elementos))#convierte a cadena lo recibido por la funcion exceso
	signo="".join(signo(parte_entera))#convierte a cadena lo recibido por la funcion signo
	punto_flotante=signo+exponente+dec_convert+dec_convert2#concatenacion
	completar=len(punto_flotante)#obtiene el numero de elementos de la cadena 
	ceros="".join(agregar_ceros(completar))#convierte a cadena lo que se recibio de la funcion agregar_ceros
	punto_flotante_simple_precision= punto_flotante+ceros#concatenacion
	precision=len(punto_flotante_simple_precision)#obtiene el numero de elementos de la cadena 
	if(precision > 32):#si el numero resulto ser mayor de 32 bits se muestra pero se indica que ya no es de simple precision
		print("\n\nLa representacion de tu numero en punto flotante es: ")
		print("\n\n",punto_flotante_simple_precision)
		print("\nPero ya no es de simple precision...!!")
	else:
		print("\n\nLa representacion de tu numero en punto flotante de simple precision es: ")
		print("\n\n",punto_flotante_simple_precision)
	salir=input("\n\n\n\npresiona una tecla para salir!!")#mantiene en espera la consola
elif(opcion == '2'):
	print("\n\nDebe ser un numero de 32 bits!!")
	numero=input("\nIngresa tu numero flotante de simple precision:\n\n")
	#numero=list(numero)
	bits=len(numero)#si el numero no es exactamente de 32 bits no se continua
	if(bits > 32 or bits < 32):
		print("\n\nNumero invalido!!")
		print("\nDebe ser un numero de 32 bits!!")
	else:
		signo=numero[0]#se determina el signo del numero
		if(signo == '1'):#el numero es negativo
			signo_decimal='-'
		else:
			signo_decimal='+'
		exponente=numero[1:9]#se obtiene la parte del exponente
		mantisa=numero[9:32]#se obtiene la parte de la mantisa
		def binario_decimal(binario):#funcion para convertir de binario a numero decimal 
			binario_lista=list(binario)
			elemento=len(binario_lista)
			decimal=0
			operando=1
			elemento-=1
			while (elemento >= 0):
				if(binario_lista[elemento]=='1'):
					decimal+=operando
				operando*=2
				elemento-=1
			return(decimal)
		def fraccion_decimal(fraccion):#funcion para pasar de binario a parte fraccionaria de un numero 
			fraccion_lista=list(fraccion)
			elemento=len(fraccion_lista)
			decimal=0
			operando=0
			elemento-=1
			contador=0
			n=-1
			while(contador <= elemento):
				operando=2**n
				if(fraccion_lista[contador]=='1'):
					decimal+=operando
				n-=1
				contador+=1
			return(decimal)
		def partes_mantisa(mantisa, decimal):#funcion para determinar cual es la parte entera y cual la fraccionaria de la mantisa
			punto=decimal-127
			punto+=1
			maximo=len(mantisa)#se obtiene el numero de elementos de la mantisa
			parte_entera=mantisa[0:punto]#se determina cual es la parte entera
			parte_decimal=mantisa[punto:maximo]#se determina cual es la parte fraccionaria
			entero=binario_decimal(parte_entera)#se convierte la parte entera en binario a decimal
			fraccion=fraccion_decimal(parte_decimal)#se convierte la parte fraccionaria en binario a fraccion en decimal
			numero=entero+fraccion#Se suman ambas partes 
			return(numero)				
		exp_endecimal=binario_decimal(exponente)#se convierte el exponente en binario a decimal
		flotante=str(partes_mantisa(mantisa, exp_endecimal))#se convierte a cadena lo recibido por la funcion partes_mantisa
		numero_flotante=signo_decimal+flotante#concatenacion
		print("\n\n\tEn flotante de simple precision es: ", numero_flotante)
	salir=input("\n\n\n\npresiona una tecla para salir!!")#mantiene en espera la consola 
else:
	print("opcion invalida...!")
	salir=input("\n\n\n\npresiona una tecla para salir!!")#mantiene en espera la consola

