class CarritoDeCompras:
  def __init__(self):
      self.productos = []
  def agregar_producto(self, producto):
      # Se espera que producto sea un diccionario con claves "nombre" y "precio"
      if "nombre" in producto and "precio" in producto:
          self.productos.append(producto)
      else:
          print("El producto debe tener 'nombre' y 'precio'.")
  def calcular_total(self):
      total = 0
      for producto in self.productos:
          total += producto["precio"]
      return total
  def mostrar_carrito(self):
      if not self.productos:
          print("El carrito está vacío.")
          return
      print("Productos en el carrito:")
      for producto in self.productos:
          print(f"- {producto['nombre']}: ${producto['precio']}")
      print(f"Total a pagar: ${self.calcular_total()}")
# Crear un carrito
carrito = CarritoDeCompras()

# Agregar productos
carrito.agregar_producto({"nombre": "Manzana", "precio": 2.5})
carrito.agregar_producto({"nombre": "Pan", "precio": 1.8})
carrito.agregar_producto({"nombre": "Leche", "precio": 3.0})

# Mostrar carrito
carrito.mostrar_carrito()
print("Realizado por Flavio Rojas.")
      