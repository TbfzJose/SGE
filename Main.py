from cotxe import Cotxe
from colibri import Colibri

cotxe1 = Cotxe("Seat", "Ibiza", 3240, "Rojo", 30000)
cotxe2 = Cotxe("Ford", "Focus", 9819, "Azul", 50000)
cotxe3 = Cotxe("Toyota", "Corolla", 2290, "Blanco", 10000)

colibri1 = Colibri("Colibrí rubí", "Pequeño", "Rojo", 5)
colibri2 = Colibri("Colibrí esmeralda", "Mediano", "Verde", 7)
colibri3 = Colibri("Colibrí gigante", "Grande", "Azul", 3)

print("Marca del primer coche:", cotxe1.get_marca())
print("Modelo del segundo coche:", cotxe2.model)
print("Año del tercer coche:", cotxe3.matricula)

print("Especie del primer colibrí:", colibri1.especie)
print("Tamaño del segundo colibrí:", colibri2.tamaño)
print("Color del tercer colibrí:", colibri3.color)
print("Velocidad del primer colibrí:", colibri1.velocidad)

cotxe1.set_marca("Volkswagen")
cotxe2.color = "Negro"

print("Nueva marca del primer coche:", cotxe1.get_marca())
print("Nuevo color del segundo coche:", cotxe2.color)

colibri1.especie = "Colibrí garganta de rubí"
colibri2.tamaño = "Muy pequeño"

print("Nueva especie del primer colibrí:", colibri1.especie)
print("Nuevo tamaño del segundo colibrí:", colibri2.tamaño)