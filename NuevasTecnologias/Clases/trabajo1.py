import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def validar_email(email):
    # Expresión regular para validar la estructura del correo electrónico
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    return False



def validar_clave(clave):
    # Verificar longitud mínima
    if len(clave) < 8:
        return False
    
    # Verificar si contiene al menos una letra mayúscula
    if not any(c.isupper() for c in clave):
        return False
    
    # Verificar si contiene al menos una letra minúscula
    if not any(c.islower() for c in clave):
        return False
    
    # Verificar si contiene al menos un dígito
    if not any(c.isdigit() for c in clave):
        return False
    
    
    return True

nombre = input("Ingresa tu primer nombre: ")
apellidos =input("Ingresa tu apellido : ")
clave_ingresada =input("Ingrese su clave: ")

if validar_clave(clave_ingresada):
    print("La clave es válida.")
else:
    print("La clave no cumple con los requisitos de seguridad.")

Email=input("Ingresa tu email:")

if validar_clave(clave_ingresada):
    print("La clave es válida.")
else:
    print("La clave no cumple con los requisitos de seguridad.")