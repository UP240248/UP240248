irst_name = "diego"
last_name = "figueroa"
full_name = first_name + "" + last_name
country = "Mexico"
city = "Aguascalientes"
age = 19
year = 2025
is_married = False
is_true = True
is_light_on = False
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on

print ("--Ejercicio 2--")

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#len
print(len(first_name))

#comparar
print(len(first_name)) > len(last_name)
print(len(first_name)) == len(last_name)

num_one = 5
num_two = 4

suma = num_one + num_two
resta = num_one - num_two
multiplicacion = num_one * num_two
division = num_one / num_two
residuo = num_one % num_two
exp = num_one ** num_two
divisionfloor = num_one // num_two

print("Suma: ", suma)
print("Resta :", resta)
print("Multiplicación :", multiplicacion)
print("División :", division)
print("Residuo :", residuo)
print("Exponencial : ", exp)
print("División enterra :", divisionfloor)

#Circulo
radio = 30
pi = 3.1416

areaC = pi * radio ** 2 
circunferencia = 2 * pi * radio 

print("Area del circulo :", areaC)
print("Circunferencia del circulo :", circunferencia)

#Radio desde el imput
radio2 = float(input("Ingresa el radio del circulo :"))
areaC2 = pi * radio2 ** 2
print("El area del circulo 2 es :")

#Pedir datos
nombre = input("Ingresa tu nombre :")
apellido = input("Ingresa tu apellido :")
pais = input("Ingresa tu país :")
edad = int(input("Ingresa tu edad :"))

print("Nombre :", nombre)
print("Apellido :", apellido)
print("País :", pais)
print("Edad :", edad)

#keywords de python
help('keywords')