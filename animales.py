class Animal:
    def __init__(self, nombre, color, hp, ataque, defensa, especie):
        self.nombre = nombre
        self.color = color
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.especie = especie
    
    def presentarse(self):
        print(f"Buenas tardes, soy {self.nombre}, un {self.especie} {self.color}!")
        print(f"\tHP -> {self.hp}")
        print(f"\tAtaque -> {self.ataque}")
        print(f"\tDefensa -> {self.defensa}")

    def atacar(self, enemigo):
        daño_recibido = self.ataque - enemigo.defensa
        enemigo.hp -= daño_recibido
        print(f"{self.nombre} hace {daño_recibido} puntos de daño a {enemigo.nombre}")



class Perro (Animal):
    def __init__(self, nombre, color, hp, ataque, defensa):
        super().__init__(nombre, color, hp, ataque, defensa, "perro")

    def ladrar (self):
        print("GUAU GUAU")
        



class Gato (Animal):
    def __init__(self, nombre, color, hp, ataque, defensa):
        super().__init__(nombre, color, hp, ataque, defensa, "gato")

    def maullar(self):
        print("MIAU MIAU")