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

#---CHARGEMENT IMAGES---#
background = pygame.image.load('images/background2.png')
plateforme = pygame.image.load('images/platform2.png')
plateforme = pygame.transform.scale(plateforme, (25, 25))
sol = pygame.image.load('images/brick2.png')
sol = pygame.transform.scale(sol, (25, 25))

ennemi_image = pygame.image.load('images/goomba_face.png')
ennemi_image = pygame.transform.scale(ennemi_image, (25, 25))

###DEFINITION classe_ennemiS###
class classe_ennemi():
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
        ###coordonnees_vers_grille###
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

class joueur_principal():
    def __init__(self, x, y, largeur, hauteur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.enSaut = False
        self.droite = False
        self.gauche = False
        self.compteurImage = 0
        # IMAGES
        self.mario0d = pygame.image.load('images/mario0d.png')
        self.mario0d = pygame.transform.scale(self.mario0d, (self.largeur, self.hauteur))
        self.mario1d = pygame.image.load('images/mario1d.png')
        self.mario1d = pygame.transform.scale(self.mario1d, (self.largeur, self.hauteur))
        self.mario2d = pygame.image.load('images/mario2d.png')
        self.mario2d = pygame.transform.scale(self.mario2d, (self.largeur, self.hauteur))
        self.mario3d = pygame.image.load('images/mario3d.png')
        self.mario3d = pygame.transform.scale(self.mario3d, (self.largeur, self.hauteur))
        self.mariod = [self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d]
        self.mario0g = pygame.image.load('images/mario0g.png')
        self.mario0g = pygame.transform.scale(self.mario0g, (self.largeur, self.hauteur))
        self.mario1g = pygame.image.load('images/mario1g.png')
        self.mario1g = pygame.transform.scale(self.mario1g, (self.largeur, self.hauteur))
        self.mario2g = pygame.image.load('images/mario2g.png')
        self.mario2g = pygame.transform.scale(self.mario2g, (self.largeur, self.hauteur))
        self.mario3g = pygame.image.load('images/mario3g.png')
        self.mario3g = pygame.transform.scale(self.mario3g, (self.largeur, self.hauteur))
        self.mariog = [self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g]
        self.mariosg = pygame.image.load('images/mariosg.png')
        self.mariosg = pygame.transform.scale(self.mariosg, (self.largeur, self.hauteur))
        self.mariosd = pygame.image.load('images/mariosd.png')
        self.mariosd = pygame.transform.scale(self.mariosd, (self.largeur, self.hauteur))
    def affiche_joueur_principal(self, fenetre):
        if self.compteurImage + 1 >= 32:
            self.compteurImage = 0
        if self.gauche and not self.enSaut:
            fenetre.blit(self.mariog[self.compteurImage // 2], (self.x, self.y))
            self.compteurImage += 1
        elif self.droite and not self.enSaut:
            fenetre.blit(self.mariod[self.compteurImage // 2], (self.x, self.y))
            self.compteurImage += 1
        elif self.droite and self.enSaut:
            fenetre.blit(self.mariosd, (self.x, self.y))
            self.compteurImage += 1
        elif self.gauche and self.enSaut:
            fenetre.blit(self.mariosg, (self.x, self.y))
            self.compteurImage += 1
        elif not self.gauche and not self.droite and self.enSaut:
            fenetre.blit(self.mariosd, (self.x, self.y))
        else: fenetre.blit(self.mario0d, (self.x, self.y))
    def mise_a_jour_position(self):
        self.ancien_x, self.ancien_y = self.x, self.y
        self.vy += GRAVITE
        self.x += self.vx
        self.y += self.vy
        self.x, self.y, self.vx, self.vy = bloque_sur_collision(map, (self.ancien_x, self.ancien_y), (self.x, self.y), self.vx, self.vy)
        if self.x <= 10:
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
        print("Mario pos x :", mario_x, "pos y :", mario_y)
        print("Delai apparition monstres :", temps_spawn)

def traite_entrees():
    global fini, score, temps_spawn
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = True
        elif event.type == nouveauennemi:
            generer_ennemi()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and mario.enSaut == False:
                mario.vy = -35
                mario.enSaut = True
            if event.key == pygame.K_g:
                generer_ennemi()
                score += 100
                temps_spawn += 25
    touche_maintenue = pygame.key.get_pressed()
    if touche_maintenue[pygame.K_RIGHT]:
        mario.droite = True
        mario.gauche = False
    if touche_maintenue[pygame.K_LEFT]:
        mario.gauche = True
        mario.droite = False
    if mario.vy == 0 and mario.y != 175 and mario.y != 300 and mario.y != 325 and mario.y != 450:
        mario.enSaut = False
    if mario.vx == 0:
        mario.compteurImage = 0
    mario.vx = (touche_maintenue[pygame.K_RIGHT] - touche_maintenue[pygame.K_LEFT]) * 5

def dessiner_map(fenetre, map):
    for j, ligne in enumerate(map):
        for i, case in enumerate(ligne):
            if case == 1:
                fenetre.blit(plateforme, (i*25, j*25))
            elif case == 2:
                fenetre.blit(sol, (i*25, j*25))

def coordonnees_vers_grille(mario_pos):
    mario_x, mario_y = mario_pos
    i = max(0, int(mario_x // 25))
    j = max(0, int(mario_y // 25))
    return i, j

def recuperer_blocs_voisins(map, i_start, j_start):
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
    i, j = coordonnees_vers_grille(nouv_pos)
    collision_future = []
    blocks = recuperer_blocs_voisins(map, i, j)
    for block in blocks:
        if not nouv_rect.colliderect(block):
            continue
        dx_correction, dy_correction = calculer_penetration(block, ancien_rect, nouv_rect)
        if dx_correction == 0.0:
            nouv_rect.top += dy_correction
            mario_vy = 0.0
        elif dy_correction == 0.0:
            nouv_rect.left += dx_correction
            mario_vx = 0.0
        else:
            collision_future.append(block)
    for block in collision_future:
        dx_correction, dy_correction = calculer_penetration(block, ancien_rect, nouv_rect)
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

def calculer_penetration(block, ancien_rect, nouv_rect):
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

def generer_ennemi():
    global temps_spawn
    ennemi = classe_ennemi(random.randint(25, FENETRE_LARGEUR - 25), 25)
    liste_ennemi.append(ennemi)
    temps_spawn -= 50
    pygame.time.set_timer(nouveauennemi, temps_spawn)

def affichage_acteurs():
    def affichage_ennemi():
        for ennemi in liste_ennemi:
            ennemi.mise_a_jour_position_ennemi()
            fenetre.blit(ennemi_image, (ennemi.x, ennemi.y))
    def affichage_mario():
        mario.mise_a_jour_position()
        mario.affiche_joueur_principal(fenetre)
    affichage_mario()
    affichage_ennemi()

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
mario = joueur_principal(25, 80, 25, 25)
while not fini:
    temps_ecoule = time.clock()
    traite_entrees()
    fenetre.blit(background, (0, 0))
    dessiner_map(fenetre, map)
    dessiner_infos()
    affichage_acteurs()
    horloge.tick(30)
    pygame.display.flip()
    diagnostics()
pygame.quit()
