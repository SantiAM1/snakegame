#Display size
altura = 8
base = 8

from funciones import pos_init, snake_long
    
class Player:
    def __init__(self, pos, body, life, manzana):
        self.pos = pos
        self.body = body
        self.life = life
        self.manzana = manzana
    
    def up(self, display):
        if self.pos[1] == 1:
            self.pos[1] = display.altura
        else:
            self.pos[1] -= 1
    
    def down(self, display):
        if self.pos[1] == display.altura:
            self.pos[1] = 1
        else:
            self.pos[1] += 1

    def right(self, display):
        if self.pos[0] == display.base:
            self.pos[0] = 1
        else:
            self.pos[0] += 1
    
    def left(self, display):
        if self.pos[0] == 1:
            self.pos[0] = display.base
        else:
            self.pos[0] -= 1

    def colision_test(self):
        for element_body in self.body:
            if self.pos == element_body:
                self.life = -1
                break
        if self.pos == self.manzana:
            self.life += 1
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

        for i in range(1, self.altura+1):
            fila = ["-"]*self.base

            if i == manzana_y:
                fila[manzana_x] = "O"

            for element_body in player.body:
                if element_body[1] == i:
                    fila[element_body[0]-1] = "x"

            if i == posy:
                fila[posx] = "@"

            fila = " ".join(fila)
            filas.append(fila)

        filas.insert(0,"█"+"██" * (self.base-1))
        filas.append("█"+"██" * (self.base-1))
        return "\n".join(filas)
