from Bus import Bus
bus = Bus(40)

print("Bus inicial:")
print(bus)

print("Subir pasajeros:")
bus.subir_pasajeros(25)
bus.subir_pasajeros(10)
bus.subir_pasajeros(10)

print("Cobrar pasajes:")
bus.cobrar_pasaje(20)
bus.cobrar_pasaje(15)

print("Estado final del bus:")
print(bus)