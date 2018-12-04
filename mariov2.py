import pygame

from pygame.locals import *

pygame.init()

#---CONSTANTES---#

NOIR = (0, 0, 0)
BLEU_ACIER = (70, 130, 180)
BRUN = (88, 41, 0)
ROUGE = (255, 0, 0)

FENETRE_LARGEUR = 800
FENETRE_HAUTEUR = 600
FENETRE_TAILLE = [FENETRE_LARGEUR, FENETRE_HAUTEUR]
fenetre = pygame.display.set_mode(FENETRE_TAILLE)

GRAVITE = 4


#---AUTRES VARIABLES---#

fini = False

enSaut = False

horloge = pygame.time.Clock()

pygame.display.set_caption('MARIO')

mario = pygame.Surface((25, 25))

mario.fill(ROUGE)

x, y = 25, 80

vx, vy = 0, 0

mur = pygame.Surface((25, 25))

mur.fill(BLEU_ACIER)

sol = pygame.Surface((25, 25))

sol.fill(BRUN)

map= [    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],

          [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],

          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],

          ]




#---FONCTIONS---#

def traite_entrees():
    global x, y, vx, vy, enSaut, fini
    for event in pygame.event.get():
        if event.type == QUIT:
            fini = True
        elif event.type == KEYDOWN:
            if event.key == K_SPACE and enSaut == False:
                vy = -35
                enSaut = True
        elif vy == 0:
            enSaut = False




    keys_pressed = pygame.key.get_pressed()

    vx = (keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) * 5



def dessiner_map(fenetre, map):
    for j, ligne in enumerate(map):
        for i, case in enumerate(ligne):
            if case == 1:
                fenetre.blit(mur, (i*25, j*25))
            elif case == 2:
                fenetre.blit(sol, (i*25, j*25))


def from_coord_to_grid(pos):
    x, y = pos
    i = max(0, int(x // 25))
    j = max(0, int(y // 25))
    return i, j

def get_neighbour_blocks(map, i_start, j_start):
    global i
    blocks = []
    for j in range(j_start, j_start+2):
        for i in range(i_start, i_start+2):
            if map[j][i] == 1 or map[j][i] == 2:
                topleft = i*25, j*25
                blocks.append(pygame.Rect((topleft), (25, 25)))
    return blocks

def bloque_sur_collision(map, ancien_pos, nouv_pos, vx, vy):
    ancien_rect = pygame.Rect(ancien_pos, (25, 25))
    nouv_rect = pygame.Rect(nouv_pos, (25, 25))
    i, j = from_coord_to_grid(nouv_pos)
    collide_later = []
    blocks = get_neighbour_blocks(map, i, j)
    for block in blocks:
        if not nouv_rect.colliderect(block):
            continue
        dx_correction, dy_correction = compute_penetration(block, ancien_rect, nouv_rect)
        if dx_correction == 0.0:
            nouv_rect.top += dy_correction
            vy = 0.0
        elif dy_correction == 0.0:
            nouv_rect.left += dx_correction
            vx = 0.0
        else:
            collide_later.append(block)
    for block in collide_later:
        dx_correction, dy_correction = compute_penetration(block, ancien_rect, nouv_rect)
        if dx_correction == dy_correction == 0.0:
            continue
        if abs(dx_correction) < abs(dy_correction):
            dy_correction = 0.0
        elif abs(dy_correction) < abs(dx_correction):
            dx_correction = 0.0
        if dy_correction != 0.0:
            nouv_rect.top += dy_correction
            vy = 0.0
        elif dx_correction != 0.0:
            nouv_rect.left += dx_correction
            vx = 0.0
    x, y = nouv_rect.topleft
    return x, y, vx, vy

def compute_penetration(block, ancien_rect, nouv_rect):
    dx_correction = dy_correction = 0.0
    if ancien_rect.bottom <= block.top < nouv_rect.bottom:
        dy_correction = block.top  - nouv_rect.bottom
    elif ancien_rect.top >= block.bottom > nouv_rect.top:
        dy_correction = block.bottom - nouv_rect.top
    if ancien_rect.right <= block.left < nouv_rect.right:
        dx_correction = block.left - nouv_rect.right
    elif ancien_rect.left >= block.right > nouv_rect.left:
        dx_correction = block.right - nouv_rect.left
    return dx_correction, dy_correction

def effet_pacman():
    global x
    if x == 0:
        x = FENETRE_LARGEUR - 35
    elif x == FENETRE_LARGEUR - 30:
        x = 5
        
def mise_a_jour_position():
    global x, y , vx, vy, GRAVITE, map
    ancien_x, ancien_y = x, y

    vy += GRAVITE

    x += vx

    y += vy

    x, y, vx, vy = bloque_sur_collision(map, (ancien_x, ancien_y), (x, y), vx, vy)



#--- BOUCLE PRINCIPALE ---#

while not fini:

    traite_entrees()

    fenetre.fill(NOIR)

    dessiner_map(fenetre, map)

    mise_a_jour_position()

    effet_pacman()

    fenetre.blit(mario, (x, y))

    horloge.tick(30)

    pygame.display.flip()

pygame.quit()
