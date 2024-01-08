#IMPORTS
from funciones import pos_init
from models import Display, Player, altura, base

#RANDOMSTART
data = pos_init(altura, base)
pos = data

while True:
    data = pos_init(altura, base)
    manzana = data
    if manzana == pos:
        data = pos_init(altura, base)
        manzana = data
    else:
        break

#GAME CONFIG
life = 1
body = []
last = [0,0]
display = Display(altura, base)
player = Player(pos, body, life, manzana)
moves = ["w","a","s","d"]
check_move = False
print(display.imprimir(player))
#START
while True:

    if check_move:
        player.leng_body(last)
        player.colision_test()
        if player.life == -1:
            print("\n\n Perdiste!")
            break
        print(player)
        print(display.imprimir(player))
        check_move = False
        
    move = input("Move: ")

    if move not in moves:
        print("Movimiento no permitido")
        continue
    
    last[0] = player.pos[0]
    last[1] = player.pos[1]

    if move == "w":
        player.up()
        check_move = True

    if move == "s":
        player.down(display)
        check_move = True

    if move == "a":
        player.left()
        check_move = True

    if move == "d":
        player.right(display)
        check_move = True
