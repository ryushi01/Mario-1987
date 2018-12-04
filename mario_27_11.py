import pygame
pygame.init()

#---CONSTANTES---#
NOIR = (0, 0, 0)
BLEU_ACIER = (70, 130, 180)
BRUN = (88, 41, 0)
ROUGE = (255, 0, 0)
FENETRE_LARGEUR = 800
FENETRE_HAUTEUR = 600

#---PARAMS---#
fenetre_taille = [FENETRE_LARGEUR, FENETRE_HAUTEUR]
fini = False
fenetre = pygame.display.set_mode(fenetre_taille)
horloge = pygame.time.Clock()
pygame.display.set_caption('MARIO')

#---CLASSES---#
class entite_mario():
    def __init__(self, x, y, largeur, hauteur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.x = x
        self.y = y
        self.en_saut = False
        self.compteur_saut = 10
        self.droite = False
        self.gauche = False
        self.compteur_marche = 0
        self.gravite_on = True
        self.compteur_gravite = 1.05
        self.position = [self.x, self.y]
        self.marcheDroite_1 = pygame.image.load('images/mario_marche_d2.png')
        self.marcheDroite_1 = pygame.transform.scale(self.marcheDroite_1, (self.largeur, self.hauteur))
        self.marcheDroite_2 = pygame.image.load('images/mario_marche_d1.png')
        self.marcheDroite_2 = pygame.transform.scale(self.marcheDroite_2, (self.largeur, self.hauteur))
        self.marcheDroite_3 = pygame.image.load('images/mario_marche_d3.png')
        self.marcheDroite_3 = pygame.transform.scale(self.marcheDroite_3, (self.largeur, self.hauteur))
        self.marcheGauche_1 = pygame.image.load('images/mario_marche_g2.png')
        self.marcheGauche_1 = pygame.transform.scale(self.marcheGauche_1, (self.largeur, self.hauteur))
        self.marcheGauche_2 = pygame.image.load('images/mario_marche_g1.png')
        self.marcheGauche_2 = pygame.transform.scale(self.marcheGauche_2, (self.largeur, self.hauteur))
        self.marcheGauche_3 = pygame.image.load('images/mario_marche_g3.png')
        self.marcheGauche_3 = pygame.transform.scale(self.marcheGauche_3, (self.largeur, self.hauteur))
        self.marcheDroite = [self.marcheDroite_1, self.marcheDroite_2, self.marcheDroite_1, self.marcheDroite_3, self.marcheDroite_1, self.marcheDroite_2,
                        self.marcheDroite_1, self.marcheDroite_3]
        self.marcheGauche = [self.marcheGauche_1, self.marcheGauche_2, self.marcheGauche_1, self.marcheGauche_3, self.marcheGauche_1, self.marcheGauche_2,
                        self.marcheGauche_1, self.marcheGauche_3]
        self.resteDroite = pygame.image.load('images/mario_statique_d.png')
        self.resteDroite = pygame.transform.scale(self.resteDroite, (self.largeur, self.hauteur))
        self.resteGauche = pygame.image.load('images/mario_statique_g.png')
        self.resteGauche = pygame.transform.scale(self.resteGauche, (self.largeur, self.hauteur))
        self.sautDroite = pygame.image.load('images/mario_saute_d.png')
        self.sautDroite = pygame.transform.scale(self.sautDroite, (self.largeur, self.hauteur))
        self.sautGauche = pygame.image.load('images/mario_saute_g.png')
        self.sautGauche = pygame.transform.scale(self.sautGauche, (self.largeur, self.hauteur))
    def dessin(self, fenetre):
        if self.compteur_marche + 1 >= 24:
            self.compteur_marche = 0
        if self.gauche and not self.en_saut:
            fenetre.blit(self.marcheGauche[self.compteur_marche // 3], (self.x, self.y))
            self.compteur_marche += 1
        elif self.droite and not self.en_saut:
            fenetre.blit(self.marcheDroite[self.compteur_marche // 3], (self.x, self.y))
            self.compteur_marche += 1
        elif self.droite and self.en_saut:
            fenetre.blit(self.sautDroite, (self.x, self.y))
            self.compteur_marche += 1
        elif self.gauche and self.en_saut:
            fenetre.blit(self.sautGauche, (self.x, self.y))
            self.compteur_marche += 1
        elif not self.gauche and not self.droite and self.en_saut:
            fenetre.blit(self.sautDroite, (self.x, self.y))

        else:
            fenetre.blit(self.resteDroite, (self.x, self.y))
        self.rect = pygame.Rect((self.x, self.y), (self.hauteur, self.largeur))

    def update(self):
        self.x = effet_pacman(self.x, self.largeur)
    def gravite(self):
        compteur_gravite = 1.05
        if self.gravite_on:
            self.y *= compteur_gravite



class entite_plateforme():
    def __init__(self, x, y, largeur, hauteur, couleur):
        self.hauteur = hauteur
        self.largeur = largeur
        self.x = x
        self.y = y
        self.couleur = couleur
        self.position = [self.x, self.y]
    def dessin(self):
        pygame.draw.rect(fenetre, self.couleur, ((self.x, self.y), (self.largeur, self.hauteur)))
        self.rect = pygame.Rect((self.x, self.y), (self.largeur, self.hauteur))

#---FONCTIONS---#
def acteurs():
    global mario, sol, plateforme1, plateforme2
    mario = entite_mario(30, FENETRE_HAUTEUR * 5/12, 30, 34)
    sol = entite_plateforme(0, FENETRE_HAUTEUR*10/12, FENETRE_LARGEUR, FENETRE_HAUTEUR*2/12, ROUGE)
    plateforme1 = entite_plateforme(-40, FENETRE_HAUTEUR*5/12, FENETRE_LARGEUR*5/12, 15, ROUGE)
    plateforme2 = entite_plateforme(FENETRE_LARGEUR-5/12*FENETRE_LARGEUR+40, FENETRE_HAUTEUR*5/12, FENETRE_LARGEUR*5/12, 15, ROUGE)

def systeme_collision():
    if mario.rect.colliderect(sol.rect) or mario.rect.colliderect(plateforme1.rect) or mario.rect.colliderect(plateforme2.rect):
        mario.gravite_on = False
    elif mario.en_saut:
        mario.gravite_on = False
    else: mario.gravite_on = True



def affiche():
    mario.dessin(fenetre)
    mario.update()
    mario.gravite()
    sol.dessin()
    plateforme1.dessin()
    plateforme2.dessin()
    systeme_collision()

def effet_pacman(position_entite_actuellex, entite_largeur):
    global FENETRE_LARGEUR
    if position_entite_actuellex > FENETRE_LARGEUR + entite_largeur:
        position_entite_actuellex = - entite_largeur
        return position_entite_actuellex
    elif position_entite_actuellex < - entite_largeur:
        position_entite_actuellex = FENETRE_LARGEUR + entite_largeur
        return position_entite_actuellex
    else:
        return position_entite_actuellex


def traite_entrees():
    global touche, fini
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fini = True
    touche = pygame.key.get_pressed()
    if touche[pygame.K_RIGHT]:
        mario.x += 5
        mario.droite = True
        mario.gauche = False
    elif touche[pygame.K_LEFT]:
        mario.x -= 5
        mario.gauche = True
        mario.droite = False
    else:
        mario.compteur_marche = 0
    if not (mario.en_saut):
        if touche[pygame.K_SPACE]:
            mario.en_saut = True
            mario.compteur_marche = 0
    else:
        if mario.compteur_saut >= -10:
            moins = 1
            if mario.compteur_saut < 0:
                moins = -1
            mario.y -= (mario.compteur_saut ** 2) * 0.35 * moins
            mario.compteur_saut -= 1
        else:
            mario.en_saut = False
            mario.compteur_saut = 10

#---BOUCLE PRINCIPALE---#
acteurs()
while not fini:
    traite_entrees()
    fenetre.fill(NOIR)
    affiche()
    pygame.display.flip()
    horloge.tick(30)

pygame.display.quit()
pygame.quit()
exit()
#---FIN PROGRAMME---#



