   # Paso 1: Variables Globale
lista_de_tareas = []
proximo_id_tarea = 1  # Para generar IDs únicos

   # Paso 2: Implementar agregar_tarea
def agregar_tarea(descripcion, prioridad="media"):
       global proximo_id_tarea  # ¡Necesario para modificar una variable global!
       nueva_tarea = {
           "id": proximo_id_tarea,
           "descripcion": descripcion,
           "completada": False,
           "prioridad": prioridad
       }
       lista_de_tareas.append(nueva_tarea)
       proximo_id_tarea += 1
       print(f"Tarea '{descripcion}' añadida con éxito.")

   # Paso 3: Implementar mostrar_tareas
def mostrar_tareas():
       print("\n--- LISTA DE TAREAS ---")
       if not lista_de_tareas:
           print("¡No hay tareas pendientes! ¡A disfrutar!")
           return
       for tarea in lista_de_tareas:
           estado = "✔" if tarea["completada"] else " "
           print(f"[{estado}] ID: {tarea['id']} | {tarea['descripcion']} (Prioridad: {tarea['prioridad']})")
       print("------------------------")

   # Paso 4: Implementar buscar_tarea_por_id
def buscar_tarea_por_id(id_buscado):
       """Recorre la lista de tareas y devuelve el diccionario de la tarea
       que coincide con el id_buscado. Si no la encuentra, devuelve None."""
       for tarea in lista_de_tareas:
           if tarea["id"] == id_buscado:
               return tarea  # ¡Éxito! Devolvemos el diccionario completo 
       return None  # Si el bucle termina, no se encontró

   # Paso 5: Implementar marcar_tarea_completada
def marcar_tarea_completada(id_tarea):
       # ¡Reutilizamos nuestra función de búsqueda!
       tarea = buscar_tarea_por_id(id_tarea)
       if tarea:  # Si la búsqueda devolvió un diccionario (no None)
           tarea["completada"] = True
           print(f"Tarea '{tarea['descripcion']}' marcada como completada.")
       else:
           print(f"Error: No se encontró la tarea con ID {id_tarea}.")

   # Paso 6: Implementar eliminar_tarea
def eliminar_tarea(id_tarea):
       tarea = buscar_tarea_por_id(id_tarea)
       if tarea:
           lista_de_tareas.remove(tarea)
           print(f"Tarea '{tarea['descripcion']}' eliminada.")
       else:
           print(f"Error: No se encontró la tarea con ID {id_tarea}.")

   # Pruebas iniciales (puedes comentar o eliminar para un programa limpio)
agregar_tarea("Estudiar para el examen de Cálculo")
agregar_tarea("Hacer las compras", prioridad="alta")
mostrar_tareas()

tarea_encontrada = buscar_tarea_por_id(1)
if tarea_encontrada:
       print(f"\nBúsqueda exitosa: {tarea_encontrada['descripcion']}")
else:
       print("\nBúsqueda fallida: Tarea no encontrada.")

tarea_fantasma = buscar_tarea_por_id(99)
if not tarea_fantasma:
       print("Búsqueda de tarea inexistente funcionó correctamente.")

mostrar_tareas()
marcar_tarea_completada(1)
mostrar_tareas()  # Debería mostrar la tarea 1 como completada
eliminar_tarea(2)
mostrar_tareas()  # La tarea 2 ya no debería aparecer
marcar_tarea_completada(99)  # Probar con un ID que no existe

   # Menú interactivo
while True:
       print("\n===== MENÚ TO-DO LIST =====")
       print("1. Agregar nueva tarea")
       print("2. Mostrar todas las tareas")
       print("3. Marcar tarea como completada")
       print("4. Eliminar tarea")
       print("0. Salir")
       opcion = input("Elige una opción: ")
       if opcion == '1':
           desc = input("Descripción de la nueva tarea: ")
           prio = input("Prioridad (alta, media, baja): ")
           agregar_tarea(desc, prio)
       elif opcion == '2':
           mostrar_tareas()
       elif opcion == '3':
           try:
               id_t = int(input("ID de la tarea a completar: "))
               marcar_tarea_completada(id_t)
           except ValueError:
               print("Por favor, ingresa un número válido para el ID.")
       elif opcion == '4':
           try:
               id_t = int(input("ID de la tarea a eliminar: "))
               eliminar_tarea(id_t)
           except ValueError:
               print("Por favor, ingresa un número válido para el ID.")
       elif opcion == '0':
           print("¡Hasta pronto!")
           break  # Rompe el bucle while
       else:
           print("Opción no válida. Inténtalo de nuevo.")
