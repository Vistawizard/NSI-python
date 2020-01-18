from pygame import*

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

# initialise le score des joueurs
scoreA = 0
scoreB = 0

clock = time.Clock()

font = font.Font(None, 74)

while continuer:
    time.Clock().tick(200)
    for evenements in event.get():
        if evenements.type == QUIT:
            continuer = 0
    
    keys = key.get_pressed()
    if keys[K_UP]: Yp2 -= 1
    if keys[K_DOWN]: Yp2 += 1
    if keys[K_w]: Yp1 -= 1
    if keys[K_s]: Yp1 += 1
    fenetre.blit(back,(0,0))
    fenetre.blit(perso1,(Xp1,Yp1))
    fenetre.blit(perso2,(Xp2,Yp2))
    
    #changer pour s'arreter et reset a la position si le joueur pert ou gagne
    if Rect((Xb, Yb),ball.get_size()).colliderect(Rect((Xp1, Yp1),perso1.get_size())) or Rect((Xb, Yb),ball.get_size()).colliderect(Rect((Xp2, Yp2),perso1.get_size())):
        vx = -vx
    if Yb == 499:
        vy = -vy
    Xb += vx
    Yb += vy
    
    fenetre.blit(ball,(Xb, Yb))
        
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