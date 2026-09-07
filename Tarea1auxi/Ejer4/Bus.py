class Bus:
    PRECIO_PASAJE = 1.50

    def __init__(self, capacidad, pasajeros_actuales=0):
        self.capacidad = capacidad
        self.pasajeros_actuales = pasajeros_actuales
        self.recaudacion = 0.0
    def subir_pasajeros(self, cantidad):
        if cantidad <= 0:
            print("ERROR: Debe subir al menos 1 pasajero.")
            return
        if self.pasajeros_actuales + cantidad > self.capacidad:
            print("ERROR: No hay suficientes asientos. Asientos disponibles:", self.asientos_disponibles())
            return
        self.pasajeros_actuales = self.pasajeros_actuales + cantidad
        print(cantidad, "pasajeros subieron. Total:", self.pasajeros_actuales)
    def cobrar_pasaje(self, cantidad):
        if cantidad <= 0:
            print("ERROR: Debe cobrar al menos 1 pasaje.")
            return
        if cantidad > self.pasajeros_actuales:
            print("ERROR: Solo hay", self.pasajeros_actuales, "pasajeros.")
            return
        total = cantidad * Bus.PRECIO_PASAJE
        self.recaudacion = self.recaudacion + total
        print("Se cobraron", cantidad, "pasajes. Total recaudado:", self.recaudacion)
    def asientos_disponibles(self):
        return self.capacidad - self.pasajeros_actuales
    def __str__(self):
        return "Capacidad: " + str(self.capacidad) + " | Pasajeros: " + str(self.pasajeros_actuales) + " | Asientos disponibles: " + str(self.asientos_disponibles()) + " | Recaudacion: " + str(self.recaudacion)