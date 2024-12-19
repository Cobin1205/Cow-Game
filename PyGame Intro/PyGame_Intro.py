import pygame 
import random
from sys import exit

pygame.init()

canvas = pygame.display.set_mode((800, 400))  #Create window with size 800x400
pygame.display.set_caption("Window")      #Name window
clock = pygame.time.Clock()

game_active = True

#Grass
grass_surf1 = pygame.image.load(r"C:\Users\bliss\source\repos\Pygame Intro\PyGame Intro\grass.png").convert_alpha()
grass_surf1 = pygame.transform.scale(grass_surf1, (450, 25))
grass_rect1 = grass_surf1.get_rect(bottomright = (0, 300))

grass_surf2 = pygame.image.load(r"C:\Users\bliss\source\repos\Pygame Intro\PyGame Intro\grass.png").convert_alpha()
grass_surf2 = pygame.transform.scale(grass_surf2, (450, 25))
grass_rect2 = grass_surf2.get_rect(bottomright = (400, 300))

grass_surf3 = pygame.image.load(r"C:\Users\bliss\source\repos\Pygame Intro\PyGame Intro\grass.png").convert_alpha()
grass_surf3 = pygame.transform.scale(grass_surf3, (450, 25))
grass_rect3 = grass_surf3.get_rect(bottomright = (800, 300))

grass_surf4 = pygame.image.load(r"C:\Users\bliss\source\repos\Pygame Intro\PyGame Intro\grass.png").convert_alpha()
grass_surf4 = pygame.transform.scale(grass_surf4, (450, 25))
grass_rect4 = grass_surf4.get_rect(bottomright = (1200, 300))

grass = pygame.Surface((800, 100))
grass.fill("#62bc2f")

#Cow
cow_surf = pygame.image.load(r"C:\Users\bliss\source\repos\PyGame Intro\PyGame Intro\Cow.png").convert_alpha()
cow_surf = pygame.transform.scale(cow_surf, (70, 70))
cow = cow_surf.get_rect(midbottom = (100, 300))

cow_gravity = 0
pVel = 3

#Enemy
enemy_surf = pygame.image.load(r"C:\Users\bliss\source\repos\PyGame Intro\PyGame Intro\hayBale.png").convert_alpha()
enemy_surf = pygame.transform.scale(enemy_surf, (70, 70))
enemy = enemy_surf.get_rect(midbottom = (700, 300))
speed = 5

#Game Over Text
go_font = pygame.font.Font(None, 75)
go_surf = go_font.render("Game Over", True, "Black", None)
go_rect = go_surf.get_rect(center = (400, 200))

ps_font = pygame.font.Font(None, 30)
ps_surf = ps_font.render("Press Space to Continue", True, "Black", None)
ps_rect = ps_surf.get_rect(center = (400, 250))

#Health Bar
health_surf = pygame.Surface((200, 20))
health_surf.fill("Red")
health = 5
healthText_font = pygame.font.Font(None, 30)
healthText_surf = healthText_font.render("Health", True, (150,0,0), None)

#Score
scores = [0]
score = 0
score_font = pygame.font.Font(None, 30)
score_surf = score_font.render("Score: ", True, "Black", None)
high_score = score_font.render("High Score: ", True, "Black", None)


while True:

    canvas.fill("#96e2ee")
   
    #Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            exit(0)
            SystemExit(0)

        
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and cow.bottom >= 300 and game_active:
                    cow_gravity = -17
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                cow.left = 100
                enemy.left = 800
                speed = 5
                health = 5
                scores.append(score)
                score = 0
            

    if game_active:

        #Grass
        canvas.blit(grass, (0,300))
        canvas.blit(grass_surf1, grass_rect1)
        canvas.blit(grass_surf2, grass_rect2)
        canvas.blit(grass_surf3, grass_rect3)
        canvas.blit(grass_surf4, grass_rect4)
        grass_rect1.x -= speed
        grass_rect2.x -= speed
        grass_rect3.x -= speed
        grass_rect4.x -= speed

        if(grass_rect1.right <= 0):
            grass_rect1.left = 800
        if(grass_rect2.right <= 0):
            grass_rect2.left = 800
        if(grass_rect3.right <= 0):
            grass_rect3.left = 800
        if(grass_rect4.right <= 0):
            grass_rect4.left = 800

        #Enemy
        canvas.blit(enemy_surf, enemy)

        #Cow
        cow.y += cow_gravity
        cow_gravity += 1
        if(cow.bottom >= 300):
            cow.bottom = 300
        canvas.blit(cow_surf, cow)

        #Health Bar
        canvas.blit(health_surf, (10, 10))
        health_surf = pygame.transform.scale(health_surf, (health*60, 20))
        canvas.blit(healthText_surf, (15, 10))

        #Score
        canvas.blit(score_surf, (10, 75))
        score_surf = score_font.render("Score: " + str(score), True, "Black", None)
        score += 1
        canvas.blit(high_score, (10, 50))
        high_score = score_font.render("High Score: " + str(max(scores)), True, "Black", None)

        #Player movement
        
        """keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            cow.x -= pVel
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            cow.x += pVel"""
        

        #Enemy Movement
        enemy.x -= speed
        speed += 0.01
        if(enemy.right <= 0):
            enemy.left = 800

        #Get Hit
        if(cow.colliderect(enemy)):
            health -= 1
            enemy.left = 800
            
        #Die
        if health <= 0:
            game_active = False

    else:
        canvas.blit(go_surf, go_rect)
        canvas.blit(ps_surf, ps_rect)

    pygame.display.update()
    clock.tick(60)     #Don't run faster than 60fps