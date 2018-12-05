import pygame
from pygame.locals import *
import random

pygame.init()

DEBUG_MODE = False

#---CONSTANTES---#
NOIR = (0, 0, 0)
BLEU_ACIER = (70, 130, 180)
BRUN = (88, 41, 0)
ROUGE = (255, 0, 0)
VERT =(0, 255, 0)
ALEATOIRE = (((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))))

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
        self.vx_random = random.randint(-3, 3)
        if self.vx_random == 0:
            self.vx_random = 1
    def mise_a_jour_position_ennemi(self):
        self.ancien_x, self.ancien_y = self.x, self.y
        self.vy += GRAVITE
        self.x += self.vx
        self.y += self.vy
        self.x, self.y, self.vx, self.vy = bloque_sur_collision(map, (self.ancien_x, self.ancien_y), (self.x, self.y), self.vx, self.vy)
        self.vx = self.vx_random
        if self.x <= 0:
            self.x = FENETRE_LARGEUR - 35
        elif self.x >= FENETRE_LARGEUR - 35:
            self.x = 10

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
          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],]

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


ennemi1 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi2 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi3 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi4 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi5 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi6 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi7 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi8 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi9 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi10 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi11 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi12 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi13 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi14 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi15 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi16 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi17 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi18 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi19 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi20 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi21 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi22 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi23 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi24 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi25 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi26 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi27 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi28 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi29 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
ennemi30 = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)

while not fini:
    traite_entrees()
    fenetre.blit(background, (0, 0))
    dessiner_map(fenetre, map)
    mise_a_jour_position_mario()
    fenetre.blit(mario_image, (mario_x, mario_y))

    ennemi1.mise_a_jour_position_ennemi()
    ennemi2.mise_a_jour_position_ennemi()
    ennemi3.mise_a_jour_position_ennemi()
    ennemi4.mise_a_jour_position_ennemi()
    ennemi5.mise_a_jour_position_ennemi()
    ennemi6.mise_a_jour_position_ennemi()
    ennemi7.mise_a_jour_position_ennemi()
    ennemi8.mise_a_jour_position_ennemi()
    ennemi9.mise_a_jour_position_ennemi()
    ennemi10.mise_a_jour_position_ennemi()
    ennemi11.mise_a_jour_position_ennemi()
    ennemi12.mise_a_jour_position_ennemi()
    ennemi13.mise_a_jour_position_ennemi()
    ennemi14.mise_a_jour_position_ennemi()
    ennemi15.mise_a_jour_position_ennemi()
    ennemi16.mise_a_jour_position_ennemi()
    ennemi17.mise_a_jour_position_ennemi()
    ennemi18.mise_a_jour_position_ennemi()
    ennemi19.mise_a_jour_position_ennemi()
    ennemi20.mise_a_jour_position_ennemi()
    ennemi21.mise_a_jour_position_ennemi()
    ennemi22.mise_a_jour_position_ennemi()
    ennemi23.mise_a_jour_position_ennemi()
    ennemi24.mise_a_jour_position_ennemi()
    ennemi25.mise_a_jour_position_ennemi()
    ennemi26.mise_a_jour_position_ennemi()
    ennemi27.mise_a_jour_position_ennemi()
    ennemi28.mise_a_jour_position_ennemi()
    ennemi29.mise_a_jour_position_ennemi()
    ennemi30.mise_a_jour_position_ennemi()

    fenetre.blit(ennemi_image, (ennemi1.x, ennemi1.y))
    fenetre.blit(ennemi_image, (ennemi2.x, ennemi2.y))
    fenetre.blit(ennemi_image, (ennemi3.x, ennemi3.y))
    fenetre.blit(ennemi_image, (ennemi4.x, ennemi4.y))
    fenetre.blit(ennemi_image, (ennemi5.x, ennemi5.y))
    fenetre.blit(ennemi_image, (ennemi6.x, ennemi6.y))
    fenetre.blit(ennemi_image, (ennemi7.x, ennemi7.y))
    fenetre.blit(ennemi_image, (ennemi8.x, ennemi8.y))
    fenetre.blit(ennemi_image, (ennemi9.x, ennemi9.y))
    fenetre.blit(ennemi_image, (ennemi10.x, ennemi10.y))
    fenetre.blit(ennemi_image, (ennemi11.x, ennemi11.y))
    fenetre.blit(ennemi_image, (ennemi12.x, ennemi12.y))
    fenetre.blit(ennemi_image, (ennemi13.x, ennemi13.y))
    fenetre.blit(ennemi_image, (ennemi14.x, ennemi14.y))
    fenetre.blit(ennemi_image, (ennemi15.x, ennemi15.y))
    fenetre.blit(ennemi_image, (ennemi16.x, ennemi16.y))
    fenetre.blit(ennemi_image, (ennemi17.x, ennemi17.y))
    fenetre.blit(ennemi_image, (ennemi18.x, ennemi18.y))
    fenetre.blit(ennemi_image, (ennemi19.x, ennemi19.y))
    fenetre.blit(ennemi_image, (ennemi20.x, ennemi20.y))
    fenetre.blit(ennemi_image, (ennemi21.x, ennemi21.y))
    fenetre.blit(ennemi_image, (ennemi22.x, ennemi22.y))
    fenetre.blit(ennemi_image, (ennemi23.x, ennemi23.y))
    fenetre.blit(ennemi_image, (ennemi24.x, ennemi24.y))
    fenetre.blit(ennemi_image, (ennemi25.x, ennemi25.y))
    fenetre.blit(ennemi_image, (ennemi26.x, ennemi26.y))
    fenetre.blit(ennemi_image, (ennemi27.x, ennemi27.y))
    fenetre.blit(ennemi_image, (ennemi28.x, ennemi28.y))
    fenetre.blit(ennemi_image, (ennemi29.x, ennemi29.y))
    fenetre.blit(ennemi_image, (ennemi30.x, ennemi30.y))

    horloge.tick(30)
    pygame.display.flip()
    diagnostics()   ###TEST###
pygame.quit()
