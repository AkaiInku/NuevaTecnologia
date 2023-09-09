def calcular_cuotas(compra, tasa_interes_mensual, cuotas):
    
 cuota_mensual = (compra/ cuotas) + (compra * tasa_interes_mensual)
 return cuota_mensual
Total = 10000
Credito = 200000
plazo_maximo = 12
tasa_interes_mensual = 0.025
Credito_establecido = 200000
menu1 =True
menu2=True

while menu1:
    print("!!Bienvenido al banco DQS!!!\n\
        Porfavor elija una de las opciones\n\
        1.- Ingresar dinero:\n\
        2.- Sacar Dinero\n\
        3.- Saldo\n\
        4.- Tarjeta Crédito\n\
        5.- Donar Dinero\n\
        6.- Salir")
    opcion = int(input())
    
    if opcion == 1:
        ingreso = float(input("Cuanto dinero deseas ingresar?: "))
        Total += ingreso
        print(f"Tu saldo es de $ {Total:.2f}")
        
    elif opcion == 2:
        egreso = float(input("Cuanto dinero deseas sacar?: "))
        Total -= egreso
        print(f"Tu saldo es de: $ {Total:.2f}")
        
    elif opcion == 3:
        print(f"El total en tu cuenta de débito es: $ {Total:.2f}")
        
    elif opcion == 4:
     while menu2:
        print("Operaciones de tarjeta crédito:")
        print("1.- Comprar")
        print("2.- Pagar Tarjeta")
        print("3.- Atras ")
        Opcion_tarjetaC = int(input("Selecciona una opción: "))
        
        if Opcion_tarjetaC == 1:
            compra = float(input("Monto de la compra: "))
            
            if compra > Credito:
             print("No tienes suficiente crédito para realizar esta compra.")
             continue
         
            Credito -= compra 
            
            cuotas = int(input("Ingrese el número de cuotas (1-12): "))
            if cuotas < 1:
                cuotas = 1
            elif cuotas > 12:
                cuotas = 12
                
            cuotas_mensuales = calcular_cuotas(compra, tasa_interes_mensual, cuotas)
            print(f"La cuota mensual para {cuotas} cuotas es de: {cuotas_mensuales:.2f}")
            print(f"Compra realizada. Tu saldo es de {Credito:.2f}")
            
        elif Opcion_tarjetaC == 2:
            print("Opción de pagar tarjeta \n\
                1.- Monto mínimo a pagar\n\
                2.- Monto opcional\n\
                3.- Atras")
            Opcion_pagar = int(input("Seleccione una opción: "))
            
            if Opcion_pagar == 1:
                monto_minimo = cuotas_mensuales
                print(f"El monto mínimo a pagar es de: {monto_minimo:.2f}")
                Opcion_pagoM = int(input("¿Desea pagar el monto mínimo? (1. Sí / 2. No): "))
                
                if Opcion_pagoM == 1:
                    Total -= monto_minimo
                    Credito += monto_minimo
                    print(f"Se ha realizado el pago mínimo. Su saldo es de {Total:.2f}")
                    print(f"Su tarjeta de débito tiene: {Total}")
                    print(f"Su tarjeta de crédito tiene para su uso: {Credito}")
                elif Opcion_pagoM ==2:
                    print(f"su cuota minima de este mes es de: $ {monto_minimo}")
                    menu1 = True
                else:
                  print("Opción no válida. Por favor, elija una opción válida.")
                  menu2=True
                   
            elif Opcion_pagar == 2:
             print(f"Su crédito actual es de {Credito:.2f}")
             cantidad_pagar = float(input("Digite la cantidad que desea depositar: "))
    
    
            if Credito + cantidad_pagar * (1 + tasa_interes_mensual) > 200000:
             print("No puedes depositar esa cantidad ya que excedería el límite máximo de crédito.")
            else:
             Credito += cantidad_pagar * (1 + tasa_interes_mensual)
             print(f"Su crédito es de {Credito:.2f}")
             
        elif Opcion_pagar ==3:
            continue
            
            
    elif opcion == 5:
     donar = float(input("Cuanto dinero deseas donar?: "))
     Total -= donar
     print(f"Tu donaste {donar:.2f}\nTu saldo es de {Total:.2f}")
    
    elif opcion == 6:
     print("Saliendo del programa.")
     break
    
 
    
