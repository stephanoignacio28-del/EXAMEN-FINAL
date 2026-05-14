import random

class tresenraya:
    def __init__(self, j1, j2):
        self.jugadores = [j1, j2]
        self.tablero = [1, 2, 3], [4, 5, 6], [7, 8, 9]
        self.icono = ["X", "O"]
        self.turno = random.randint(0,1)
        
    def mostrar_tablero(self, con_numeros=True):
        for fila in self.tablero:
            print(" | ".join(fila))
            print("-" * 9)
    
    def colocar_ficha(self, posicion):
        for fila in range(3):
            for col in range(3):
                if self.tablero[fila][col] == str(posicion):
                    self.tablero[fila][col] = self.icono[self.turno]
                    return True
        return False
