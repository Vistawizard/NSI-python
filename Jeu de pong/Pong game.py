# ajouter une limite au boost et une barre de recharge
# Ajouter un saving grace (Teleporte automatiquement vers la balle)
# Ajouter de la vitesse a la balle qui va plus rapidement le plus long le jeu va
# Reparer le bug avec la balle qui desside ou pas de sortir

from pygame import*
from playsound import playsound
import random

mixer.pre_init(44100,16,2,4096)


init()
BLANC = (255,255,255)
fenetre = display.set_mode((888, 499), RESIZABLE)
back = image.load("back.jpg").convert()
fenetre.blit(back,(0,0))
display.set_caption("Jeu de Pong")
display.flip()
ball = image.load("ball.png").convert_alpha()
perso1 = image.load("perso1.png").convert_alpha()
perso2 = image.load("perso2.png").convert_alpha()

for x in range(ball.get_size()[0]):
    for y in range(ball.get_size()[1]):
        [r,v,b,t] = ball.get_at((x,y))
        if r+v+b >= 750:
            ball.set_at((x,y),(0,0,0,0))
for x in range(perso1.get_size()[0]):
    for y in range(perso1.get_size()[1]):
        [r,v,b,t] = perso1.get_at((x,y))
        if r+v+b >= 750:
            perso1.set_at((x,y),(0,0,0,0))
for x in range(perso2.get_size()[0]):
    for y in range(perso2.get_size()[1]):
        [r,v,b,t] = perso2.get_at((x,y))
        if r+v+b >= 750:
            perso2.set_at((x,y),(0,0,0,0))
            
continuer = 1
Xb = 444
Yb = 10
Yp1 = 100
Yp2 = 100
Xp1 = 10
Xp2 = 750
vx = 5
vy = 5

#ajouter 16 son
rater = ['Nulgermain.mp3', 'Match.mp3', 'Match_1.mp3', 'Yeuxlaid.mp3', 'paye.mp3', 'Ongagne.mp3', 'tapette.mp3', 'Oui.mp3']

# initialise le score des joueurs
scoreA = 0
scoreB = 0

clock = time.Clock()

#Score/Screen font
font = font.Font(None, 74)

mute = False

#Nombre de point pour arreter le jeu
point = 4

# Musique de font
mixer.music.load('backmusic.mp3')
mixer.music.set_volume(0.4)
mixer.music.play(-1)

black=(0,0,0)
end_it=False
while (end_it==False):
    fenetre.fill(black)
    nlabel=font.render("Welcome "+"Players", 1, (230, 0, 0))
    Instructions = font.render("Press m to mute sound",  1, (255, 255, 0))
    Joueur1 = font.render("wasd controls for player 1",  1, (130, 255, 0))
    Joueur2 = font.render("Arrows control for player 2",  1, (130, 255, 130))
    for eventss in event.get():
        if eventss.type==MOUSEBUTTONDOWN:
            end_it=True
    fenetre.blit(nlabel,(20,50))
    fenetre.blit(Instructions,(30,100))
    fenetre.blit(Joueur1,(40,150))
    fenetre.blit(Joueur2,(50,200))
    display.flip()


while continuer:
    time.Clock().tick(200)
    for evenements in event.get():
        if evenements.type == QUIT:
            continuer = 0
    if scoreA >= point:
        gagnant = str('A')
    if scoreB >= point:
        gagnant = str('B')
    if scoreA >= point or scoreB >= point:
        fin = font.render(str('Joueur {} a gagner'.format(gagnant)), 1, BLANC)
        fenetre.blit(fin, (222,249))
        display.flip()
        time.delay(5000) # Attend 5 seconde
        continuer = 0 # Arrete le jeu
        
    
    
    keys = key.get_pressed()
    if keys[K_m]: mute = True
    if keys[K_UP]: Yp2 -= 1
    if keys[K_DOWN]: Yp2 += 1
    if keys[K_w]: Yp1 -= 1
    if keys[K_s]: Yp1 += 1
    #Boost, a rajouter une limite a l'utilisation
    if keys[K_a]: Yp1 -= 10
    if keys[K_d]: Yp1 += 10
    if keys[K_LEFT]: Yp2 -= 10
    if keys[K_RIGHT]: Yp2 += 10
    
    #Ne laisse pas toucher les bords
    if Yp1 <= 0:
        Yp1 = 0
    if Yp2 <= 0:
        Yp2 = 0
    if Yp1 >= 327: #499 - la taille du joueur
        Yp1 = 327
    if Yp2 >= 327:
        Yp2 = 327
        
    fenetre.blit(back,(0,0))
    fenetre.blit(perso1,(Xp1,Yp1))
    fenetre.blit(perso2,(Xp2,Yp2))
    
    #changer pour s'arreter et reset a la position si le joueur pert ou gagne
    if Rect((Xb, Yb),ball.get_size()).colliderect(Rect((Xp1, Yp1),perso1.get_size())) or Rect((Xb, Yb),ball.get_size()).colliderect(Rect((Xp2, Yp2),perso1.get_size())):
        vx = -vx
        
    if Yb >= 444:
        Xb += 1
        vy = -vy
    if Yb <= 0:
        Xb += 1        
        vy = -vy
    Xb += vx
    Yb += vy
    
    fenetre.blit(ball,(Xb, Yb))
    son = random.choice(rater)
    if Xb <= 0:
        scoreB += 1
        Xb = 444
        Yb = 10
        if mute == False:
            mixer.music.set_volume(0.1)
            playsound(son)
            mixer.music.set_volume(0.5)
            rater.remove(son)
        
    if Xb >= 888:
        son = random.choice(rater)
        scoreA += 1
        Xb = 444
        Yb = 10
        if mute == False:
            mixer.music.set_volume(0.1)
            playsound(son)
            mixer.music.set_volume(0.5)
            rater.remove(son)

        
    #dessine les limites
    draw.line(fenetre, BLANC, [444, 0], [444, 500], 5)
    
    # Ajout au score
    text = font.render(str(scoreA), 1, BLANC)
    fenetre.blit(text, (350,10))
    text = font.render(str(scoreB), 1, BLANC)
    fenetre.blit(text, (500,10))
    
    display.flip()
    
    clock.tick(60)
quit()