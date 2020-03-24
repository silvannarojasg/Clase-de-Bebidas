class REGISTRO():   
  def __init__(self):     #Se declara el registro y sus variables
    self.dia = 0   
    self.mes = 0     
    self.año = 0
    self.nombre = ""     
    self.apellido = "" 
    self.pais = 0  
    self.sexo = ""  
    self.edad = 0
#REGISTRO DE DATOS

#VARIABLES
confirmadosM = 0
confirmadosF = 0
recuperadosM = 0
recuperadosF = 0
fallecidosM = 0
fallecidosF = 0
descartadosM = 0
descartadosF = 0

confirmados_italia = 0
recuperados_italia = 0
fallecidos_italia = 0
descartados_italia = 0

confirmados_chile = 0
recuperados_chile = 0
fallecidos_chile = 0
descartados_chile = 0

confirmados_colombia = 0
recuperados_colombia = 0
fallecidos_colombia = 0
descartados_colombia = 0

confirmados_mexico = 0
recuperados_mexico = 0
fallecidos_mexico = 0
descartados_mexico = 0

confirmados_peru = 0
recuperados_peru = 0
fallecidos_peru = 0
descartados_peru = 0

fiebre = ""
tos = ""
difRespirar= ""
congNasal = ""
dolorgarg = ""
diarrea = ""
dolorCab = ""
dolorMusc = ""

covid_19 = ""
edadMax_fallecidos = 0
edadMin_fallecidos = 200
nomb_min_fallecido = ""
nomb_max_fallecido = ""
apellido_min_fallecido = ""
apellido_max_fallecido = ""

nomb_max_descartado = ""
nomb_min_descartado = ""
apellido_max_descartado = ""
apellido_min_descartado = ""
edadMin_descartado = 200
edadMax_descartado = 0

nomb_max_covid = ""
nomb_min_covid = ""
apellido_min_covid = ""
apellido_max_covid = ""
edadMin_covid = 200
edadMax_covid = 0
Paciente = 0
fallecidos = 0
recuperados = 0
confirmados = 0
descartados = 0
descartado = 0
opcion = 0
opcion3 = 0
datos = REGISTRO()

while (opcion != 3):
	print ("\t\t===> MENU PRINCIPAL <===\n\n")
	print ("\t\t\t[1]. Registro.")
	print ("\t\t\t[2]. Reportes.")			#SE ELIGE UNA OPCION DEL MENU
	print ("\t\t\t[3]. SALIR.")


	opcion3 = 0
	Paciente = 0
	fiebre = ""
	tos = ""
	difRespirar= "" #VARIABLE INICIALIZADAS
	congNasal = ""
	dolorgarg = ""
	diarrea = ""
	dolorCab = ""
	dolorMusc = ""

	covid_19 = ""

	opcion = int(input("\t\t Elige una opcion: "))
	#Si la opcion es igual 1 entonces procedera a solicitar los datos
	if (opcion == 1):
		print("==================================================\n")
		datos.nombre = input("\nIndique su nombre: ")
		print("==================================================\n")
		datos.apellido = input("\nIndique su apellido: ")
		print("==================================================\n")
		print("\nA continuacion ingresara su fecha de nacimiento en orden: \n")
		datos.dia = input("Dia: ")
		datos.mes = input("Mes: ")
		datos.año = input("Año: ")
		print("==================================================\n")
		print ("\n1-Italia.\n2-Chile.\n3-Colombia.\n4-Mexico.\n5-Peru.")
		datos.pais = input("\nSeleccione pais de residencia: ")
		print("==================================================\n")
		datos.edad = int(input("\nIndique su edad: "))
		print("==================================================\n")
		datos.sexo = input("\nIndique su genero F/M: ")
		print("==================================================\n")
	#Se solicitan los datos personales...

	#Se pregunta acerca de los sintomas que posee cada persona...
		print("\nA continuacion responda las siguientes preguntas acerca de los sintomas: \n")
		print("==================================================\n")
		fiebre = input("Tiene sintomas de fiebre? S/N: \n")
		print("==================================================\n")
		tos = input("Tiene sintomas de tos? S/N: \n")
		print("==================================================\n")
		difRespirar = input("Ha tenido problemas o dificultad para respirar? S/N: \n")
		print("==================================================\n")
		congNasal = input("Ha tenido congestion nasal? S/N: \n")
		print("==================================================\n")
		dolorgarg = input("Ha tenido dolor de garganta? S/N: \n")
		print("==================================================\n")
		diarrea = input("Ha tenido diarrea? S/N: \n")
		print("==================================================\n")
		dolorCab = input("Ha tenido dolor de cabeza? S/N: \n")
		print("==================================================\n")
		dolorMusc = input("Ha tenido dolores musculares? S/N: \n")
		print("==================================================\n")


		'''Aqui se hace una comparacion MUY detallada, para saber
		que virus posee dependiendo de sus sintomas'''

		'''Para resumir, si entre sus sintomas tiene dificultad para respirar
		es muy probable que sea portador del COVID-19'''
		if (fiebre == "s" or fiebre == "S"):
			if (tos == "s" or tos == "S"):
				if (difRespirar == "s" or difRespirar == "S"):
					if (congNasal =="s" or congNasal == "S"):
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
					else:
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
				else:
					if (congNasal == "s" or congNasal == "S"):
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
					else:
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
			else:
				if (difRespirar == "s" or difRespirar == "S"):
					if (congNasal =="s" or congNasal == "S"):
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
					else:
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
				else:
					if (congNasal == "s" or congNasal == "S"):
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
					else:
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
		else:
			if (tos == "s" or tos == "S"):
				if (difRespirar == "s" or difRespirar == "S"):
					if (congNasal =="s" or congNasal == "S"):
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
					else:
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
				else:
					if (congNasal == "s" or congNasal == "S"):
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
					else:
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
			else:
				if (difRespirar == "s" or difRespirar == "S"):
					if (congNasal =="s" or congNasal == "S"):
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
					else:
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
										#Si tiene todos los sintomas, dara positivo para COVID-19
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
										#Es descartado si se trata de otro virus diferente al COVID-19
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA COVID-19. <-----\n")
										covid_19 = "s"
										Paciente = input("\nPaciente: \n1- Estable. \n2- Fallecido.\n")
				else:
					if (congNasal == "s" or congNasal == "S"):
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
					else:
						if (dolorgarg == "s" or dolorgarg == "S"):
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
						else:
							if (diarrea == "s" or diarrea == "S"):
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA RESFRIADO COMUN. <-----\n")
										descartado = "s"
							else:
								if (dolorCab == "s" or dolorCab == "S"):
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
									else:
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
								else:
									if (dolorMusc == "s" or dolorMusc == "S"):
										print("\n-----> POSITIVO PARA GRIPE DE TIPO A O B. <-----\n")
										descartado = "s"
							

		'''Aqui termina la comparacion de los sintomas y empieza 
		la asignacion de cada variable que sera mostrada en los reportes'''

		#Para los reportes mundiales
		if (covid_19 == "s"):
			confirmados += 1
			if (datos.sexo == "f" or datos.sexo =="F"):
				confirmadosF += 1 
			else:
				confirmadosM += 1

			if (Paciente == "1"):
				recuperados += 1
				if (datos.sexo == "f" or datos.sexo =="F"):
					recuperadosF += 1
				else:
					recuperadosM += 1
			else:
				fallecidos += 1
				if (datos.sexo == "f" or datos.sexo =="F"):
					fallecidosF += 1
				else:
					fallecidosM += 1

		else:
			if (descartado == "s"):
				descartados += 1
				if (datos.sexo == "f" or datos.sexo =="F"):
					descartadosF += 1
				else:
					descartadosM += 1

		#Para los casos por paises
		#ITALIA
		if (covid_19 == "s" and datos.pais == "1"):
			confirmados_italia += 1

			if (Paciente == "1"):
				recuperados_italia += 1
			else:
				fallecidos_italia += 1
		else:
			if (descartado == "s" and datos.pais == "1"):
				descartados_italia += 1
		#CHILE
		if (covid_19 == "s" and datos.pais == "2"):
			confirmados_chile += 1

			if (Paciente == "1"):
				recuperados_chile += 1
			else:
				fallecidos_chile += 1
		else:
			if (descartado == "s" and datos.pais == "2"):
				descartados_chile += 1
		#COLOMBIA
		if (covid_19 == "s" and datos.pais == "3"):
			confirmados_colombia += 1

			if (Paciente == "1"):
				recuperados_colombia += 1
			else:
				fallecidos_colombia += 1
		else:
			if (descartado == "s" and datos.pais == "3"):
				descartados_colombia += 1
		#MEXICO
		if (covid_19 == "s" and datos.pais == "4"):
			confirmados_mexico += 1

			if (Paciente == "1"):
				recuperados_mexico += 1
			else:
				fallecidos_mexico += 1
		else:
			if (descartado == "s" and datos.pais == "4"):
				descartados_mexico += 1
		#PERU
		if (covid_19 == "s" and datos.pais == "5"):
			confirmados_italia += 1

			if (Paciente == "1"):
				recuperados_peru += 1
			else:
				fallecidos_peru += 1
		else:
			if (descartado == "s" and datos.pais == "5"):
				descartados_peru += 1


		#Persona de mayor y menor edad
		'''Si la variable que contiene la edad, es menor que la edad minima (200)
		entonces la edad minima ahora sera la edad del registrado y asi se comparara
		las veces necesarias durante el ciclo'''
		if (covid_19 == "s"):
			if (datos.edad <= edadMin_covid):
				edadMin_covid = datos.edad
				nomb_min_covid = datos.nombre
				apellido_min_covid = datos.apellido
			
			if (datos.edad > edadMax_covid):
				edadMax_covid = datos.edad
				nomb_max_covid = datos.nombre
				apellido_max_covid = datos.apellido

		else:
			if (datos.edad <= edadMin_descartado):
				edadMin_descartado = datos.edad
				nomb_min_descartado = datos.nombre
				apellido_min_descartado = datos.apellido
			 
			if (datos.edad > edadMax_descartado):
				edadMax_descartado = datos.edad
				nomb_max_descartado = datos.nombre
				apellido_max_descartado = datos.apellido

		if (Paciente == "2"):
			if (datos.edad <= edadMin_fallecidos):
				edadMin_fallecidos = datos.edad
				nomb_min_fallecido = datos.nombre
				apellido_max_fallecido = datos.apellido
			
			if (datos.edad > edadMax_fallecidos):
				edadMax_fallecidos = datos.edad
				nomb_max_fallecido = datos.nombre
				apellido_max_fallecido = datos.apellido



	
	if (opcion == 2):
		while (opcion3 != 3):
			print("\n\t\t===>MENU DE REPORTES<===\n")
			print ("\t\t[1]. Cantidad de infectados, recuperados y fallecidos.")
			print ("\t\t[2]. Datos de mayor y menor edad registrados hasta ahora.")
			print ("\t\t[3]. VOLVER")
			opcion3 = int(input("\t\tElige una opcion: \n"))

			if (opcion3 == 1):
				print("\nCantidad de casos generales:")
				print("==================================================\n")
				print("Infectados: ",confirmados)
				print("Femeninas: ", confirmadosF)
				print("Masculino: ", confirmadosM)
				print("==================================================\n")
				print("\nRecuperados: ", recuperados)		#Se muestra informacion general de casos, por genero
				print("Femeninas: ", recuperadosF)			#Y por paises
				print("Masculino: ", recuperadosM)
				print("==================================================\n")
				print("\nFallecidos: ", fallecidos)
				print("Femeninas: ", fallecidosF)
				print("Masculino: ", fallecidosM)
				print("==================================================\n")
				print("\nDescartados: ", descartados)
				print("Femeninas: ", descartadosF)
				print("Masculino: ", descartadosM)
				print("==================================================\n")

				print("\nCantidad de casos por paises:\n")
				print("==================================================\n")
				print("\nITALIA:\n")
				print("Infectados: ",confirmados_italia)
				print("Recuperados: ", recuperados_italia)
				print("Fallecidos: ", fallecidos_italia)
				print("Descartados: ", descartados_italia)
				print("==================================================\n")
				print("\nCHILE: \n")
				print("Infectados: ",confirmados_chile)
				print("Recuperados: ", recuperados_chile)
				print("Fallecidos: ", fallecidos_chile)
				print("Descartados: ", descartados_chile)
				print("==================================================\n")

				print("\nCOLOMBIA: \n")
				print("Infectados: ",confirmados_colombia)
				print("Recuperados: ", recuperados_colombia)
				print("Fallecidos: ", fallecidos_colombia)
				print("Descartados: ", descartados_colombia)
				print("==================================================\n")

				print("\nMEXICO: \n")
				print("Infectados: ",confirmados_mexico)
				print("Recuperados: ", recuperados_mexico)
				print("Fallecidos: ", fallecidos_mexico)
				print("Descartados: ", descartados_mexico)
				print("==================================================\n")

				print("\nPERU: \n")
				print("Infectados: ",confirmados_peru)
				print("Recuperados: ", recuperados_peru)
				print("Fallecidos: ", fallecidos_peru)
				print("Descartados: ", descartados_peru)
				print("==================================================\n")

			if (opcion3 == 2):
				print("==================================================\n")
				print ("\nDatos del infectado de menor edad: \n")
				print("Nombre: ",nomb_min_covid, apellido_min_covid)
				print("Edad: ", edadMin_covid)
				print("==================================================\n")

				print("\nDatos del infectado de mayor edad: \n")
				print("Nombre: ",nomb_max_covid, apellido_max_covid)
				print("Edad: ", edadMax_covid)										#Aqui se muestran los resultados de 
				print("==================================================\n")	
																					#Los registrados con menor y mayor edad
				print("\nDatos del descartado de menor edad: \n")					#Para cada caso
				print("Nombre: ",nomb_min_descartado, apellido_min_descartado)
				print("Edad: ", edadMin_descartado)
				print("==================================================\n")

				print("\nDatos del descartado de mayor edad: \n")
				print("Nombre: ",nomb_max_descartado, apellido_max_descartado)
				print("Edad: ", edadMax_descartado)
				print("==================================================\n")

				print("\nDatos del fallecido de menor edad: \n")
				print("\nNombre: ",nomb_min_fallecido, apellido_min_fallecido)
				print("\nEdad: ", edadMin_fallecidos)
				print("==================================================\n")
				print("\nDatos del fallecido de mayor edad: \n")
				print("\nNombre: ", nomb_max_fallecido, apellido_max_fallecido)
				print("\nEdad: ", edadMax_fallecidos)
				print("==================================================\n")


		