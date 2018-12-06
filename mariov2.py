import pygame

pygame.init()

#---CONSTANTES---#

NOIR = (0, 0, 0)

FENETRE_LARGEUR = 800
FENETRE_HAUTEUR = 600
FENETRE_TAILLE = [FENETRE_LARGEUR, FENETRE_HAUTEUR]
fenetre = pygame.display.set_mode(FENETRE_TAILLE)

GRAVITE = 4

#---CLASSES---#

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

    def affiche_mario(self, fenetre):
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
        else:
            fenetre.blit(self.mario0d, (self.x, self.y))

    def mise_a_jour_position(self):
        self.ancien_x, self.ancien_y = self.x, self.y

        self.vy += GRAVITE

        self.x += self.vx

        self.y += self.vy

        self.x, self.y, self.vx, self.vy = bloquer_si_collision_avec_decor(map, (self.ancien_x, self.ancien_y), (self.x, self.y), self.vx, self.vy)






#---AUTRES VARIABLES---#

fini = False

horloge = pygame.time.Clock()

pygame.display.set_caption('MARIO')

mario = joueur_principal(25, 80, 24, 30)

plateforme = pygame.image.load('images/platform.png')
plateforme = pygame.transform.scale(plateforme, (25, 25))


sol = pygame.image.load('images/brick.png')
sol = pygame.transform.scale(sol, (25, 25))



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
    global fini

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and mario.enSaut == False:
                mario.vy = -35
                mario.enSaut = True

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

def effet_pacman_mario():
    if mario.x == 0:
        mario.x = FENETRE_LARGEUR - 35
    elif mario.x == FENETRE_LARGEUR - 30:
        mario.x = 5

def coordonnees_vers_grille (pos):
    x, y = pos
    i = max(0, int(x // 25))
    j = max(0, int(y // 25))
    return i, j

def obtenir_carres_voisins (map, i_start, j_start):
    global i
    carres = []
    for j in range(j_start, j_start+2):
        for i in range(i_start, i_start+2):
            if map[j][i] == 1 or map[j][i] == 2:
                topleft = i*25, j*25
                carres.append(pygame.Rect((topleft), (25, 25)))
    return carres

def bloquer_si_collision_avec_decor(map, ancien_pos, nouv_pos, vx, vy):
    ancien_rect = pygame.Rect(ancien_pos, (25, 25))
    nouv_rect = pygame.Rect(nouv_pos, (25, 25))
    i, j = coordonnees_vers_grille (nouv_pos)
    collisions_futurs = []
    carres = obtenir_carres_voisins (map, i, j)
    for block in carres:
        if not nouv_rect.colliderect(block):
            continue
        dx_correction, dy_correction = ameliorer_precision(block, ancien_rect, nouv_rect)
        if dx_correction == 0.0:
            nouv_rect.top += dy_correction
            vy = 0.0
        elif dy_correction == 0.0:
            nouv_rect.left += dx_correction
            vx = 0.0
        else:
            collisions_futurs.append(block)
    for block in collisions_futurs:
        dx_correction, dy_correction = ameliorer_precision(block, ancien_rect, nouv_rect)
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

def ameliorer_precision(block, ancien_rect, nouv_rect):
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

def mise_a_jour_position():
    mario.mise_a_jour_position()

def affiche_entite():
    mario.affiche_mario(fenetre)






#--- BOUCLE PRINCIPALE ---#

while not fini:

    traite_entrees()

    fenetre.fill(NOIR)

    dessiner_map(fenetre, map)

    mise_a_jour_position()

    effet_pacman_mario()

    affiche_entite()

    horloge.tick(32)

    pygame.display.flip()

pygame.quit()
