# Paso 1: Definir el número secreto
numero_secreto = 7
# Paso 2: Pedir al usuario que adivine el número
print("¡Bienvenido al juego de Adivina el Número!")
intento = int(input("Ingresa un número del 1 al 12: "))

# Paso 3: Repetir mientras no adivine
while intento != numero_secreto:
    if intento < numero_secreto:
        print("muy bajo. Intenta nuevamente.")
    else:
        print("muy alto. Intenta nuevamente.")
    intento = int(input("Ingresa otro número: "))
# Paso 4: Mensaje de felicitaciones
print(f"¡Correcto! El número era {numero_secreto}.")
print("Realizado por Flavio Rojas.")