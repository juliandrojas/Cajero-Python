#Importamos módulo datetime para trabajar fechas
from datetime import datetime
#Lista para almacenar las cuentas bancarias
cuentasBancarias = []
#Lista para almacenar los movimientos de las cuentas bancarias
movimiento = []
#Datos de la cuenta bancaria
cedula = 0
edad = 0
nombre = "" 
apellidos = ""
contraseña = ""
#Saldo inicial de la cuenta 
saldoInicial = 0
#Saldo actual de la cuenta
saldoActual = 0
#Saldo que adicionamos a la cuenta
saldoAdicional = 0
#Saldo que restamos a la cuenta
saldoRestado = 0
#Saldo que debitamos de la cuenta para el préstamo
saldoDebitado = 0
#Saldo total que se debe
totalDeuda = 0
#Capturamos la fecha actual
fechaActual = datetime.now().date()
#Pasamos de YYYY-MM-DD a DD-MM-YYYY para saber cuando se abrió la cuenta
fechaApertura = fechaActual.strftime("%d-%m-%Y")
#Pasamos de YYYY-MM-DD a DD-MM-YYYY para saber cuando se depositó en una cuenta
fechaMovimiento = fechaActual.strftime("%d-%m-%Y")
#Métodos
#Opción 1: Crear cuenta
def crear_cuenta():
    cedula = input("Introduce el número de cédula: ")
    while not cedula.isdigit() or int(cedula) <= 0:
        print("Error: Debes ingresar números")
        cedula = input("Introduce el número de cédula: ")
        
    nombre = input("Introduce tu(s) nombre(s): ")
    while not nombre.isalpha():
        print("Error: Debes ingresar letras")
        nombre = input("Introduce tu(s) nombre(s): ")
        
    apellidos = input("Introduce tus apellidos: ")
    while not apellidos.isalpha():
        print("Error: Debes ingresar letras")
        apellidos = input("Introduce tu(s) apellido(s): ")
        
    edad = input("Introduce tu edad: ")
    while not edad.isdigit() or int(edad) <= 0:
        print("Error: Debes ingresar números")
        edad = input("Introduce tu edad: ")
        
    contraseña = input("Introduce tu contraseña: ")
    while not contraseña.isdigit() or len(contraseña) != 4:
        print("Error: La contraseña debe tener 4 números. Inténtalo de nuevo.")
        contraseña = input("Introduce tu contraseña: ")
        
    saldoInicial = input("Ingresa el saldo inicial de la cuenta (debe ser de 50000 o más): ")
    while not saldoInicial.isdigit() or int(saldoInicial) < 50000:
        print("Error: El saldo inicial debe ser de 50000 o más. Por favor, intenta nuevamente.")
        saldoInicial = input("Ingresa el saldo inicial de la cuenta: ")
        
    saldoActual = int(saldoInicial)
    fechaApertura = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    # Creamos la cuenta bancaria
    cuenta = [cedula, nombre, apellidos, edad, fechaApertura, contraseña, saldoActual]    
    cuentasBancarias.append(cuenta)  # Agregamos la cuenta a la lista de cuentasBancarias
    
    print("Cuenta creada con éxito!")
    print("Detalles de la cuenta creada:")
    print("Cédula:", cuenta[0])
    print("Nombre(s):", cuenta[1])
    print("Apellido(s):", cuenta[2])
    print("Edad:", cuenta[3])
    print("Fecha de apertura:", cuenta[4])
    print("Contraseña:", cuenta[5])
    print("Saldo actual:", cuenta[6])
#Opción 2: Realizar depósito
def realizar_deposito():
    cedula = input("Introduce el número de cédula: ")
    while not cedula.isdigit() or int(cedula) <= 0:
        print("Error: Debes ingresar números")
        cedula = input("Introduce el número de cédula: ")
        
    cuenta_encontrada = None
    # Buscamos la cuenta en cuentasBancarias
    for cuenta in cuentasBancarias:
        if cuenta[0] == cedula:
            cuenta_encontrada = cuenta
            break
    
    if cuenta_encontrada:
        print("Cuenta encontrada :D")
        print("Detalles de la cuenta encontrada:")
        print("Cédula:", cuenta_encontrada[0])
        print("Nombre(s):", cuenta_encontrada[1])
        print("Apellido(s):", cuenta_encontrada[2])
        print("Edad:", str(cuenta_encontrada[3]))
        print("Fecha de apertura:", str(cuenta_encontrada[4]))
        print("Contraseña:", cuenta_encontrada[5])
        print("Saldo actual:", cuenta_encontrada[6])
        
        saldoAdicional = input("Ingresa el monto que quieres depositar en tu cuenta: ")
        while not saldoAdicional.isdigit() or int(saldoAdicional) <= 0:
            print("Error: Debes ingresar un monto válido")
            saldoAdicional = input("Ingresa el monto que quieres depositar en tu cuenta: ")
        
        saldoAdicional = int(saldoAdicional)
        saldoActual = cuenta_encontrada[6] + saldoAdicional
        
        # Actualizamos el nuevo saldo actual en la lista "cuentasBancarias"
        cuenta_encontrada[6] = saldoActual
        
        # Registramos el movimiento en la cuenta
        fechaMovimiento = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        movimiento = (fechaMovimiento, 'depósito', saldoAdicional)
        cuenta_encontrada.append(movimiento)
        
        print("Saldo actualizado en la cuenta:", saldoActual)
        print("Fecha del movimiento:", fechaMovimiento)
    else:
        print("Cuenta no encontrada")
#Opción 3: Realizar retiro
def realizar_retiro():
    cedula = input("Introduce el número de cédula: ")
    while not cedula.isdigit() or int(cedula) <= 0:
        print("Error: Debes ingresar números")
        cedula = input("Introduce el número de cédula: ")
    
    existe = False
    cuenta_encontrada = None

    # Iteramos las cuentas
    for cuenta in cuentasBancarias:
        if cuenta[0] == cedula:
            existe = True
            cuenta_encontrada = cuenta
            break
    
    # Si existe, le retiramos saldo a la cuenta
    if existe:
        print("Cuenta encontrada :D")
        print("Detalles de la cuenta encontrada: ")
        print("Cédula: " + cuenta_encontrada[0])
        print("Nombre(s): " + cuenta_encontrada[1])
        print("Apellido(s): " + cuenta_encontrada[2])
        print("Edad: " + str(cuenta_encontrada[3]))
        print("Fecha de apertura: " + cuenta_encontrada[4])
        print("Contraseña: " + cuenta_encontrada[5])
        print("Saldo actual: " + str(cuenta_encontrada[6]))

        # Verificar si existen préstamos en la cuenta
        tiene_deuda = False
        for movimiento in cuenta_encontrada[7:]:
            if movimiento[1] == 'préstamo':
                tiene_deuda = True
                break
        
        if tiene_deuda:
            print("No puedes retirar saldo mientras tengas una deuda pendiente.")
        elif cuenta_encontrada[6] == 0:
            print("No puedes retirar saldo de una cuenta vacía.")
        else:
            saldoRestado = input("Ingresa el monto que quieres retirar en tu cuenta: ")
            while not saldoRestado.isdigit() or int(saldoRestado) <= 0 or int(saldoRestado) > cuenta_encontrada[6]:
                print("Error: Debes ingresar un monto válido y menor o igual al saldo actual")
                saldoRestado = input("Ingresa el monto que quieres retirar en tu cuenta: ")
            
            saldoRestado = int(saldoRestado)
            saldoActual = cuenta_encontrada[6] - saldoRestado

            # Actualizamos el nuevo saldo actual en la lista "cuentasBancarias"
            cuenta_encontrada[6] = saldoActual

            # Registramos el movimiento en un array de movimientos
            fechaMovimiento = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            movimiento = (fechaMovimiento, 'retiro', saldoRestado)
            cuenta_encontrada.append(movimiento)

            # Imprimimos el nuevo saldo actual
            print("Saldo actualizado en la cuenta: " + str(saldoActual))
            print("Fecha del movimiento: " + fechaMovimiento)
    else:
        print("Cuenta no encontrada")
#Opción 4: Mostrar saldo de la cuenta
def mostrar_detalles_cuenta():
    cedula = input("Introduce el número de cédula: ")
    while not cedula.isdigit() or int(cedula) <= 0:
        print("Error: Debes ingresar números")
        cedula = input("Introduce el número de cédula: ")
    existe = False
    cuenta_encontrada = None
    
    # Iteramos las cuentas
    for cuenta in cuentasBancarias:
        if cuenta[0] == cedula:
            existe = True
            cuenta_encontrada = cuenta
            break
    
    # Si existe, mostramos los detalles de la cuenta
    if existe:
        # Imprimimos los detalles de la cuenta
        print("Cuenta encontrada :D")
        print("Detalles de la cuenta encontrada: ")
        # Posición 0: Cédula
        print("Cédula: " + cuenta_encontrada[0])
        # Posición 1: Nombre(s)
        print("Nombre(s): " + cuenta_encontrada[1])
        # Posición 2: Apellido(s)
        print("Apellido(s): " + cuenta_encontrada[2])
        # Posición 3: Edad
        print("Edad: " + str(cuenta_encontrada[3]))
        # Posición 4: Fecha de apertura
        print("Fecha de apertura: " + str(cuenta_encontrada[4]))
        # Posición 5: Contraseña
        print("Contraseña: " + cuenta_encontrada[5])
        # Posición 6: Saldo
        print("Saldo actual: " + str(cuenta_encontrada[6]))
    else:
        print("Cuenta no encontrada")
#Opción 5: Hacer préstamo con la cuenta
def prestamo_con_cuenta(cuentasBancarias):
    cedula = input("Ingresa tu número de cédula para continuar: ")
    existe = False
    cuenta_encontrada = None

    # Iteramos las cuentas
    for cuenta in cuentasBancarias:
        if cuenta[0] == cedula:
            existe = True
            cuenta_encontrada = cuenta
            break

    # Si existe, le debitamos una cantidad a la cuenta
    if existe:
        print("Cuenta encontrada :D")
        print("Detalles de la cuenta encontrada: ")
        # Posición 0: Cédula
        print("Cédula: " + cuenta_encontrada[0])
        # Posición 1: Nombre(s)
        print("Nombre(s): " + cuenta_encontrada[1])
        # Posición 2: Apellido(s)
        print("Apellido(s): " + cuenta_encontrada[2])
        # Posición 3: Edad
        print("Edad: " + cuenta_encontrada[3])
        # Posición 4: Fecha de apertura
        print("Fecha de apertura: " + cuenta_encontrada[4])
        # Posición 5: Contraseña
        print("Contraseña: " + cuenta_encontrada[5])
        # Posición 6: Saldo
        print("Saldo actual: " + str(cuenta_encontrada[6]))

        # Verificamos si ya existe un préstamo registrado en la cuenta
        tiene_prestamo = False
        for movimiento in cuenta_encontrada[7:]:
            if movimiento[1] == 'préstamo':
                tiene_prestamo = True
                break

        if tiene_prestamo:
            print("Ya tienes un préstamo registrado en esta cuenta.")
        else:
            saldoDebitado = input("Ingresa el monto del préstamo: ")
            while not saldoDebitado.isdigit() or int(saldoDebitado) <= 0:
                print("Error: Debes ingresar un monto válido")
                saldoDebitado = input("Ingresa el monto del préstamo: ")

            saldoDebitado = int(saldoDebitado)

            if saldoDebitado <= cuenta_encontrada[6] and saldoDebitado <= 4 * cuenta_encontrada[6]:
                saldoActual = cuenta_encontrada[6] - saldoDebitado
                cuenta_encontrada[6] = saldoActual

                print("Saldo debitado: " + str(saldoDebitado))
                print("Saldo actual: " + str(saldoActual))

                # Registramos el movimiento en un array de movimientos
                fechaMovimiento = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                movimiento = (fechaMovimiento, 'préstamo', saldoDebitado)
                cuenta_encontrada.append(movimiento)

                print("Fecha del movimiento: " + fechaMovimiento)
            else:
                print("El monto del préstamo excede el saldo disponible o supera 4 veces el saldo actual.")
    else:
        print("Cuenta no encontrada")
#Opción 6: Ver préstamos activos
def ver_prestamos_activos():
    cedula = input("Introduce el número de cédula: ")
    while not cedula.isdigit() or int(cedula) <= 0:
        print("Error: Debes ingresar números")
        cedula = input("Introduce el número de cédula: ")
    
    existe = False
    cuenta_encontrada = None

    # Iteramos las cuentas
    for cuenta in cuentasBancarias:
        if cuenta[0] == cedula:
            existe = True
            cuenta_encontrada = cuenta
            break
    
    # Si existe, mostramos los préstamos activos de la cuenta
    if existe:
        # Imprimimos los detalles de la cuenta
        print("Cuenta encontrada :D")
        print("Detalles de la cuenta encontrada: ")
        # Posición 0: Cédula
        print("Cédula: " + cuenta_encontrada[0])
        # Posición 1: Nombre(s)
        print("Nombre(s): " + cuenta_encontrada[1])
        # Posición 2: Apellido(s)
        print("Apellido(s): " + cuenta_encontrada[2])
        # Posición 3: Edad
        print("Edad: " + str(cuenta_encontrada[3]))
        # Posición 4: Fecha de apertura
        print("Fecha de apertura: " + cuenta_encontrada[4])
        # Posición 5: Contraseña
        print("Contraseña: " + cuenta_encontrada[5])
        # Posición 6: Saldo
        print("Saldo actual: " + str(cuenta_encontrada[6]))
        
        # Imprimimos los préstamos activos de la cuenta
        print("Préstamos:")
        for movimiento in cuenta_encontrada[7:]:
            fecha_movimiento, tipo, monto = movimiento
            if tipo == 'préstamo':
                print("Fecha: " + str(fecha_movimiento) + ", Tipo: " + tipo + ", Monto: " + str(monto))
    else:
        print("Cuenta no encontrada")
#Opción 7: Abonar a préstamo
def abonar_a_prestamo():
    cedula = input("Ingresa tu número de cédula para continuar: ")
    existe = False
    cuenta_encontrada = None

    # Iteramos las cuentas
    for cuenta in cuentasBancarias:
        if cuenta[0] == cedula:
            existe = True
            cuenta_encontrada = cuenta
            break

    # Si existe, le debitamos una cantidad a la cuenta
    if existe:
        print("Cuenta encontrada :D")
        print("Detalles de la cuenta encontrada: ")
        # Posición 0: Cédula
        print("Cédula: " + cuenta_encontrada[0])
        # Posición 1: Nombre(s)
        print("Nombre(s): " + cuenta_encontrada[1])
        # Posición 2: Apellido(s)
        print("Apellido(s): " + cuenta_encontrada[2])
        # Posición 3: Edad
        print("Edad: " + cuenta_encontrada[3])
        # Posición 4: Fecha de apertura
        print("Fecha de apertura: " + cuenta_encontrada[4])
        # Posición 5: Contraseña
        print("Contraseña: " + cuenta_encontrada[5])
        # Posición 6: Saldo
        print("Saldo actual: " + str(cuenta_encontrada[6]))

        # Imprimimos los movimientos de la cuenta
        print("Movimientos:")
        movimientos = cuenta_encontrada[7:]
        for i, movimiento in enumerate(movimientos):
            fecha_movimiento, tipo, monto = movimiento
            print("Índice: " + str(i) + ", Fecha: " + str(fecha_movimiento) + ", Tipo: " + tipo + ", Monto: " + str(monto))

        # Solicitar índice del préstamo al que se desea abonar
        indice_abono = int(input("Ingresa el índice del préstamo al que deseas abonar: "))

        if indice_abono < len(movimientos) and movimientos[indice_abono][1] == 'préstamo':
            monto_abono = int(input("Ingresa el monto del abono: "))
            if monto_abono <= cuenta_encontrada[6]:
                cuenta_encontrada[6] -= monto_abono
                movimientos[indice_abono] = (movimientos[indice_abono][0], 'abono', monto_abono)
                print("Abono realizado exitosamente.")
                print("Saldo actual: " + str(cuenta_encontrada[6]))

                # Verificar si el préstamo se ha pagado en su totalidad
                if monto_abono == movimientos[indice_abono][2]:
                    cuenta_encontrada.pop(indice_abono + 7)  # Eliminar el movimiento de préstamo de la cuenta
                    print("El préstamo ha sido completamente pagado y se ha eliminado de la lista de movimientos.")

                # Registramos el movimiento de abono en un array de movimientos
                movimiento = (fechaMovimiento, 'abono deuda', monto_abono)
                cuenta_encontrada.append(movimiento)

                # Si el abono es mayor a la deuda, se adiciona al capital
                if monto_abono > movimientos[indice_abono][2]:
                    saldo_adicional = monto_abono - movimientos[indice_abono][2]
                    cuenta_encontrada[6] += saldo_adicional
                    print("El abono excedió la deuda. Se ha adicionado $" + str(saldo_adicional) + " al capital.")
            else:
                print("No se puede realizar el abono. Verifica el monto ingresado.")
        else:
            print("No se puede realizar el abono. Verifica el índice del préstamo y el monto ingresado.")
    else:
        print("Cuenta no encontrada")
#Opción 8: ver_movimientos
def ver_movimientos():
    cedula = input("Ingresa tu número de cédula para continuar: ")
    existe = False
    cuenta_encontrada = None
    totalDeuda = 0

    # Iteramos las cuentas
    for cuenta in cuentasBancarias:
        if cuenta[0] == cedula:
            existe = True
            cuenta_encontrada = cuenta
            break

    # Si existe, mostramos los movimientos de la cuenta
    if existe:
        print("Cuenta encontrada :D")
        print("Detalles de la cuenta encontrada: ")
        # Posición 0: Cédula
        print("Cédula: " + cuenta_encontrada[0])
        # Posición 1: Nombre(s)
        print("Nombre(s): " + cuenta_encontrada[1])
        # Posición 2: Apellido(s)
        print("Apellido(s): " + cuenta_encontrada[2])
        # Posición 3: Edad
        print("Edad: " + cuenta_encontrada[3])
        # Posición 4: Fecha de apertura
        print("Fecha de apertura: " + cuenta_encontrada[4])
        # Posición 5: Contraseña
        print("Contraseña: " + cuenta_encontrada[5])
        # Posición 6: Saldo
        print("Saldo actual: " + str(cuenta_encontrada[6]))
        # Imprimimos los movimientos de la cuenta
        print("Movimientos:")
        for movimiento in cuenta_encontrada[7:]:
            fecha_movimiento, tipo, monto = movimiento
            if tipo == 'préstamo':
                totalDeuda += monto
            print("Fecha: " + str(fecha_movimiento) + ", Tipo: " + tipo + ", Monto: " + str(monto) + ", Total de deuda: " + str(totalDeuda))
    else:
        print("Cuenta no encontrada")
#Opciones del menú
opciones = 0
while opciones != 9:
    opciones = int(input(
        "Selecciona una opción:" + "\n" +
        "1. Crear cuenta" + "\n" +
        "2. Consignar saldo a la cuenta" + "\n" +
        "3. Retirar saldo de la cuenta" + "\n" +
        "4. Mostrar saldo de la cuenta" + "\n" +
        "5. Hacer préstamo con la cuenta" + "\n" +
        "6. Ver préstamos activos" + "\n" +
        "7. Abonar a préstamo "+"\n"+
        "8. Ver movimientos "+"\n"+
        "Escribe un número: "))
    if opciones == 1:
        crear_cuenta()
    elif opciones == 2:
        realizar_deposito()
    elif opciones == 3:
        realizar_retiro()
    elif opciones == 4:
        mostrar_detalles_cuenta()
    elif opciones == 5:
        prestamo_con_cuenta(cuentasBancarias)
    elif opciones == 6:
        ver_prestamos_activos()
    elif opciones == 7:
        abonar_a_prestamo()
    elif opciones == 8:
        ver_movimientos()
    elif opciones == 9:
        print("Salir")
    else:
        print("Opción inválida")