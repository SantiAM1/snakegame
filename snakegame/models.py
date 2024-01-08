#Display size
altura = 8
base = 8

from funciones import pos_init, snake_long, graphics
    
class Player:
    def __init__(self, pos, body, life, manzana):
        self.pos = pos
        self.body = body
        self.life = life
        self.manzana = manzana
        self.sentido = "up"
    
    def up(self):
        self.sentido = "up"
        if self.pos[1] == 1:
            #Fuera de rango, juego terminado
            self.life = -1
        else:
            self.pos[1] -= 1
    
    def down(self, display):
        self.sentido = "down"
        if self.pos[1] == display.altura:
            #Fuera de rango, juego terminado
            self.life = -1
        else:
            self.pos[1] += 1

    def right(self, display):
        self.sentido = "right"
        if self.pos[0] == display.base:
            #Fuera de rango, juego terminado
            self.life = -1
        else:
            self.pos[0] += 1
    
    def left(self):
        self.sentido = "left"
        if self.pos[0] == 1:
            #Fuera de rango, juego terminado
            self.life = -1
        else:
            self.pos[0] -= 1

    def colision_test(self):
        #Detectar si el jugador choco consigo mismo
        for element_body in self.body:
            if self.pos == element_body:
                self.life = -1
                break
        #Detectar que el juegador come una manzana
        if self.pos == self.manzana:
            self.life += 1
            #Nueva pos de manzana
            while True:
                self.manzana = pos_init(altura, base)
                manzana_valida = True
                if self.manzana == self.pos:
                    manzana_valida = False
                else:
                    for element_body in self.body:
                        if self.manzana == element_body:
                            manzana_valida = False
                            break
                if manzana_valida:
                    break

    def leng_body(self, ultimo):
        #Generar el largo de la serpiente
        self.body = snake_long(self.body, ultimo.copy(), self.life)

    def __str__(self):
        return f"Pos{self.pos} Body{self.body} Life {self.life} Manzana{self.manzana}"
    
class Display:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base
        
    
    def __str__(self):
        return f"Display config {self.altura} x {self.base}"

    def imprimir(self, player):

        posx = player.pos[0] - 1
        posy = player.pos[1]

        manzana_x = player.manzana[0] - 1
        manzana_y = player.manzana[1]

        filas = []
        
        #Importar vectores graficos
        graph = graphics(player)

        for i in range(1, self.altura + 1):
            fila = [" "]*self.base

            if i == manzana_y:
                fila[manzana_x] = "O"
            
            #Generar body de la serpiente con graphics
            for num in range(len(player.body)):
                if player.body[num][1] == i:

                    if num < len(graph) and graph[num] == [1, 0] and graph[num-1] == [1, 0]:
                        fila[player.body[num][0]-1] = "="
                    if num < len(graph) and graph[num] == [-1, 0] and graph[num-1] == [-1, 0]:
                        fila[player.body[num][0]-1] = "="

                    if num < len(graph) and graph[num] == [0, 1] and graph[num-1] == [0, 1]:
                        fila[player.body[num][0]-1] = "║"
                    if num < len(graph) and graph[num] == [0, -1] and graph[num-1] == [0, -1]:
                        fila[player.body[num][0]-1] = "║"
                    
                    if num < len(graph) and graph[num] == [0, 1] and graph[num-1] == [1, 0]:
                        fila[player.body[num][0]-1] = "╚"
                    if num < len(graph) and graph[num] == [0, 1] and graph[num-1] == [-1, 0]:
                        fila[player.body[num][0]-1] = "╝"
                    
                    if num < len(graph) and graph[num] == [0, -1] and graph[num-1] == [1, 0]:
                        fila[player.body[num][0]-1] = "╔"
                    if num < len(graph) and graph[num] == [0, -1] and graph[num-1] == [-1, 0]:
                        fila[player.body[num][0]-1] = "╗"
                    
                    if num < len(graph) and graph[num] == [1, 0] and graph[num-1] == [0, 1]:
                        fila[player.body[num][0]-1] = "╗"
                    if num < len(graph) and graph[num] == [1, 0] and graph[num-1] == [0, -1]:
                        fila[player.body[num][0]-1] = "╝"

                    if num < len(graph) and graph[num] == [-1, 0] and graph[num-1] == [0, 1]:
                        fila[player.body[num][0]-1] = "╔"
                    if num < len(graph) and graph[num] == [-1, 0] and graph[num-1] == [0, -1]:
                        fila[player.body[num][0]-1] = "╚"

                    if num == 0 and num < len(graph) and player.sentido == "up" and graph[num] == [1, 0]:
                        fila[player.body[num][0]-1] = "╝"
                    if num == 0 and num < len(graph) and player.sentido == "up" and graph[num] == [-1, 0]:
                        fila[player.body[num][0]-1] = "╚"
                    if num == 0 and num < len(graph) and player.sentido == "up" and (graph[num] == [0, 1] or graph[num] == [0, -1]):
                        fila[player.body[num][0]-1] = "║"

                    if num == 0 and num < len(graph) and player.sentido == "down" and graph[num] == [-1, 0]:
                        fila[player.body[num][0]-1] = "╔"
                    if num == 0 and num < len(graph) and player.sentido == "down" and graph[num] == [1, 0]:
                        fila[player.body[num][0]-1] = "╗"
                    if num == 0 and num < len(graph) and player.sentido == "down" and (graph[num] == [0, 1] or graph[num] == [0, -1]):
                        fila[player.body[num][0]-1] = "║"

                    if num == 0 and num < len(graph) and player.sentido == "left" and graph[num] == [0, 1]:
                        fila[player.body[num][0]-1] = "╝"
                    if num == 0 and num < len(graph) and player.sentido == "left" and graph[num] == [0, -1]:
                        fila[player.body[num][0]-1] = "╗"
                    if num == 0 and num < len(graph) and player.sentido == "left" and (graph[num] == [1, 0] or graph[num] == [-1, 0]):
                        fila[player.body[num][0]-1] = "="   

                    if num == 0 and num < len(graph) and player.sentido == "right" and graph[num] == [0, 1]:
                        fila[player.body[num][0]-1] = "╚"
                    if num == 0 and num < len(graph) and player.sentido == "right" and graph[num] == [0, -1]:
                        fila[player.body[num][0]-1] = "╔"
                    if num == 0 and num < len(graph) and player.sentido == "right" and (graph[num] == [1, 0] or graph[num] == [-1, 0]):
                        fila[player.body[num][0]-1] = "="   
                    
                    if num == len(player.body)-1:
                        fila[player.body[num][0]-1] = "x"

            #Cabeza de la serpiente
            if i == posy:
                if player.sentido == "up":
                    fila[posx] = "^"
                if player.sentido == "down":
                    fila[posx] = "v"
                if player.sentido == "right":
                    fila[posx] = ">"
                if player.sentido == "left":
                    fila[posx] = "<"

            fila = " ".join(fila)
            filas.append(fila)

        #Bordes
        filas.insert(0, "█" + "██" * (self.base-1))
        filas.append("█" + "██" * (self.base-1))
        return "\n".join(filas)
