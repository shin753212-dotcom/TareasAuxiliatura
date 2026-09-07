from Auto import Auto
auto1 = Auto("Toyota", "Corolla", 2020, 15000, "Rojo")
auto2 = Auto("Honda", "Civic", 2021, 20000, "Azul")

print("Auto 1:", auto1)
print("Auto 2:", auto2)

auto1.cambiar_color("Negro")
auto2.cambiar_color("Blanco")

print("Auto 1:", auto1)
print("Auto 2:", auto2)

print("Kilometraje Auto 1:")
auto1.mostrar_kilometraje()

print("Kilometraje Auto 2:")
auto2.mostrar_kilometraje()