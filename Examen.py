import os

# diccionarios
diccionarioClientes = {}
diccionarioProyectos = {}
diccionarioDepartamentos = {}

# variables declaradas
opcionSeleccionada = "0"


def limpiarPantalla():  # Metodo para limpiar la pantalla
    print(" " * 25000000)


def pausarPantalla():  # Metodo para pausar la pantalla
    print("")
    print("\t\t\t\t\t", end="")
    os.system("pause")


def insertarDatosClientesProyectos():  # Metodo para ingreso de datos de clientes y proyectos
    listadoTemporal = [];
    listadoDeOpcionClientes = ("NOMBRE", "APELLIDO", "TELEFONO", "DIRECCION")
    listadoDeOpcionProyectos = ("NOMBRE", "FECHA", "DIRECCION", "ESTADO")
    if opcionInsertar == "clientes":
        codigoCliente = (input("\t\t\t\tINSERTE EL CODIGO DEL CLIENTE: "))
        for x in range(4):
            informacionCliente = str(input("\t\t\t\tINSERTE EL " + listadoDeOpcionClientes[x] + " DEL CLIENTE: "))
            listadoTemporal.append(informacionCliente)
        diccionarioTemporal = {codigoCliente: listadoTemporal}
        diccionarioClientes.update(diccionarioTemporal)
    elif opcionInsertar == "proyectos":
        impresionDeRegistros()
        if 0 != len(diccionarioClientes):
            print("")
            codigoProyecto = (input("\t\t\t\tINSERTE EL CODIGO DEL PROYECTO: "))
            codigoCliente = (input("\t\t\t\tINSERTE EL CODIGO DEL CLIENTE: "))
            listadoTemporal.append(
                str(diccionarioClientes[codigoCliente][0]) + " " + (diccionarioClientes[codigoCliente][1]))
            for x in range(4):
                infoProyect = str(input("\t\t\t\tINSERTE EL " + listadoDeOpcionProyectos[x] + " DEL PROYECTO: "))
                listadoTemporal.append(infoProyect)
            diccionarioTemporal = {codigoProyecto: listadoTemporal}
            diccionarioProyectos.update(diccionarioTemporal)


def ingresarDepartamentosMunicipios(): # Metodo para registro de Departamentos y sus Municipios
    if opcionDepartamentoCiudad == "departamento":
        nombreDelDepartamento = str(input("\t\t\t\tINGRESE EL NOMBRE DEL DEPARTAMENTO: "))
        diccionarioDepartamentos.update({nombreDelDepartamento: []})
    if opcionDepartamentoCiudad == "municipios":
        impresionDeRegistros()
        if 0 != len(diccionarioDepartamentos):
            nombreDelDepartamento = str(input("\t\t\t\tINGRESE EL NOMBRE DEL DEPARTAMENTO: "))
            nombreDeCiudad = str(input("\t\t\t\tINGRESE EL NOMBRE DEL MUNICIPIO: "))
            diccionarioDepartamentos[nombreDelDepartamento].append(nombreDeCiudad)


def impresionDeRegistros():  # Metodo para la impresion de todos los registros
    def impresionClientes():  # Metodo de impresion de clientes
        print("");
        print("\t\t\t", customer.ljust(20, " "), end="")
        for x in range(4):
            print(diccionarioClientes[customer][x].ljust(20, " "), end="")

    def impresionProyectos():  # Metodo de impresion de proyectos
        print("");
        print("\t\t\t", customer.ljust(20, " "), end="")
        for x in range(5):
            print(diccionarioProyectos[customer][x].ljust(20, " "), end="")

    if opcionImprimir == "clientes": # Impresion de clientes
        print("\t\t\t" + "CODIGO".ljust(20, " ") + "NOMBRES".ljust(20, " ") + "APELLIDOS".ljust(20," ") + "NO. TELEFONO".ljust(20, " ") + "DIRECCION".ljust(20, " "))
        contador1 = 2
        contador2 = 2
        for customer in diccionarioClientes:
            contador1 = contador1 + 1
            if opcionImprimir == "clientes":
                contador1 = 0
                impresionClientes()
            else:
                contador2 = contador2 + 1
        if contador1 == contador2:
            print("");
            print("\t\t\tNO SE ENCONTRO NINGUN CLIENTE")
    elif opcionImprimir == "proyectos": # Impresion de Proyectos
        print(
            "\t\t\t" + "CODIGO".ljust(20, " ") + "CLIENTE".ljust(20, " ") + "NOMBRE".ljust(20, " ") + "FECHA".ljust(20, " ") + "DIRECCION".ljust(20, " ") + "ESTADO".ljust(20, " "))
        contador1 = 2
        contador2 = 2
        for customer in diccionarioProyectos:
            contador1 = contador1 + 1
            if opcionDeBuscar == "proyectos":
                contador1 = 0
                impresionProyectos()
            elif opcionDeBuscar == diccionarioProyectos[customer][0]:
                impresionProyectos()
            else:
                contador2 = contador2 + 1
        if contador1 == contador2:
            print("");
            print("\t\t\tNO SE ENCONTRO NINGUN PROYECTO")
    elif opcionImprimir == "departamentos": # impresion de departamentos
        contador1 = 1
        contador2 = 1
        cursor = 0
        for departament in diccionarioDepartamentos:
            cursor += 1
            contador1 = contador1 + 1
            if opcionImprimir == "departamentos":
                contador1 = 0
                print("\t\t\t", cursor, departament.ljust(20, " "))
            else:
                contador2 = contador2 + 1
        if contador1 == contador2:
            print("");
            print("\t\t\tNO SE ENCONTRO NINGUN DEPARTAMENTO")
    elif opcionImprimir == "municipios": # Impresion de Municipios
        contador1 = 1
        contador2 = 1
        cursor = 0
        for departament in diccionarioDepartamentos:
            cursor += 1
            contador1 = contador1 + 1
            if opcionImprimir == "municipios":
                contador1 = 0
                print("");
                print("\t\t\t", cursor, departament, ":  ", end="")
                for town in diccionarioDepartamentos[departament]:
                    print(town + ";  ", end="")
            else:
                contador2 = contador2 + 1
        if contador1 == contador2:
            print("");
            print("\t\t\tNO SE ENCONTRO NINGUN DEPARTAMENTO")


def menuDelSistema(): # Metodo del menu principal del sistema
    print("\t\t\t\t1) INGRESAR DATOS DE UN CLIENTE")
    print("\t\t\t\t2) VISUALIZAR INFORMACION DEL CLIENTE")
    print("\t\t\t\t3) INGRESAR DATOS DE UN PROYECTO")
    print("\t\t\t\t4) VISUALIZAR INFORMACION DEL PROYECTO")
    print("\t\t\t\t5) BUSCAR PROYECTOS DE UN CLIENTE")
    print("\t\t\t\t6) INGRESO DE DEPARTAMENTOS Y MUNICIPIOS")
    print("\t\t\t\t7) SALIDA DEL MENU")


def menuDelDepartamento(): # Metodo del menu secundario
    print("\t\t\t\t1) INGRESAR UN DEPARTAMENTO")
    print("\t\t\t\t2) INGRESAR UN MUNICIPIO")
    print("\t\t\t\t3) MOSTRAR DEPARTAMENTOS Y MUNICIPIOS")
    print("\t\t\t\t4) SALIDA DEL MENU")


while str(opcionSeleccionada) != "7": # switch
    opcionImprimir = "NADA"
    limpiarPantalla()
    opcionSeleccionada = "0"  # SE DECLARA NUEVAMENTE POR LAS OPCIONES DE ENCABEZADO
    menuDelSistema()
    opcionSeleccionada = str(input("\t\t\t\t\tINGRESE UNA OPCION: "))  # MENU DE OPCIONES
    if (str(opcionSeleccionada) == "1"): # INGRESAR DATOS DE UN CLIENTE
        limpiarPantalla()
        opcionInsertar = "clientes"
        insertarDatosClientesProyectos()
        pausarPantalla()
    elif str(opcionSeleccionada) == "2": # VISUALIZAR INFORMACION DEL CLIENTE
        limpiarPantalla()
        opcionImprimir = "clientes"
        impresionDeRegistros()
        pausarPantalla()
    elif str(opcionSeleccionada) == "3": # INGRESAR DATOS DE UN PROYECTO
        limpiarPantalla()
        opcionInsertar = "proyectos"
        opcionImprimir = "clientes"
        insertarDatosClientesProyectos()
        pausarPantalla()
    elif str(opcionSeleccionada) == "4": # VISUALIZAR INFORMACION DEL PROYECTO
        limpiarPantalla()
        opcionImprimir = "proyectos"
        opcionDeBuscar = "proyectos"
        impresionDeRegistros()
        pausarPantalla()
    elif str(opcionSeleccionada) == "5": # BUSCAR PROYECTOS DE UN CLIENTE
        limpiarPantalla()
        opcionImprimir = "proyectos"
        opcionDeBuscar = str(input("\t\t\t\tINGRESE EL NOMBRE DEL CLIENTE: "))
        impresionDeRegistros()
        pausarPantalla()
    elif str(opcionSeleccionada) == "6": # INGRESO DE DEPARTAMENTOS Y MUNICIPIOS
        limpiarPantalla()
        opcionSeleccionada2 = 0
        while str(opcionSeleccionada2) != "4":
            opcionSeleccionada2 = 0
            limpiarPantalla()
            menuDelDepartamento()
            opcionSeleccionada2 = str(input("\t\t\t\t\tINSERTE UNA OPCION: "))
            if (str(opcionSeleccionada2) == "1"): # INGRESAR UN DEPARTAMENTO
                limpiarPantalla()
                opcionDepartamentoCiudad = "departamento"
                ingresarDepartamentosMunicipios()
                pausarPantalla()
            elif (str(opcionSeleccionada2) == "2"): # INGRESAR UN MUNICIPIO
                limpiarPantalla()
                opcionImprimir = "departamentos"
                opcionDepartamentoCiudad = "municipios"
                ingresarDepartamentosMunicipios()
                pausarPantalla()
            elif (str(opcionSeleccionada2) == "3"): # MOSTRAR DEPARTAMENTOS Y MUNICIPIOS
                limpiarPantalla()
                opcionImprimir = "municipios"
                impresionDeRegistros()
                pausarPantalla()
            elif str(opcionSeleccionada2) == "4": # SALIDA DEL MENU
                print("")
                print("\t\t\t\t\tREGRESANDO AL MENU PRINCIPAL")
            else:
                print("\t\t\t\t\tPOR FAVOR INGRESE UN VALOR CORRECTO")
                pausarPantalla()
        pausarPantalla()
    elif str(opcionSeleccionada) == "7": # SALIDA DEL MENU
        print("")
        print("\t\t\t\t\tGRACIAS POR UTILIZAR EL PROGRAMA")
        pausarPantalla()
    else:
        print("\t\t\t\t\tPOR FAVOR INGRESE UN VALOR CORRECTO")
        pausarPantalla()
