import random

#Coordenadas aleatorias
def pos_init(altura, base):
    coords = [0,0]
    coords[0] = random.randrange(1, base)
    coords[1] = random.randrange(1, altura)
    return coords

#Generacion del cuerpo de la serpiente
def snake_long(body, ultima_pos, vida):
    body.insert(0, ultima_pos)
    if vida < len(body):
        body.pop()
    return body


def graphics(player):
    vectores = []
    #Se analiza elemento por elemento en el cuerpo de la serpiente
    if len(player.body) > 1:
        for i in range(1, len(player.body)):
            #Se generan los vectores jundamentales, los cuales dan direccion a la serpiente
            #Vectores i, -i, j, -j
            vectores.append(vectors(player.body[i-1], player.body[i])) 
    return vectores

def vectors(vector_1,vector_2):
    return [vector_1[0]-vector_2[0],vector_1[1]-vector_2[1]]
