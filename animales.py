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
        if enemigo is not self:
            daño = self.ataque - self.defensa
            enemigo.hp -= daño
            if self.enemigo.hp <= 0:
                print(f"{self.nombre} ha caído")
            else:
                print(f"{self.nombre} hace {daño} puntos de daño a {enemigo.nombre}")
        else:
            print("No te puedes suicidar!!")



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
