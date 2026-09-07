from Computadora import Computadora
comp1 = Computadora("Dell", "Intel i7", 16, 512)
comp2 = Computadora("HP", "AMD Ryzen 5", 8, 256)

print("Computadora 1:", comp1)
print("Computadora 2:", comp2)

x = 16
print("RAM de comp1 es igual a", x, "?", comp1.es_ram_igual(x))
print("RAM de comp2 es igual a", x, "?", comp2.es_ram_igual(x))

print("La computadora con mayor almacenamiento es:")
mayor = comp1.mayor_almacenamiento(comp2)
print(mayor)