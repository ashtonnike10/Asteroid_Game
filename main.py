# allows code from open-source pygame library
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from weapon import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # groups
    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()

    # containers
    Player.containers = (update_group, draw_group)
    Asteroid.containers = (asteroid_group, update_group, draw_group)
    AsteroidField.containers = (update_group)
    Shot.containers = (shots_group, update_group, draw_group)

    # objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        # adds exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0)) # screen RBG code
        update_group.update(dt) # moves player

        for asteroid in asteroid_group:
            if player.collides(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots_group:
                if asteroid.collides(shot):
                    shot.kill()
                    asteroid.split()

        # re-render the player on the screen each frame
        for sprite in draw_group:
            sprite.draw(screen)

        # refresh the screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000  # Convert seconds to milliseconds

if __name__ == "__main__":
    main()