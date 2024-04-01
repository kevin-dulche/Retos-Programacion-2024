# Operadores de asignación
print("Operadores de asignación")
# Asignación
a = 10
print(f"El valor de a es: {a}")


b = 5

# Operadores aritméticos
print("Operadores aritméticos")
# Suma
suma = a + b
print(f"La suma de {a} + {b} es: {suma}")

# Resta
resta = b - a
print(f"La resta de {b} - {a} es: {resta}")

# Multiplaicacion
multiplicacion = a * b
print(f"La multiplicación de {a} * {b} es: {multiplicacion}")

# Division
division = a / b
print(f"La división de {a} / {b} es: {division}")

# Modulo
modulo = a % b
print(f"El módulo de {a} % {b} es: {modulo}")

# Exponente
exponente = a ** b
print(f"El exponente de {a} ** {b} es: {exponente}")

# Division entera
divisionEntera = a // b
print(f"La división entera de {a} // {b} es: {divisionEntera}")

# Comparaciones
print("Comparaciones")
# Mayor que
print(f"{a} > {b} = {a > b}")

# Menor que
print(f"{a} < {b} = {a < b}")

# Mayor o igual que
print(f"{a} >= {b} = {a >= b}")

# Menor o igual que
print(f"{a} <= {b} = {a <= b}")

# Igual que
print(f"{a} == {b} = {a == b}")

# Diferente que
print(f"{a} != {b} = {a != b}")

# Operadores lógicos
print("Operadores lógicos")
# and
print(f"{a} > {b} and {a} < {b} = {a > b and a < b}")

# or
print(f"{a} > {b} or {a} < {b} = {a > b or a < b}")

# not
print(f"not {a} > {b} = {not a > b}")


# Estructuras de control
print("Estructuras de control")
# if
if a > b:
    print(f"{a} es mayor que {b}")

# if else
if a > b:
    print(f"{a} es mayor que {b}")
else:
    print(f"{a} es menor que {b}")

# if elif else
if a > b:
    print(f"{a} es mayor que {b}")
elif a == b:
    print(f"{a} es igual que {b}")
else:
    print(f"{a} es menor que {b}")

# if anidado
if a > b:
    if a % 2 == 0:
        print(f"{a} es mayor que {b} y es par")
    else:
        print(f"{a} es mayor que {b} y es impar")
else:
    if b % 2 == 0:
        print(f"{b} es mayor que {a} y es par")
    else:
        print(f"{b} es mayor que {a} y es impar")

# while
contador = 0
while contador < 10:
    print(f"Contador: {contador}")
    contador += 1

# for
for i in range(10):
    print(f"i: {i}")

# for con inicio y fin
for i in range(5, 10):
    print(f"i: {i}")

# for con inicio, fin y paso
for i in range(0, 10, 2):
    print(f"i: {i}")

# for con lista
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(f"i: {i}")

# for con lista y break
for i in lista:
    if i == 3:
        break
    print(f"i: {i}")

# for con lista y continue
for i in lista:
    if i == 3:
        continue
    print(f"i: {i}")

# for con lista y else
for i in lista:
    print(f"i: {i}")
else:
    print("Fin del ciclo")

# for con diccionario
diccionario = {
    "nombre": "Kevin",
    "apellido": "Dulche"
}
for key, value in diccionario.items():
    print(f"{key}: {value}")

# for con diccionario y break
for key, value in diccionario.items():
    if key == "apellido":
        break
    print(f"{key}: {value}")

# for con diccionario y continue
for key, value in diccionario.items():
    if key == "apellido":
        continue
    print(f"{key}: {value}")

# for con diccionario y else
for key, value in diccionario.items():
    print(f"{key}: {value}")
else:
    print("Fin del ciclo")

# for con range y break
for i in range(10):
    if i == 5:
        break
    print(f"i: {i}")

# for con range y continue
for i in range(10):
    if i == 5:
        continue
    print(f"i: {i}")

# for con range y else
for i in range(10):
    print(f"i: {i}")
else:
    print("Fin del ciclo")

# for con range y enumerate
for i, v in enumerate(lista):
    print(f"i: {i} - v: {v}")

# for con range y enumerate y break
for i, v in enumerate(lista):
    if i == 2:
        break
    print(f"i: {i} - v: {v}")

# for con range y enumerate y continue
for i, v in enumerate(lista):
    if i == 2:
        continue
    print(f"i: {i} - v: {v}")

# for con range y enumerate y else
for i, v in enumerate(lista):
    print(f"i: {i} - v: {v}")
else:
    print("Fin del ciclo")

# for con range y zip
lista2 = [6, 7, 8, 9, 10]
for v1, v2 in zip(lista, lista2):
    print(f"v1: {v1} - v2: {v2}")

# for con range y zip y break
for v1, v2 in zip(lista, lista2):
    if v1 == 3:
        break
    print(f"v1: {v1} - v2: {v2}")

# for con range y zip y continue
for v1, v2 in zip(lista, lista2):
    if v1 == 3:
        continue
    print(f"v1: {v1} - v2: {v2}")

# for con range y zip y else
for v1, v2 in zip(lista, lista2):
    print(f"v1: {v1} - v2: {v2}")
else:
    print("Fin del ciclo")

# for con range y zip y enumerate
for i, (v1, v2) in enumerate(zip(lista, lista2)):
    print(f"i: {i} - v1: {v1} - v2: {v2}")

# for con range y zip y enumerate y break
for i, (v1, v2) in enumerate(zip(lista, lista2)):
    if i == 2:
        break
    print(f"i: {i} - v1: {v1} - v2: {v2}")

# for con range y zip y enumerate y continue
for i, (v1, v2) in enumerate(zip(lista, lista2)):
    if i == 2:
        continue
    print(f"i: {i} - v1: {v1} - v2: {v2}")

# for con range y zip y enumerate y else
for i, (v1, v2) in enumerate(zip(lista, lista2)):
    print(f"i: {i} - v1: {v1} - v2: {v2}")
else:
    print("Fin del ciclo")

# Programa opcional
# Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)