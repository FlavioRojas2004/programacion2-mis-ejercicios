import os
import json
# 1. Crear sala llena de 'L'
def crear_sala(filas, columnas):
    return [['L' for _ in range(columnas)] for _ in range(filas)]
# 2. Mostrar sala con formato cuadrícula
def mostrar_sala(sala):
    filas = len(sala)
    columnas = len(sala[0]) if filas > 0 else 0
    print("\nSala de cine:")
    # Encabezado columnas
    print("    " + " ".join(f"{c+1:2}" for c in range(columnas)))
    print("   " + "---" * columnas)
    for i, fila in enumerate(sala):
        fila_str = " ".join(f" {asiento}" for asiento in fila)
        print(f"{i+1:2} |{fila_str}")
# 3. Ocupar asiento con validaciones
def ocupar_asiento(sala, fila, columna):
    filas = len(sala)
    columnas = len(sala[0]) if filas > 0 else 0
    if fila < 1 or fila > filas or columna < 1 or columna > columnas:
        print("Error: Coordenadas fuera de rango.")
        return False
    if sala[fila-1][columna-1] == 'O':
        print("Error: El asiento ya está ocupado.")
        return False
    sala[fila-1][columna-1] = 'O'
    print(f"Asiento ({fila}, {columna}) ocupado exitosamente.")
    return True
# 4. Contar asientos libres
def contar_asientos_libres(sala):
    return sum(asiento == 'L' for fila in sala for asiento in fila)
# Guardar sala en archivo JSON
def guardar_sala(sala, filename="sala_cine.json"):
    with open(filename, 'w') as f:
        json.dump(sala, f)
# Cargar sala desde archivo JSON
def cargar_sala(filename="sala_cine.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return None
# Programa principal
def main():
    print("=== Sistema de Gestión de Sala de Cine ===")
    # Intentar cargar sala existente
    sala = cargar_sala()
    if sala is None:
        print("No se encontró sala guardada. Creando nueva sala 5x8.")
        sala = crear_sala(5, 8)
    else:
        print("Sala cargada desde archivo.")
    while True:
        mostrar_sala(sala)
        libres = contar_asientos_libres(sala)
        print(f"\nAsientos libres: {libres}")
        print("\nMenú:")
        print("1. Ocupar asiento")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == '1':
            try:
                fila = int(input("Ingrese fila (número): "))
                columna = int(input("Ingrese columna (número): "))
                ocupar_asiento(sala, fila, columna)
            except ValueError:
                print("Error: Debes ingresar números válidos para fila y columna.")
        elif opcion == '0':
            print("Guardando sala y saliendo...")
            guardar_sala(sala)
            break
        else:
            print("Opción inválida, intenta de nuevo.")
if __name__ == "__main__":
    main()
    print("Realizado por Flavio Rojas.")
