print("Funciones v2")
print("Ever Daniel Pereyra Castillo")

# Lista
juegos = ["Pacman",  "Mario", "Megaman"]
def verlista(games):
    for unjuego in games:
        print(unjuego)
print("Imprime la lista de Juegos")
verlista(juegos)

# Tupla
estados = ("Chihuahua", "Colima", "Veracruz")
def vertupla(ado):
    for unest in ado:
        print(unest)
print("Imprime los estados de la tupla")
vertupla(estados)

# Set
comida = {"pizza", "Hamburguesa", "hotdog"}
def verset(comidas):
    for chatarra in comidas:
        print(chatarra)
print("Imprime la comida del set")
verset(comida)

# Diccionario
animales = {"Carnivoro": "Oso", "Herbivoro": "Elefante", "Omnivoro": "Cerdo"}
def ver_diccionario(anim):
    for tipo, nombre in anim.items():
        print(f"tipo: {tipo}, nombre: {nombre}")
print("Imprime los animales y su tipo del diccionario")
ver_diccionario(animales)


