class Computadora:
    def __init__(self, marca, procesador, ram, almacenamiento):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
    def es_ram_igual(self, x):
        if self.ram == x:
            return True
        else:
            return False
    def mayor_almacenamiento(self, otra):
        if self.almacenamiento > otra.almacenamiento:
            return self
        else:
            return otra
    def __str__(self):
        return self.marca + " - " + self.procesador + " - RAM: " + str(self.ram) + "GB - Almacenamiento: " + str(self.almacenamiento) + "GB"