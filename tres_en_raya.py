import random

class TresEnRaya:
    def __init__(self, j1, j2):
        self.tablero = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.jugadores = [j1, j2]
        self.simbolos = ["X", "O"]
        self.turno = random.randint(0, 1)

    def mostrar_tablero(self, con_numeros=True):
        for fila in self.tablero:
            print(" | ".join(fila))
            print("-" * 9)

    def colocar_ficha(self, posicion):
        for fila in range(3):
            for col in range(3):
                if self.tablero[fila][col] == str(posicion):
                    self.tablero[fila][col] = self.simbolos[self.turno]
                    return True
        return False

    def verificar_ganador(self):
        t = self.tablero
        for i in range(3):
            if t[i][0] == t[i][1] == t[i][2]:
                return t[i][0]
            if t[0][i] == t[1][i] == t[2][i]:
                return t[0][i]
        if t[0][0] == t[1][1] == t[2][2]:
            return t[0][0]
        if t[0][2] == t[1][1] == t[2][0]:
            return t[0][2]
        return None

    def tablero_lleno(self):
        for fila in self.tablero:
            for casilla in fila:
                if casilla.isdigit():
                    return False
        return True

    def reiniciar(self):
        self.tablero = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def cargar_historial():
    historial = {}
    try:
        with open("historial.txt", "r") as f:
            for linea in f:
                nombre, puntos = linea.strip().split(":")
                historial[nombre] = int(puntos)
    except FileNotFoundError:
        pass
    return historial

def guardar_historial(historial):
    with open("historial.txt", "w") as f:
        for nombre, puntos in historial.items():
            f.write(f"{nombre}:{puntos}\n")

historial = cargar_historial()

while True:
    print("\n=== TRES EN RAYA ===")
    print("1. Jugar")
    print("2. Ver historial")
    print("3. Salir")
    opcion = input("Opcion: ")
    
    if opcion == "1":
        n1 = input("Jugador 1: ")
        n2 = input("Jugador 2: ")
        if n1 not in historial: historial[n1] = 0
        if n2 not in historial: historial[n2] = 0
        
        juego = TresEnRaya(n1, n2)
        print(f"Comienza: {juego.jugadores[juego.turno]}")
        
        jugando = True
        while jugando:
            print("\n")
            juego.mostrar_tablero()
            print(f"Turno de {juego.jugadores[juego.turno]} ({juego.simbolos[juego.turno]})")
            pos = input("Elige posicion (1-9): ")
            
            if pos.isdigit() and 1 <= int(pos) <= 9:
                if juego.colocar_ficha(pos):
                    ganador_simbolo = juego.verificar_ganador()
                    if ganador_simbolo:
                        juego.mostrar_tablero()
                        ganador_nombre = juego.jugadores[juego.turno]
                        print(f"¡GANÓ {ganador_nombre}!")
                        historial[ganador_nombre] += 1
                        jugando = False
                    elif juego.tablero_lleno():
                        juego.mostrar_tablero()
                        print("¡Empate!")
                        jugando = False
                    else:
                        juego.turno = 1 - juego.turno
                else:
                    print("Error: posicion ocupada.")
            else:
                print("Error: posicion invalida.")
                
    elif opcion == "2":
        print("\n--- HISTORIAL ---")
        for nombre, victorias in historial.items():
            print(f"{nombre}: {victorias} victorias")
            
    elif opcion == "3":
        print("Guardando historial...")
        guardar_historial(historial)
        print("¡Hasta luego!")
        break
