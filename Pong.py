import pygame, sys, random, time
from pygame import mixer
mixer.init()
mixer.music.load(r"Underground Theme - NSMB + NSMBW Mashup.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()
def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time, winner_theme

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    
    if ball.left <=0:
        player_score += 1
        mixer.music.load(r"yt5s.com - HE HE HE HAW (Earrape) (128 kbps).mp3")
        mixer.music.set_volume(0.3)
        mixer.music.play()
        time.sleep(1.5)
        mixer.music.load(r"Underground Theme - NSMB + NSMBW Mashup.mp3")
        mixer.music.set_volume(0.5)
        mixer.music.play()
        if player_score == 7:
            mixer.music.load(r"Stage Win (Super Mario) - Sound Effect HD.mp3")
            mixer.music.set_volume(0.2)
            mixer.music.play()
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        opponent_score += 1
        mixer.music.load(r'Mario Death - Sound Effect (HD).mp3')
        mixer.music.set_volume(0.5)
        mixer.music.play()
        time.sleep(3)
        mixer.music.load(r"Underground Theme - NSMB + NSMBW Mashup.mp3")
        mixer.music.play()

        if opponent_score == 7:
            mixer.music.load(r"Game_Over_-_New_Super_Mario_Bros_Wii.mp3")
            mixer.music.set_volume(0.2)
            mixer.music.play()

        score_time = pygame.time.get_ticks()




    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)
#Timer
    if current_time - score_time < 1000:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))

    if 1000 < current_time - score_time < 2000:
        number_two = game_font.render("2", False, light_grey)
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))

    if 2000 < current_time - score_time < 3000:
        number_one = game_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))

    if current_time - score_time < 3000:
        ball_speed_x, ball_speed_y = 0, 0


    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None



pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')



bg_color = (17, 10, 33)
light_grey = (189, 45, 60)
winner = (232, 225, 28)

#Game Rectangles
ball = pygame.Rect(screen_width/2 -15, screen_height/2 - 15, 30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10,140)


#Game Variables
ball_speed_x = 10 * random.choice((-1,1))
ball_speed_y = 10 * random.choice((-1,1))
player_speed = 0
opponent_speed = 10


#Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)
final_font = pygame.font.Font("freesansbold.ttf", 100)

#Score Timer
score_time = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 10
            if event.key == pygame.K_UP:
                player_speed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 10
            if event.key == pygame.K_UP:
                player_speed += 10

    ball_animation()
    player_animation()
    opponent_animation()
    #Visuals:
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    if score_time:
        ball_restart()


    player_text = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(player_text, (660, 470))

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600, 470))

    objective_text = game_font.render("First one to 7", False, light_grey)
    screen.blit(objective_text, (700, 50))
  

    if player_score == 7:
        final_text = final_font.render("You win!!!", False, winner)
        screen.blit(final_text, (400, 450))
        final_score_text = game_font.render("Final Score: " + str(opponent_score) + " vs. " + str(player_score), False, winner)
        screen.blit(final_score_text, (480, 780))
        time.sleep(3)
    if opponent_score == 7:
        final_text = final_font.render("You Lose!!!", False, winner)
        screen.blit(final_text, (400, 450))
        final_score_text = game_font.render("Final Score: " + str(opponent_score) + " vs. " + str(player_score), False, winner)
        screen.blit(final_score_text, (480, 780))
        time.sleep(3)
    pygame.display.flip()


    clock.tick(60)
    if player_score == 7:
        time.sleep(5)
        quit()
    if opponent_score == 7:
        time.sleep(5)
        quit()