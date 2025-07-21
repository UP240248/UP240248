print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool

print("diego abiud figueroa carlos")
print("el nombre de mi familia es carlos")


print("--- ejercicio 3.3 ---")
print("numero entero0", 10)
print("numero flotante", 10.3)
print("numero complejo", 10+11j)
print("cadena de nunero", 10,11,12)
print("bolone", True)
print("lista", [1, 2, 3])
print("diccionario", {"nombre": "Diego", "apellido": "Figueroa"})
print("tupla", (1, 2, 3))
print("set", {1, 2, 3,3})
print("ejemplo de un diccionario", {"nombre": "Diego", "edad": "19"})

print("--- ejercicio 3.4 ---")

x1,y1= 2,3
x2,y2= 10,8

distancia=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("La distancia entre los puntos (2,3) y (10,8) es:", distancia)
