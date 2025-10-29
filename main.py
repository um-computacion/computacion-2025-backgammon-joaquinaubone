"""Módulo principal del juego Backgammon.

Inicializa los componentes principales del juego (tablero, dados y jugadores)
y ejecuta la interfaz CLI para comenzar la partida.
"""
from core.game import Juego
from cli.cli import jugar
from pygameUI.pygame_ui import jugar_pygame

def main():
    """Punto de entrada del programa. Configura los objetos principales y lanza el juego."""
    print("=" * 50)
    print("BACKGAMMON")
    print("=" * 50)
    print("Selecciona la interfaz:")
    print("1. CLI (texto)")
    print("2. GUI (gráfica con Pygame)")
    print("=" * 50)
    juego = Juego()

    while True:
        opcion = input("Ingresa tu opción (1 o 2): ")
        if opcion in ['1', '2']:
            break
        print(" Opción inválida. Por favor ingresa 1 o 2.\n")
    
    if opcion == '2':
        try:
            print("\nIniciando interfaz gráfica...\n")
            jugar_pygame(juego)
        except ImportError:
            print("\n  Error: Pygame no está instalado.")
            print("Instalalo con: pip install pygame")
            print("\nIniciando CLI en su lugar...\n")
            jugar(juego)
            
    else:
        print("\nIniciando interfaz CLI...\n")
        jugar(juego)


if __name__ == '__main__':
    main()