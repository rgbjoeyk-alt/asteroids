import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              return
        screen.fill("black")
        updatable.update(dt)
        for thing in asteroids:
            if player.collides_with(thing):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for thing in asteroids:
            for shot in shots:
                if thing.collides_with(shot):
                    log_event("asteroid_shot")
                    thing.kill()
                    shot.kill()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
