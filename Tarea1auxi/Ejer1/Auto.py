class Auto:
    def __init__(self, marca, modelo, fecha, kilometraje, color):
        self.marca = marca
        self.modelo = modelo
        self.fecha = fecha
        self.kilometraje = kilometraje
        self.color = color
    def mostrar_kilometraje(self):
        km = self.kilometraje
        metros = km * 1000
        print("Kilometraje:", km, "km")
        print("En metros:", metros, "m")
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print("Color cambiado a:", self.color)
    def __str__(self):
        return self.marca + " " + self.modelo + " (" + str(self.fecha) + ") - Color: " + self.color + " - Km: " + str(self.kilometraje)