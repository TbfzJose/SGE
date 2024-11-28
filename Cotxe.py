class Cotxe:
    def __init__(self, marca, model, matricula, color, km):
        self.marca = marca
        self.model = model
        self.matricula = matricula
        self.color = color
        self.km = km

    def get_marca(self):
        return self.marca
    
    def set_marca(self, nueva_marca):
        self.marca = nueva_marca