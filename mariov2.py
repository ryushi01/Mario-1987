import pygame, random, time

pygame.init()

#---CONSTANTES---#

NOIR = (0, 0, 0)
BLANC = (255, 255, 255)

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
        # Servira à gérer les suites d'images

        self.mort = False

        # IMAGES

        self.mario0d = pygame.image.load('images/mario0d.png')
        self.mario0d = pygame.transform.scale(self.mario0d, (self.largeur, self.hauteur))

        self.mario1d = pygame.image.load('images/mario1d.png')
        self.mario1d = pygame.transform.scale(self.mario1d, (self.largeur, self.hauteur))

        self.mariod = [self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d, self.mario0d, self.mario1d]
        # Permet l'animation de marche de mario (vers la droite)

        self.mario0g = pygame.image.load('images/mario0g.png')
        self.mario0g = pygame.transform.scale(self.mario0g, (self.largeur, self.hauteur))

        self.mario1g = pygame.image.load('images/mario1g.png')
        self.mario1g = pygame.transform.scale(self.mario1g, (self.largeur, self.hauteur))

        self.mariog = [self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g, self.mario0g, self.mario1g]
        # Permet l'animation de marche (vers la gauche)

        self.mariosg = pygame.image.load('images/mariosg.png')
        self.mariosg = pygame.transform.scale(self.mariosg, (self.largeur, self.hauteur))
        # Image de saut à gauche

        self.mariosd = pygame.image.load('images/mariosd.png')
        self.mariosd = pygame.transform.scale(self.mariosd, (self.largeur, self.hauteur))
        # Image de saut à droite

        self.mariomort = pygame.image.load('images/mariogameover.png')
        self.mariomort = pygame.transform.scale(self.mariomort, (self.largeur, self.hauteur))
        # Image quand mario meurt

    def affiche(self, fenetre):
        if self.compteurImage + 1 >= 32: # L'écran étant rafraichît toutes les 32 s (voir horloge.tick lignes 471 et 491)
            self.compteurImage = 0
        if self.gauche and not self.enSaut and self.mort == False:
            fenetre.blit(self.mariog[self.compteurImage // 2], (self.x, self.y))
            self.compteurImage += 1
            # Gére l'animation de marche vers la gauche
        elif self.droite and not self.enSaut and self.mort == False:
            fenetre.blit(self.mariod[self.compteurImage // 2], (self.x, self.y))
            self.compteurImage += 1
            # Gére l'animation de marche vers la droite
        elif self.droite and self.enSaut and self.mort == False:
            fenetre.blit(self.mariosd, (self.x, self.y))
            self.compteurImage += 1
            # Gére l'animation de saut vers la droite
        elif self.gauche and self.enSaut and self.mort == False:
            fenetre.blit(self.mariosg, (self.x, self.y))
            self.compteurImage += 1
            # Gére l'animation de saut vers la droite
        elif not self.gauche and self.droite and self.enSaut and self.mort == False:
            fenetre.blit(self.mariosd, (self.x, self.y))
            self.compteurImage += 1
            # Gére l'animation de saut vers la droite
        elif self.mort == True:
            fenetre.blit(self.mariomort, (self.x, self.y))
            # Gére l'animation de game over
        else:
            fenetre.blit(self.mario0d, (self.x, self.y))
        # pygame.draw.rect(fenetre, (255, 0, 0), self.rect, 2 # Permet d'afficher le rectangle entourant mario (la hitbox)

    def mise_a_jour_position(self):
        self.ancien_x, self.ancien_y = self.x, self.y

        self.vy += GRAVITE

        self.x += self.vx

        self.y += self.vy

        self.x, self.y, self.vx, self.vy = bloquer_si_collision_avec_plateforme(map, (self.ancien_x, self.ancien_y), (self.x, self.y), self.vx, self.vy)


        if self.x == 0:
            self.x = FENETRE_LARGEUR - 35
        elif self.x == FENETRE_LARGEUR - 30:
            self.x = 5

        self.rect = [self.x, self.y, 25, 25]


class ennemi():
    def __init__(self, x, y, largeur, hauteur):

        self.x = x
        self.y = y

        self.hauteur = hauteur
        self.largeur = largeur

        self.vx_negative = random.randint(-4,-1)
        self.vx_positive = random.randint(1, 4)
        self.aleatoire = random.randint(1,2)
        if self.aleatoire == 1:
            self.vx = self.vx_positive
        elif self.aleatoire == 2:
            self.vx = self.vx_negative
        self.vy = 0

        self.compteurImage = 0


        # IMAGES

        self.goombag = pygame.image.load('images/goombag.png')
        self.goombag = pygame.transform.scale(self.goombag, (self.largeur, self.hauteur))
        self.goombad = pygame.image.load('images/goombad.png')
        self.goombad = pygame.transform.scale(self.goombad, (self.largeur, self.hauteur))
        self.goombamort = pygame.image.load('images/goombamort.png')
        self.goombamort = pygame.transform.scale(self.goombamort, (self.largeur, self.hauteur))

        self.goomba = [self.goombag, self.goombad]

    def mise_a_jour_position(self):

        self.ancien_x, self.ancien_y = self.x, self.y

        self.vy += GRAVITE

        self.x += self.vx

        self.y += self.vy

        self.x, self.y, self.vx, self.vy = bloquer_si_collision_avec_plateforme(map, (self.ancien_x, self.ancien_y), (self.x, self.y), self.vx, self.vy)

        if self.vx == 0:
            self.vx == 3

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

        self.rect = [self.x, self.y, 25, 25]

    def affiche(self, fenetre):

        if self.compteurImage <= 4:
            self.image_en_cours = self.goombad
            self.compteurImage += 1
        elif self.compteurImage <= 8 and self.compteurImage > 4:
            self.image_en_cours = self.goombag
            self.compteurImage += 1
        else:
            self.compteurImage = 0
        fenetre.blit(self.image_en_cours, (self.x, self.y))
        #pygame.draw.rect(fenetre, (255, 0, 0), self.rect, 2) # Permet d'afficher le rectangle entourant un ennemi

#---FONCTIONS---#

def traite_entrees():
    global fini, intro, ennemis, score, son_saut, ennemis

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = True
            intro = False
        elif event.type == pygame.KEYDOWN and intro == True:
                intro = False
                fini = False
                mario.mort = False
                score = 0
                mario.droite = True
                mario.gauche = False
                ennemis = []
                mario.x = 25
                mario.y = 80
                mario.vx = 0
                mario.vy = 0
        elif event.type == pygame.KEYDOWN and intro == False:
            if event.key == pygame.K_SPACE and mario.enSaut == False and mario.mort == False:
                mario.vy = - 35
            elif event.key == pygame.K_r and mario.mort == True:
                mario.mort = False
                score = 0
                mario.droite = True
                mario.gauche = False
                ennemis = []
                mario.x = 25
                mario.y = 80
                mario.vx = 0
                mario.vy = 0
        elif event.type == nouvelennemi:
            generer_ennemi()
    touche_maintenue = pygame.key.get_pressed()
    if mario.vx > 0 and mario.mort == False:
        mario.droite = True
        mario.gauche = False
    if mario.vx < 0 and mario.mort == False:
        mario.gauche = True
        mario.droite = False
    if mario.vy < 0:
        mario.enSaut = True
    if mario.vy == 0 and mario.y != 175 and mario.y != 300 and mario.y != 325 and mario.y != 450:
        mario.enSaut = False
    if mario.vx == 0:
        mario.compteurImage = 0

    if mario.mort == False:
        mario.vx = (touche_maintenue[pygame.K_RIGHT] - touche_maintenue[pygame.K_LEFT]) * 5
    else:
        mario.vx = 0




def dessiner_map(fenetre, map):
    for j, ligne in enumerate(map):
        for i, case in enumerate(ligne):
            if case == 1:
                fenetre.blit(plateforme, (i*25, j*25))
            elif case == 2:
                fenetre.blit(sol, (i*25, j*25))

def coordonnees_vers_grille (pos):
    x, y = pos
    i = max(0, int(x // 25))
    j = max(0, int(y // 25))
    return i, j

def obtenir_cases_voisines(map, i_start, j_start):
    global i
    carres = []
    for j in range(j_start, j_start+2):
        for i in range(i_start, i_start+2):
            if map[j][i] == 1 or map[j][i] == 2:
                topleft = i*25, j*25
                carres.append(pygame.Rect((topleft), (25, 25)))
    return carres

def bloquer_si_collision_avec_plateforme(map, ancien_pos, nouv_pos, vx, vy):
    ancien_rect = pygame.Rect(ancien_pos, (25, 25))
    nouv_rect = pygame.Rect(nouv_pos, (25, 25))
    i, j = coordonnees_vers_grille (nouv_pos)
    collisions_futurs = []
    carres = obtenir_cases_voisines(map, i, j)
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


def collisions_entite():
    global fini, score, temps_spawn
    for goomba in ennemis:
        if mario.rect[1] < goomba.rect[1] and mario.rect[1] + mario.rect[3] >= goomba.rect[1] and mario.mort == False:
            if mario.rect[0] + mario.rect[2] > goomba.rect[0] and mario.rect[0] < goomba.rect[0] + goomba.rect[2]:
                ennemis.pop(ennemis.index(goomba))
                mario.vy = -25
                score += 100
                temps_spawn -= 20
                pygame.time.set_timer(nouvelennemi, temps_spawn)
        elif mario.rect[1] < goomba.rect[1] + goomba.rect[3] and mario.rect[1] + mario.rect[3] > goomba.rect[1]:
            if mario.rect[0] + mario.rect[2] > goomba.rect[0] and mario.rect[0] < goomba.rect[0] + goomba.rect[2]:
                mario.mort = True


def generer_ennemi():
    if mario.mort == True and len(ennemis) < 10:
        goomba = ennemi(random.randint(30, FENETRE_LARGEUR - 30), 0, 25, 25)
        ennemis.append(goomba)
    elif mario.mort == False and len(ennemis) < 50:
        goomba = ennemi(random.randint(30, FENETRE_LARGEUR - 30), 0, 25, 25)
        ennemis.append(goomba)


def affiche_entites():
    def affiche_ennemi():
        for goomba in ennemis:
            goomba.mise_a_jour_position()
            goomba.affiche(fenetre)
    def affiche_mario():
        mario.mise_a_jour_position()
        mario.affiche(fenetre)
    affiche_ennemi()
    affiche_mario()

def affiche_score():
    affichage_score = police.render("SCORE:", True, BLANC)
    affichage_score2 = police.render(str(score), True, BLANC)
    fenetre.blit(affichage_score, (10, 10))
    fenetre.blit(affichage_score2, (100, 10))

def affiche_intro():
    fenetre.fill(NOIR)
    titre = pygame.image.load('images/mario_titre.png')
    titre = pygame.transform.scale(titre, (300, 80))
    fenetre.blit(titre, (FENETRE_LARGEUR/2 - 150, 30))
    message = police.render("APPUYER SUR N'IMPORTE QUELLE TOUCHE POUR JOUER", True, BLANC)
    message_largeur, message_hauteur = police.size("APPUYER SUR N'IMPORTE QUELLE TOUCHE POUR JOUER")
    fenetre.blit(message, ((FENETRE_LARGEUR - message_largeur) // 2, 4 * FENETRE_HAUTEUR // 5))

def affiche_game_over():
    global intro
    if mario.mort == True and intro == False:
        message1 = police.render("GAME OVER !", True, BLANC)
        message1_largeur, message1_hauteur = police.size("GAME OVER !")
        fenetre.blit(message1, ((FENETRE_LARGEUR - message1_largeur) // 2, FENETRE_HAUTEUR  // 10))
        message2 = police.render("[R]ECOMMENCER", True, BLANC)
        message2_largeur, message2_hauteur = police.size("[R]ECOMMENCER")
        fenetre.blit(message2, ((FENETRE_LARGEUR - message2_largeur) // 2, 3 * FENETRE_HAUTEUR // 5 ))

def deplacements_artficiels():
    global ennemis
    if mario.mort == False:
        mario.vx = 5
        for goomba in ennemis:
            goomba.rect = [goomba.x, goomba.y, 25, 25]
            mario.rect = [mario.x, mario.y, 25, 25]
            if mario.rect[1] == goomba.rect[1]:
                if goomba.rect[0] - mario.rect[0] <= 40 and goomba.rect[0] - mario.rect[0] >= 0:
                    mario.vy = -35
        if mario.vy == 0:
            aleatoire = random.randint(1,50)
            if aleatoire == 10:
                mario.vy = -37
    if mario.mort == True:
        mario.y = 80
        mario.x = 25
        ennemis = []
        mario.mort = False


#---AUTRES VARIABLES---#

fini = True
intro = True

horloge = pygame.time.Clock()

pygame.display.set_caption('MARIO')

mario = joueur_principal(25, 80, 25, 25)
ennemis = []

score = 0
nouvelennemi = pygame.USEREVENT + 1
temps_spawn = 3000
pygame.time.set_timer(nouvelennemi, temps_spawn)

police = pygame.font.SysFont('monospace', FENETRE_HAUTEUR//25, True)
police_titre = pygame.font.SysFont('monospace', 50, True)

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


#--- BOUCLE PRINCIPALE ---#

while intro:

    affiche_intro()

    traite_entrees()

    dessiner_map(fenetre, map)

    deplacements_artficiels()

    affiche_entites()

    collisions_entite()

    horloge.tick(32)

    pygame.display.flip()

    while not fini:

        traite_entrees()

        fenetre.fill(NOIR)

        dessiner_map(fenetre, map)

        affiche_entites()

        collisions_entite()

        affiche_score()

        affiche_game_over()

        horloge.tick(32)

        pygame.display.flip()

pygame.quit()
