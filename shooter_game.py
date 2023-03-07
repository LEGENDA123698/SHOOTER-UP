#Створи власний Шутер!

from models import *


pygame.display.set_caption("Шутер")

background = pygame.transform.scale(pygame.image.load("galaxy.jpg"), WZ)
player = Player("rocket.png",10, WZ[0]/2, WZ[1] - pl_size[1])


pygame.mixer.init()
pygame.mixer.music.load("space.ogg")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()


win = font_message.render("YOU WIN!!!!", 1,(0,255,0))
lose = font_message.render("YOU LOSE!!!!", 1,(255,0,0))



enemies = pygame.sprite.Group()
for i in range(5):
    enemies.add(Enemy("ufo.png", randint(1,3),randint(0,WZ[0]-pl_size[0]),randint(-100,0),True))


asteroids = sprite.Group()
for i in range(3):
    asteroids.add(Enemy("asteroid.png", 1,randint(0,WZ[0]-pl_size[0]),randint(-100,0),False))





clock = pygame.time.Clock()
game = True
game_ower = False
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if not game_ower:
        window.blit(background,(0,0))

        enemies.draw(window)
        enemies.update()
        asteroids.draw(window)
        asteroids.update()

        player.update_position()
        player.reset()
        player.fire()

        bullets.draw(window)
        bullets.update()

        for bullet in bullets:
            for enemy in enemies:
                if pygame.sprite.collide_rect(bullet, enemy):
                    bullet.kill()
                    enemy.kill()
                    counter.kill()
                    enemies.add(Enemy("ufo.png", randint(1,3),randint(0,WZ[0]-pl_size[0]),randint(-100,0),True))
        sprite.groupcollide(bullets, asteroids, True, False)

        if counter.kill_enemy >= 10:
            game_ower = True
            window.blit(win, (WZ[0]/2,WZ[1]/2))
        elif counter.lost_enemy >= 3 or pygame.sprite.spritecollide(player,enemies,False) or sprite.spritecollide(player,asteroids,False):
            game_ower = True
            window.blit(lose, (WZ[0]/2,WZ[1]/2))
        
        counter.c_update(window)
        clock.tick(FPS)
        pygame.display.update()
        