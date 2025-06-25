import json
import os
# Archivo donde se guardan los contactos
ARCHIVO = "contactos.json"
# Lista global que almacena los contactos
agenda = []
#PERSISTENCIA 
# Cargar contactos desde el archivo JSON
def cargar_contactos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
# Guardar contactos al archivo JSON
def guardar_contactos():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(agenda, f, indent=4, ensure_ascii=False)
#FUNCIONES PRINCIPALES 
# Agregar un nuevo contacto
def agregar_contacto():
    nombre = input("Nombre: ")
    telefonos = input("Teléfonos (separados por coma): ").split(",")
    telefonos = [t.strip() for t in telefonos]
    email = input("Email: ")
    direccion = input("Dirección (opcional): ")
    contacto = {
        "nombre": nombre,
        "telefonos": telefonos,
        "email": email,
        "direccion": direccion
    }
    agenda.append(contacto)
    guardar_contactos()
    print(f" Contacto '{nombre}' agregado.\n")
# Buscar un contacto por nombre
def buscar_por_nombre():
    nombre = input("Nombre a buscar: ")
    resultados = [c for c in agenda if c["nombre"].lower() == nombre.lower()]
    if resultados:
        for c in resultados:
            mostrar_un_contacto(c)
    else:
        print(" Contacto no encontrado.\n")
# Editar un contacto existente
def editar_contacto():
    nombre = input("Nombre del contacto a editar: ")
    for contacto in agenda:
        if contacto["nombre"].lower() == nombre.lower():
            print("Deja vacío cualquier campo que no quieras cambiar.")
            nuevo_nombre = input(f"Nuevo nombre [{contacto['nombre']}]: ") or contacto['nombre']
            nuevos_telefonos = input(f"Nuevos teléfonos (separados por coma) [{', '.join(contacto['telefonos'])}]: ")
            nuevos_telefonos = [t.strip() for t in nuevos_telefonos.split(",")] if nuevos_telefonos else contacto['telefonos']
            nuevo_email = input(f"Nuevo email [{contacto['email']}]: ") or contacto['email']
            nueva_direccion = input(f"Nueva dirección [{contacto['direccion']}]: ") or contacto['direccion']
            contacto.update({
                "nombre": nuevo_nombre,
                "telefonos": nuevos_telefonos,
                "email": nuevo_email,
                "direccion": nueva_direccion
            })
            guardar_contactos()
            print(" Contacto actualizado.\n")
            return
    print(" Contacto no encontrado.\n")
# Eliminar un contacto por nombre
def eliminar_contacto():
    nombre = input("Nombre del contacto a eliminar: ")
    global agenda
    original = len(agenda)
    agenda = [c for c in agenda if c["nombre"].lower() != nombre.lower()]
    if len(agenda) < original:
        guardar_contactos()
        print(f" Contacto '{nombre}' eliminado.\n")
    else:
        print(" Contacto no encontrado.\n")
# Mostrar todos los contactos
def mostrar_contactos():
    if not agenda:
        print(" Agenda vacía.\n")
    for c in agenda:
        mostrar_un_contacto(c)
# Mostrar un solo contacto
def mostrar_un_contacto(c):
    print(f" {c['nombre']}")
    print(f"    Teléfonos: {', '.join(c['telefonos'])}")
    print(f"    Email: {c['email']}")
    if c['direccion']:
        print(f"    Dirección: {c['direccion']}")
    print()
#MENÚ INTERACTIVO
def menu():
    while True:
        print(" GESTOR DE CONTACTOS")
        print("1. Agregar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")
        opcion = input("Elige una opción (1-6): ")
        print()
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_por_nombre()
        elif opcion == "3":
            editar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            mostrar_contactos()
        elif opcion == "6":
            print(" Saliendo del gestor. ¡Hasta pronto!")
            break
        else:
            print(" Opción no válida, intenta de nuevo.\n")
# Cargar contactos al iniciar
agenda = cargar_contactos()
# Iniciar menú interactivo
menu()
print("Realizado por Flavio Rojas.")