'''Actividad: Gestor de inventario
1.- Creación: Crear una lista llamada inventario que contenga los 
siguientes articulos: "laptop", "ratón", "monitor", "cable hdmi"'''
inventario = ["laptop", "ratón", "monitor", "cable hdmi"]

'''2.- Expansión: Utiliza el método correspondiente para agregar "impresora" al final de la lista'''
inventario.append("impresora")
inventario.append("teclado")

'''3.-Conteo: Utiliza la función integrada para mostrar cuantos elementos totales hay en la lista.'''
print(f"Cantidad de elementos en el inventario: {len(inventario)}")

'''4.- Acceso y modificación: Modifica "teclado" por "teclado mecánico"'''
inventario[5] = "teclado mecánico"

'''5.- Slicing: Crear una nueva lista llamada "promoción", debe contener
solo los 3 primeros elementos de la lista "inventario".'''
promocion = inventario[:3]

'''6.- Mostrar la lista de inventario ordenado alfabeticamente.'''
print(sorted(inventario))

'''7.- Elimina el último elemento de la lista inventario mostrtando el elemento 
eliminado y la lista final.'''
print(f"Elemento eliminado: {inventario.pop()}")
print(f"Inventario actual: {inventario}")