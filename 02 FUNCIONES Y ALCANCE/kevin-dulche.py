def fun_sin_return():
    print('Hola mundo')

def fun_con_return():
    return 'Hola mundo'

def fun_con_varios_return():
    return 'Hola mundo', 10, [1, 2, 3]

def fun_con_parametros(param1, param2):
    return f'param1: {param1}, param2: {param2}'

def fun_con_parametros_por_defecto(param1, param2='default'):
    return f'param1: {param1}, param2: {param2}'

def fun_con_fun():
    def fun_interna():
        return 'Hola mundo'
    return fun_interna()

def fun_con_lambda():
    return lambda x: x + 10

def fun_variable_local():
    variable = 'Hola mundo'
# Esto no funcionará porque la variable no está definida en el alcance global
# print(variable)

def ejercicio(cadena_uno, cadena_dos):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0:
            print(cadena_uno)
        elif i % 5 == 0:
            print(cadena_dos)
        elif i % 3 == 0 and i % 5 == 0:
            print(cadena_uno + cadena_dos)
        else:
            print(i)
            contador += 1
    return contador

valor = ejercicio('Fizz', 'Buzz')
print(f"{valor} veces se imprimio el numero")