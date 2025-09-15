from juego import crear_personaje
from batalla import batalla
from base_datos import boss

def iniciar_juego():
    jugador = crear_personaje()
    batalla(jugador, boss)

if __name__ == "__main__":
    iniciar_juego()
