# Simple
a = 33
b = 200

if b > a:
    print(b,"es mayor que",a)

 #Double
y = 200
z = 333
if y > z :
    print(y,"es mayor que",z)
else:
    print(y,"no es mayor que",z)

#Multiple
a1 = 200
a2 = 207
if a > b:
    print(a1,"es mayor que",a2)
elif a1 < a2:
    print(a1,"es menor que ",a2)

x = 28
if x > 10:
    print("por encima de diez")
    if x > 20:
        print("y tambien por encima de 20")
    else:
        print("pero no por encima de 20.")

# parametro end y sep
#sep
print ("Daniela","Luis","Carlos","Camila")#Agrega un espacio por defecto
print ("Daniela","Luis","Carlos","Camila",sep="")#quita el espacio
print ("Daniela","Luis","Carlos","Camila",sep=",")#agrega una coma

print ("Daniela","Luis","Carlos","Camila", sep = "_", end="_Curso_python")# agrega guion bajo


