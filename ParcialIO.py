p = 0
w = 0
Lq = 0
tasaLlegada = 0
tasaservicio = 0
opc = 0
bucle = True

while bucle==True:
    opc = input("---Menu---\n1.Ingresar datos.\n2.Calcular utilizacion del servidor.\n3.Calcular Tiempo de Espera promedio.\n4.Calcular longitud de la cola.\n0.Salir\nSeleccione: ")
    print(opc)
    if opc == 1:
        print("ha seleccionado ingresar datos")
        tasaLlegada = input("ingrese la tasa de llegada al servidor: ") 
        tasaservicio = input("ingrese la tasa de servicio del servidor ")
    elif opc == 2:
        print("ha seleccionado Calcular utilizacion del servidor")
        p = tasaLlegada/tasaservicio
        print("la utilizacion el servirdor es:" + p)
        if p >= 1:
            print("el servidor Esta congestionado")
        elif p >= 0.8:
            print("el servidor se esta congestionando")
        elif p <= 0.7:
            print("el servidor esta en sin congestion")
        else:
            print("Error, la utilizacion del servidor es menor que 0")
    elif opc == 3:
        print("ha seleccionado Calcular tiempo de espera promedio")
        w = 1/(tasaservicio-tasaLlegada)
        print("el Tiempo de espera promedio es de: " + w)
    elif opc == 4:
        print("ha seleccionado Calcular longitud de la cola")
        Lq = tasaLlegada*w
        print("La longitud de la cola es de: "+ Lq)
    elif opc == 0:
        print("Saliendo...")
        bucle = False 
        break
    #else:
        print("error de seleccion")
