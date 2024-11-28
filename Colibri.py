class Colibri:
        def __init__(self, especie, tamaño, velocidad, color, edad):
        self.especie = especie
        self.tamaño = tamaño
        self.velocidad = velocidad
        self.color = color
        self.edad = edad

    def get_especie(self):
        return self.especie
    
    def get_especie(self, nueva_especie):
        self.especie = nueva_especie