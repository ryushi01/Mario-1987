
import pygame

pygame.init()

#---CONSTANTES---#

NOIR = (0, 0, 0)
BLEU_ACIER = (70, 130, 180)
BRUN = (88, 41, 0)
ROUGE = (255, 0, 0)

FENETRE_LARGEUR = 800
FENETRE_HAUTEUR = 600
fenetre_taille = [FENETRE_LARGEUR, FENETRE_HAUTEUR]

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

        self.gravite_on = True
        self.compteur_gravite = 1.05

        # CHARGEMENT_IMAGES

        # Mario

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

    def update(self):
        self.position = [self.x, self.y]
        self.rect = pygame.Rect(self.position, (self.largeur, self.hauteur))

    def dessine_plateformes_et_gravite(self):

        # 3EME ETAGE

        plateforme_hauteur = 15
        plateforme_largeur = (FENETRE_LARGEUR / 32) * 14

        plateforme_positiong = [0, FENETRE_HAUTEUR / 5]
        plateforme_positiond = [FENETRE_LARGEUR - plateforme_largeur, FENETRE_HAUTEUR / 5]

        pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiong, (plateforme_largeur, plateforme_hauteur)))
        pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiond, (plateforme_largeur, plateforme_hauteur)))

        # 2EME ETAGE

        # 2 EXTREMITES

        plateforme_largeur2 = (FENETRE_LARGEUR / 32) * 4

        plateforme_positiong2 = [0, (FENETRE_HAUTEUR * 2 / 5) + 15]
        plateforme_positiond2 = [FENETRE_LARGEUR - plateforme_largeur2, (FENETRE_HAUTEUR * 2 / 5) + 15]

        pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiong2, (plateforme_largeur2, plateforme_hauteur)))
        pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiond2, (plateforme_largeur2, plateforme_hauteur)))

        # CENTRE

        plateforme_largeur2b = (FENETRE_LARGEUR / 32) * 18

        plateforme_positionc2b = [plateforme_largeur2 + (FENETRE_LARGEUR / 32) * 3, (FENETRE_HAUTEUR * 2 / 5)]

        pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positionc2b, (plateforme_largeur2b, plateforme_hauteur)))

        # 1ER ETAGE

        plateforme_largeur3 = (FENETRE_LARGEUR / 32) * 11

        plateforme_positiong3 = [0, (FENETRE_HAUTEUR * 3 / 5)]
        plateforme_positiond3 = [FENETRE_LARGEUR - plateforme_largeur3, (FENETRE_HAUTEUR * 3 / 5)]

        pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiong3, (plateforme_largeur3, plateforme_hauteur)))
        pygame.draw.rect(fenetre, BLEU_ACIER, (plateforme_positiond3, (plateforme_largeur3, plateforme_hauteur)))

        plateforme_g3_rect = pygame.Rect(plateforme_positiong3, (plateforme_largeur3, plateforme_hauteur))
        plateforme_d3_rect = pygame.Rect(plateforme_positiond3, (plateforme_largeur3, plateforme_hauteur))

        # SOL

        sol_hauteur = FENETRE_HAUTEUR / 5
        sol_largeur = FENETRE_LARGEUR

        sol_position = [0, FENETRE_HAUTEUR * 4 / 5]

        pygame.draw.rect(fenetre, BRUN, (sol_position, (sol_largeur, sol_hauteur)))

        sol_rect = pygame.Rect(sol_position, (sol_hauteur, sol_largeur))

        # GRAVITE

        if self.rect.colliderect(plateforme_g3_rect) or self.rect.colliderect(sol_rect):
            self.gravite_on = False
            print('no')
        else:
            self.gravite_on = True
            print('yes')

        if self.gravite_on == True:
            self.compteur_gravite = 1.05
            self.y *= self.compteur_gravite


#---FONCTIONS---#

def affiche():
    mario.dessine_plateformes_et_gravite()
    mario.dessin(fenetre)


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

def mario_saut():

    if not(mario.en_saut):
        if touche[pygame.K_SPACE]:
            mario.en_saut = True
            mario.compteur_marche = 0

    else:
        if mario.compteur_saut >= -10:
            moins = 1
            if mario.compteur_saut < 0:
                moins = -1
            mario.y -= (mario.compteur_saut **2) * 0.35 * moins
            mario.compteur_saut -= 1

        else:
            mario.en_saut = False
            mario.compteur_saut = 10

#---AUTRES VARIABLE---#

fini = False

fenetre = pygame.display.set_mode(fenetre_taille)

horloge = pygame.time.Clock()

ancien_temps = 0

pygame.display.set_caption('MARIO')

mario = entite(10, FENETRE_HAUTEUR*2/5 - 34, 30, 34)

#---BOUCLE PRINCIPALE---#

while not fini:

    traite_entrees()
    mario.update()
    mario_saut()
    fenetre.fill(NOIR)
    affiche()
    pygame.display.flip()
    horloge.tick(24)

pygame.display.quit()
pygame.quit()
exit()

#---FIN PROGRAMME---#



