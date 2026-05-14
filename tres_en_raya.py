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
            with open("historial.txt","r")
            
