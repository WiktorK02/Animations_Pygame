import pygame
import os

#pygame screen window
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#aniamtions declarations 

#stationary animation
stationary = [None]*15
for picIndex in range(0,15):
    stationary[picIndex-1] = pygame.image.load(os.path.join("animation_stay", "stay" + str(picIndex) + ".png"))
    stationary[picIndex-1] = pygame.transform.scale(stationary[picIndex-1], (120, 120))
    picIndex+=1

#stationary_left animation
stationary_left = [None]*15
for picIndex in range(0,15):
    stationary_left[picIndex-1] = pygame.image.load(os.path.join("animation_stay_left", "stay_left" + str(picIndex) + ".png"))
    stationary_left[picIndex-1] = pygame.transform.scale(stationary_left[picIndex-1], (120, 120))
    picIndex+=1

#run_left animation
left = [None]*8
for picIndex in range(0,8):
    left[picIndex-1] = pygame.image.load(os.path.join("animation_run_left", "run" + str(picIndex) + ".png"))
    left[picIndex-1] = pygame.transform.scale(left[picIndex-1], (160, 120))
    picIndex+=1

#run_left animation
right = [None]*8
for picIndex in range(0,8):
    right[picIndex-1] = pygame.image.load(os.path.join("animation_run_right", "run" + str(picIndex) + ".png"))
    right[picIndex-1] = pygame.transform.scale(right[picIndex-1], (160, 120))
    picIndex+=1

#jump_left animation
jump_right = [None]*10
for picIndex in range(0,10):
    jump_right[picIndex-1] = pygame.image.load(os.path.join("animation_jump", "jump" + str(picIndex) + ".png"))
    jump_right[picIndex-1] = pygame.transform.scale(jump_right[picIndex-1], (120, 120))
    picIndex+=1

#jump_left animation
jump_left = [None]*5
for picIndex in range(0,5):
    jump_left[picIndex-1] = pygame.image.load(os.path.join("animation_jump_left", "jump" + str(picIndex) + ".png"))
    jump_left[picIndex-1] = pygame.transform.scale(jump_left[picIndex-1], (120, 120))
    picIndex+=1

#starting pos
x = 250
y = 250

#velocity
vel = 10

#starting animation bool
move_left = False
move_right = False
animation_jump_right = False
animation_jump_left = False
stay_right = True
stay_left = False

stepIndex = 0
direction ='' #to help accurate with the direction (is it left or right)
isJump = False
jumpCount = 10

#draw the Game
def draw_game():
    global stepIndex
    screen.fill('Black')
    if stepIndex >= 28:
        stepIndex = 0
    if move_left:
        screen.blit(left[stepIndex//4], (x, y))
        stepIndex += 1
    elif animation_jump_left:
        screen.blit(jump_left[stepIndex//6], (x,y))
        stepIndex += 1
    elif animation_jump_right:
        screen.blit(jump_right[stepIndex//4], (x,y))
        stepIndex += 1
    elif move_right:
        screen.blit(right[stepIndex//4], (x,y))
        stepIndex += 1
    elif stay_right:
        screen.blit(stationary[stepIndex//2], (x,y))
        stepIndex += 1
    elif stay_left:
        screen.blit(stationary_left[stepIndex//2], (x,y))
        stepIndex += 1
    
#main Loop
run = True
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    
    #key detection
    if keys[pygame.K_LEFT]: 
        x -= vel
        direction = 'left'
        move_left = True
        move_right = False
        animation_jump_right= False
        animation_jump_left = True
    
    elif keys[pygame.K_RIGHT]:  
        x += vel
        direction = 'right'
        move_left = False
        move_right = True
        animation_jump_right = False
        animation_jump_left = False
    else: 
        move_left = False
        move_right = False
        animation_jump_right = False
        animation_jump_left = False
        if direction == 'left':
            stay_right = False
            stay_left = True
        else:
            stay_right = True
            stay_left = False
    
    if not(isJump):
        
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5 
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False
            
    #cancel run aniamtion while jump
    if isJump == True:
        move_left = False
        move_right = False
        if direction == 'left':
            animation_jump_left = True
            animation_jump_right = False
        else:
            animation_jump_left = False
            animation_jump_right = True

    draw_game()

    pygame.time.delay(30)
    pygame.display.update()
