import pygame
from pygame.locals import *
import random
import time
pygame.init()

DEBUG_MODE = True

#---CONSTANTES---#
NOIR = (0, 0, 0)
BLEU_ACIER = (70, 130, 180)
BRUN = (88, 41, 0)
ROUGE = (255, 0, 0)
VERT =(0, 255, 0)

FENETRE_LARGEUR = 800
FENETRE_HAUTEUR = 600
FENETRE_TAILLE = [FENETRE_LARGEUR, FENETRE_HAUTEUR]
fenetre = pygame.display.set_mode(FENETRE_TAILLE)
background = pygame.image.load('images/background.png')
GRAVITE = 4
#---AUTRES VARIABLES---#
fini = False
horloge = pygame.time.Clock()
pygame.display.set_caption('MARIO')

#---CHARGEMENT IMAGES---#
plateforme = pygame.image.load('images/platform.png')
plateforme = pygame.transform.scale(plateforme, (25, 25))

sol = pygame.image.load('images/brick.png')
sol = pygame.transform.scale(sol, (25, 25))

mario_image = pygame.Surface((25, 25))
mario_image.fill(ROUGE)

ennemi_image = pygame.Surface((25, 25))
ennemi_image.fill(VERT)

###DEFINITION ENTITES###
class entite():
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
        self.vx = 0
        self.vy = 0
        self.enSaut = False
        self.pos = (pos_x, pos_y)
        ###MAJ POSITION###
        self.ancien_x, self.ancien_y = self.x, self.y
        self.vy += GRAVITE
        self.x += self.vx
        self.y += self.vy
        self.x, self.y, self.vx, self.vy = bloque_sur_collision(map, (self.ancien_x, self.ancien_y), (self.x, self.y), self.vx, self.vy)
        ###from_coord_to_grid###
        self.x, self.y = self.pos
        self.i = max(0, int(self.x // 25))
        self.j = max(0, int(self.y // 25))
        self.pos = (self.i, self.j)
        self.vx_random = random.randint(1, 5)
    def mise_a_jour_position_ennemi(self):
        self.ancien_x, self.ancien_y = self.x, self.y
        self.vy += GRAVITE
        self.x += self.vx
        self.y += self.vy
        self.x, self.y, self.vx, self.vy = bloque_sur_collision(map, (self.ancien_x, self.ancien_y), (self.x, self.y), self.vx, self.vy)
        self.vx = self.vx_random
        if self.x <= 0:
            self.x = FENETRE_LARGEUR - 35
        elif self.x >= FENETRE_LARGEUR - 30:
            self.x = 5
#---CONFIG MAP---#
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

          [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0],

          [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],

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
def diagnostics():
    if DEBUG_MODE == True:
        print("ennemi 1 x :", ennemi.x, "ennemi 1 y :", ennemi.y)
        print("ennemi 2 x :", ennemi2.x, "ennemi 2 y :", ennemi2.y)
        print("mario x :", mario_x, "mario y :", mario_y)

def traite_entrees():
    global mario_x, mario_y, mario_vx, mario_vy, mario_enSaut, fini
    for event in pygame.event.get():
        if event.type == QUIT:
            fini = True
        elif event.type == KEYDOWN:
            if event.key == K_SPACE and mario_enSaut == False:
                mario_vy = -35
                mario_enSaut = True
        elif mario_vy == 0:
            mario_enSaut = False
    keys_pressed = pygame.key.get_pressed()
    mario_vx = (keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) * 5

def dessiner_map(fenetre, map):
    for j, ligne in enumerate(map):
        for i, case in enumerate(ligne):
            if case == 1:
                fenetre.blit(plateforme, (i*25, j*25))
            elif case == 2:
                fenetre.blit(sol, (i*25, j*25))

def from_coord_to_grid(mario_pos):
    mario_x, mario_y = mario_pos
    i = max(0, int(mario_x // 25))
    j = max(0, int(mario_y // 25))
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

def bloque_sur_collision(map, ancien_pos, nouv_pos, mario_vx, mario_vy):
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
            mario_vy = 0.0
        elif dy_correction == 0.0:
            nouv_rect.left += dx_correction
            mario_vx = 0.0
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
            mario_vy = 0.0
        elif dx_correction != 0.0:
            nouv_rect.left += dx_correction
            mario_vx = 0.0
    mario_x, mario_y = nouv_rect.topleft
    return mario_x, mario_y, mario_vx, mario_vy

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

def mise_a_jour_position_mario():
    global mario_x, mario_y, mario_vx, mario_vy, GRAVITE, map
    ancien_x, ancien_y = mario_x, mario_y
    mario_vy += GRAVITE
    mario_x += mario_vx
    mario_y += mario_vy
    mario_x, mario_y, mario_vx, mario_vy = bloque_sur_collision(map, (ancien_x, ancien_y), (mario_x, mario_y), mario_vx, mario_vy)
    if mario_x == 0:
        mario_x = FENETRE_LARGEUR - 35
    elif mario_x == FENETRE_LARGEUR - 30:
        mario_x = 5


#--- BOUCLE PRINCIPALE ---#


mario_enSaut = False
mario_x, mario_y = FENETRE_LARGEUR//2, FENETRE_HAUTEUR - 100
mario_vx, mario_vy = 0, 0

ennemi = entite(600, 10)
ennemi2 = entite(300, 20)

while not fini:
    traite_entrees()
    fenetre.blit(background, (0, 0))
    dessiner_map(fenetre, map)
    mise_a_jour_position_mario()
    ennemi.mise_a_jour_position_ennemi()
    ennemi2.mise_a_jour_position_ennemi()
    fenetre.blit(mario_image, (mario_x, mario_y))
    fenetre.blit(ennemi_image, (ennemi.x, ennemi.y))
    fenetre.blit(ennemi_image, (ennemi2.x, ennemi2.y))
    horloge.tick(30)
    pygame.display.flip()
    diagnostics()   ###TEST###
pygame.quit()
