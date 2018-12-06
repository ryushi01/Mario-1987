import pygame
from pygame.locals import *
import random
import time
import math

DEBUG_MODE = False

#---CONSTANTES---#
NOIR = (0, 0, 0)
BLEU_ACIER = (70, 130, 180)
BRUN = (88, 41, 0)
ROUGE = (255, 0, 0)
VERT =(0, 255, 0)
BLANC =(255, 255, 255)
ALEATOIRE = (((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255))))
FENETRE_LARGEUR = 800
FENETRE_HAUTEUR = 600
FENETRE_TAILLE = [FENETRE_LARGEUR, FENETRE_HAUTEUR]
fenetre = pygame.display.set_mode(FENETRE_TAILLE)
GRAVITE = 4

#---AUTRES VARIABLES---#
temps_ecoule = 0
score = 0
fini = False
horloge = pygame.time.Clock()
nouveauennemi = pygame.USEREVENT + 1
temps_spawn = 7500
pygame.time.set_timer(nouveauennemi, temps_spawn)
pygame.display.set_caption('MARIO')
liste_ennemi = []

#---INITIALISER MARIO---#
mario_enSaut = False
mario_x, mario_y = FENETRE_LARGEUR//2, FENETRE_HAUTEUR - 100
mario_vx, mario_vy = 0, 0

#---CHARGEMENT IMAGES---#
background = pygame.image.load('images/background2.png')
plateforme = pygame.image.load('images/platform2.png')
plateforme = pygame.transform.scale(plateforme, (25, 25))
sol = pygame.image.load('images/brick2.png')
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
        if self.x <= 10:
            if self.y == 525 and self.x <= 10:
                self.x = FENETRE_LARGEUR - 35
                self.y = 125
            else: self.x = FENETRE_LARGEUR - 35
        elif self.x >= FENETRE_LARGEUR - 35:
            if self.y == 525 and self.x >= FENETRE_LARGEUR - 35:
                self.x = 10
                self.y = 125
            else: self.x = 10

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
        print("Mario pos x :", mario_x, "pos y :", mario_y)
        print("Delai apparition monstres :", temps_spawn)

def traite_entrees():
    global mario_x, mario_y, mario_vx, mario_vy, mario_enSaut, fini, score, temps_spawn
    for event in pygame.event.get():
        if event.type == QUIT:
            fini = True
        elif event.type == KEYDOWN:
            if event.key == K_SPACE and mario_enSaut == False:
                mario_vy = -35
                mario_enSaut = True
            if event.key == pygame.K_g:
                generer_ennemi()
                score += 100
                temps_spawn += 25
        elif event.type == nouveauennemi:
            generer_ennemi()
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

def generer_ennemi():
    global temps_spawn
    ennemi = entite(random.randint(25, FENETRE_LARGEUR - 25), 25)
    liste_ennemi.append(ennemi)
    temps_spawn -= 50
    pygame.time.set_timer(nouveauennemi, temps_spawn)
def affichage_ennemi():
    for ennemi in liste_ennemi:
        ennemi.mise_a_jour_position_ennemi()
        fenetre.blit(ennemi_image, (ennemi.x, ennemi.y))

def dessiner_infos():
    global affichage_score, affichage_score2, affichage_temps, temps_spawn
    police = pygame.font.SysFont('monospace', 24, True)
    affichage_score = police.render("Score:", True, BLANC)
    affichage_score2 = police.render(str(score), True, BLANC)
    affichage_temps = police.render("Time:", True, BLANC)
    affichage_temps2 = police.render(str(math.trunc(temps_ecoule)), True, BLANC)
    affichage_spawntime = police.render("Spawntime:", True, BLANC)
    affichage_spawntime2 = police.render(str(temps_spawn), True, BLANC)
    fenetre.blit(affichage_score, (10, 10))
    fenetre.blit(affichage_score2, (92, 10))
    fenetre.blit(affichage_spawntime, (FENETRE_LARGEUR//2, 10))
    fenetre.blit(affichage_spawntime2, (FENETRE_LARGEUR//2+138, 10))
    fenetre.blit(affichage_temps, (FENETRE_LARGEUR - 132, 10))
    fenetre.blit(affichage_temps2, (FENETRE_LARGEUR - 64, 10))

#--- BOUCLE PRINCIPALE ---#
pygame.init()
while not fini:
    temps_ecoule = time.clock()
    traite_entrees()
    fenetre.blit(background, (0, 0))
    dessiner_map(fenetre, map)
    dessiner_infos()
    mise_a_jour_position_mario()
    fenetre.blit(mario_image, (mario_x, mario_y))
    affichage_ennemi()
    horloge.tick(30)
    pygame.display.flip()
    diagnostics()
pygame.quit()
