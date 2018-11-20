import pygame

pygame.init()


#---CONSTANTES---#

NOIR = (0, 0, 0)
BLEU_ACIER = (70, 130, 180)
BRUN = (88, 41, 0)
ROUGE = (255, 0, 0)

FENETRE_LARGEUR = 800
FENETRE_HAUTEUR = 600
fenetre_taille = (FENETRE_LARGEUR, FENETRE_HAUTEUR)

#---CLASSES---#

class entite():
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

    def dessin(self,fenetre):
        if self.compteur_marche + 1 >= 24:
            self.compteur_marche = 0
        if self.gauche and not self.en_saut:
            fenetre.blit(marcheGauche[self.compteur_marche // 3], (self.x, self.y))
            self.compteur_marche += 1
        elif self.droite and not self.en_saut:
            fenetre.blit(marcheDroite[self.compteur_marche // 3], (self.x, self.y))
            self.compteur_marche += 1
        elif self.droite and self.en_saut:
            fenetre.blit(sautDroite, (self.x, self.y))
            self.compteur_marche += 1
        elif self.gauche and self.en_saut:
            fenetre.blit(sautGauche, (self.x, self.y))
            self.compteur_marche += 1
        elif not self.gauche and not self.droite and self.en_saut:
            fenetre.blit(sautDroite, (self.x, self.y))
        else:
            fenetre.blit(resteDroite, (self.x, self.y))

    def gravite(self):
        compteur_gravite = 1.05
        self.y *= compteur_gravite






#---AUTRES VARIABLE---#

fini = False
gravite = True

fenetre = pygame.display.set_mode(fenetre_taille)

horloge = pygame.time.Clock()

ancien_temps = 0

pygame.display.set_caption('MARIO')

mario = entite(10, FENETRE_HAUTEUR//5 - 34, 30, 34)


#---CHARGEMENT_IMAGES---#

# Mario

marcheDroite_1 = pygame.image.load('images/mario_marche_d2.png')
marcheDroite_1 = pygame.transform.scale(marcheDroite_1, (mario.largeur, mario.hauteur))

marcheDroite_2 = pygame.image.load('images/mario_marche_d1.png')
marcheDroite_2 = pygame.transform.scale(marcheDroite_2, (mario.largeur, mario.hauteur))

marcheDroite_3 = pygame.image.load('images/mario_marche_d3.png')
marcheDroite_3 = pygame.transform.scale(marcheDroite_3, (mario.largeur, mario.hauteur))


marcheGauche_1 = pygame.image.load('images/mario_marche_g2.png')
marcheGauche_1 = pygame.transform.scale(marcheGauche_1, (mario.largeur, mario.hauteur))

marcheGauche_2 = pygame.image.load('images/mario_marche_g1.png')
marcheGauche_2 = pygame.transform.scale(marcheGauche_2, (mario.largeur, mario.hauteur))

marcheGauche_3 = pygame.image.load('images/mario_marche_g3.png')
marcheGauche_3 = pygame.transform.scale(marcheGauche_3, (mario.largeur, mario.hauteur))

marcheDroite = [marcheDroite_1, marcheDroite_2, marcheDroite_1, marcheDroite_3, marcheDroite_1, marcheDroite_2, marcheDroite_1, marcheDroite_3]
marcheGauche = [marcheGauche_1, marcheGauche_2, marcheGauche_1, marcheGauche_3, marcheGauche_1, marcheGauche_2, marcheGauche_1, marcheGauche_3]

resteDroite = pygame.image.load('images/mario_statique_d.png')
resteDroite = pygame.transform.scale(resteDroite, (mario.largeur, mario.hauteur))

resteGauche = pygame.image.load('images/mario_statique_g.png')
resteGauche = pygame.transform.scale(resteGauche, (mario.largeur, mario.hauteur))

sautDroite = pygame.image.load('images/mario_saute_d.png')
sautDroite = pygame.transform.scale(sautDroite, (mario.largeur, mario.hauteur))

sautGauche = pygame.image.load('images/mario_saute_g.png')
sautGauche = pygame.transform.scale(sautGauche, (mario.largeur, mario.hauteur))

# Background

bg = pygame.image.load('images/bg.png')
bg = pygame.transform.scale(bg, (FENETRE_LARGEUR, FENETRE_HAUTEUR))

#---FONCTIONS---#

def gravite_mario():
    mario.gravite()

def affiche_mario():
    mario.dessin(fenetre)
    if gravite == True:
        gravite_mario()

def effet_pacman(position_entite_actuellex, entite_largeur):
    global FENETRE_LARGEUR
    if position_entite_actuellex > FENETRE_LARGEUR:
        position_entite_actuellex = 0
        return position_entite_actuellex
    elif position_entite_actuellex < 0:
        position_entite_actuellex = FENETRE_LARGEUR - entite_largeur
        return position_entite_actuellex
    else:
        return position_entite_actuellex

def dessine_plateformes():

    # 3eme etage

    plateforme_hauteur = 15
    plateforme_largeur = (FENETRE_LARGEUR/32)*14

    plateforme_positiong = [0, FENETRE_HAUTEUR/5]
    plateforme_positiond = [FENETRE_LARGEUR-plateforme_largeur, FENETRE_HAUTEUR/5]

    pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiong, (plateforme_largeur, plateforme_hauteur)))
    pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiond, (plateforme_largeur, plateforme_hauteur)))


    # 2eme etage

    # 2extremites

    plateforme_largeur2 = (FENETRE_LARGEUR/32)*4

    plateforme_positiong2 = [0, (FENETRE_HAUTEUR*2/5)+15]
    plateforme_positiond2 = [FENETRE_LARGEUR-plateforme_largeur2, (FENETRE_HAUTEUR*2/5)+15]

    pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiong2, (plateforme_largeur2, plateforme_hauteur)))
    pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiond2, (plateforme_largeur2, plateforme_hauteur)))

    # centre
    plateforme_largeur2b = (FENETRE_LARGEUR/32)*18



    plateforme_positionc2b = [plateforme_largeur2 + (FENETRE_LARGEUR/32)*3 ,(FENETRE_HAUTEUR*2/5)]

    pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positionc2b, (plateforme_largeur2b, plateforme_hauteur)))


    # 1er etage

    plateforme_largeur3 = (FENETRE_LARGEUR/32)*11

    plateforme_positiong3 = [0, (FENETRE_HAUTEUR*3/5)]
    plateforme_positiond3 = [FENETRE_LARGEUR - plateforme_largeur3, (FENETRE_HAUTEUR * 3/5)]

    pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiong3, (plateforme_largeur3, plateforme_hauteur)))
    pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiond3, (plateforme_largeur3, plateforme_hauteur)))

    # sol

    sol_hauteur = FENETRE_HAUTEUR/5
    sol_largeur = FENETRE_LARGEUR

    sol_position = [0, FENETRE_HAUTEUR*4/5]

    pygame.draw.rect(fenetre, BRUN, (sol_position, (sol_largeur, sol_hauteur)))





#---BOUCLE PRINCIPALE---#

while not fini:
    temps_maintenant = pygame.time.get_ticks()

    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fini = True

    mario.x = effet_pacman(mario.x, mario.largeur)
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

    if not(mario.en_saut):
        if touche[pygame.K_SPACE]:
            mario.en_saut = True
            mario.compteur_marche = 0
    else:
        if mario.compteur_saut >= -10:
            moins = 1
            if mario.compteur_saut < 0:
                moins = -1
            mario.y -= (mario.compteur_saut **2) * 0.2 * moins
            mario.compteur_saut -= 1

        else:
            mario.en_saut = False
            mario.compteur_saut = 10


    fenetre.fill(NOIR)
    dessine_plateformes()
    affiche_mario()
    pygame.display.flip()
    horloge.tick(24)

pygame.display.quit()
pygame.quit()
exit()

#---FIN PROGRAMME---#



