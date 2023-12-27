import random

def pos_init(altura, base):
    coords = [0,0]
    coords[0] = random.randrange(1, base)
    coords[1] = random.randrange(1, altura)
    return coords

def snake_long(body, ultima_pos, vida):
    body.insert(0, ultima_pos)
    if vida < len(body):
        body.pop()
    return body
