

def calcular_total(valor, incluir_servicio):
    if incluir_servicio:
        total = valor * 1.10
    else:
        total = valor
    return total

valorApagar = int(input("Ingresa el valor a pagar: "))
opcion = input("¿Desea agregar el servicio del 10%? (s/n): ")

if opcion.lower() == "s":
    incluir_servicio = True
else:
    incluir_servicio = False

total_con_servicio = calcular_total(valorApagar, incluir_servicio)
propina = total_con_servicio - valorApagar

print("El valor recibido fue de:", valorApagar)
print("la propina es de:", propina )
print("Total a pagar:", total_con_servicio)
print("hola")
