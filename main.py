from animales import *
import random

# Creamos a nuestro perro, hacemos que ladre y se presente
mi_perro = Perro("Tobi", "gris", 60, 10, 5)
mi_perro.ladrar()
mi_perro.presentarse()

# Creamos a nuestro gato, hacemos que maulle y se presente 
mi_gato = Gato("Marramiau", "negro", 50, 13, 4)
mi_gato.maullar()
mi_gato.presentarse()

# Empezamos el combate
while mi_perro.hp > 0 and mi_gato.hp > 0:
    if random.randint(0, 1) == 0:
        mi_gato.atacar(mi_perro) # 50% de probabilidades que el perro ataque
    else:
        mi_perro.atacar(mi_gato) # 50% de probabilidades que el gato ataque

    print(f"Perro hp: {mi_perro.hp}, Gato hp: {mi_gato.hp}\n")

# Comprobamos quién ha salido ganador
print("¡Escuchemos las declaraciones del vencedor!")
if mi_perro.hp > 0:
    mi_perro.ladrar() 
elif mi_gato.hp > 0:
    mi_gato.maullar()
