# clase12_diccionarios.py

# 1. Crear el diccionario producto
producto = {
    "codigo": "P001",
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio_unitario": 15.50,
    "stock": 50,
    "proveedor": "El Ceibo Ltda."
}
# 2. Imprimir nombre y precio del producto
print(f"Producto: {producto['nombre']}")
print(f"Precio unitario: ${producto['precio_unitario']:.2f}")
# 3. Simular una venta y actualizar stock (restar 5 unidades)
producto["stock"] -= 5
# 4. Añadir clave "en_oferta" con valor True
producto["en_oferta"] = True
# 5. Imprimir el diccionario completo para ver todos los cambios
print("\nEstado actualizado del producto:")
for clave, valor in producto.items():
    print(f"{clave}: {valor}")
# Ejercicio 2: Creando un Inventario
def crear_inventario():
    inventario = []
    # 2. Crear productos como diccionarios
    producto1 = {
        "codigo": "P001",
        "nombre": "Chocolate para Taza 'El Ceibo'",
        "precio_unitario": 15.50,
        "stock": 50,
        "proveedor": "El Ceibo Ltda."
    }
    producto2 = {
        "codigo": "P002",
        "nombre": "Café de los Yungas",
        "precio_unitario": 25.00,
        "stock": 100,
        "proveedor": "Cafés Bolivianos S.A."
    }
    producto3 = {
        "codigo": "P003",
        "nombre": "Quinua Real en Grano",
        "precio_unitario": 40.75,
        "stock": 80,
        "proveedor": "Quinua Orgánica Ltda."
    }
    # 3. Añadir productos a la lista inventario
    inventario.append(producto1)
    inventario.append(producto2)
    inventario.append(producto3)
    return inventario
def mostrar_inventario(inventario):
    print("\n--- Inventario Actual ---")
    for producto in inventario:
        print(f"- {producto['nombre']}: {producto['stock']} unidades en stock.")
def main_inventario():
    inventario = crear_inventario()
    # 4. Imprimir cantidad de tipos de producto
    print(f"Cantidad de tipos de productos en inventario: {len(inventario)}")
    # 5. Mostrar resumen del inventario
    mostrar_inventario(inventario)
if __name__ == "__main__":
    main_inventario()
print("Realizado por Flavio Rojas.")