materias=["matematicas","Espanol","Ciencias","Sociales","Fisica","Quimica"]
#para determinal el tamano de la lista podemos usar len()
print(len(materias))
#print(dir(materias))
#podemos acceder a los elementos indicando la poscicion:
print(materias[2])
#Slicing muestra las posiciones en un rango 
print(materias[2:5])
print(materias[3:])
print(materias[:5])
print(materias[-5:-1])
print(materias[1:5])

#tipos de datos en la lista 
edades=[17,18,20,19,58,80,40]

print(type(edades))

#actualizar un elemento de la lista 

materias[2]="Biologia"

materias[1:3]="Lengua Castellana","Ciensias Naturales"

#agregando elementos a la lista 

materias.append("Religion")
print(materias[0:])

materias.insert(0,"Etica")
print(materias[0:])

#quitar elementos de la lista 

materias.pop()
print(materias[0:])

materias.pop(5)
print(materias[0:])

del materias[4]
print(materias[0:])

#materias.clear()
#print(materias[0:])


print("------------------------")

for i in materias:
    print(i)
    
print("-"*50)

for i in range(len(materias)):
    print(materias[i])
    print("-"*50)
    
for i, materias in enumerate(materias):
    print(i,materias)
    
print("-"*50)

#usando un siclo while

i=0
while i <len(materias):
    print(materias[i])
    i+=1
    print("-"*50)
    
#list comprehension 
[print(i)for i in materias]

#crear lista numero




