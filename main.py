import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids,drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    
    x = SCREEN_WIDTH /2
    y = SCREEN_HEIGHT /2
    player = Player(x, y)
    def __init__(self, x, y):
        self.x = SCREEN_WIDTH /2
        self.y = SCREEN_HEIGHT /2
    
    asteroidfield = AsteroidField()

    dt = 0.0
    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill("black")
        updatable.update(dt)
        for draws in drawable:
            player.draw(screen)
            for aster in asteroids:
                aster.draw(screen)
            for shot in shots:
                shot.draw(screen)
        for aster in asteroids:
            for shot in shots:
                if aster.collides_with(shot):
                    log_event("asteroid_shot")
                    aster.split()
                    shot.kill()
            if aster.collides_with(player):
                log_event("player_hit")
                print("")
                print("Game over!")
                print("")
                sys.exit()
        

        pygame.display.flip()
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()

#uv run main.py