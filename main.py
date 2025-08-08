from asteroidfield import *
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize Variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    initial_x = SCREEN_WIDTH / 2
    initial_y = SCREEN_HEIGHT / 2

    # Initialize Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)

    # Initialize Player
    player = Player(initial_x, initial_y)    
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)

        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                return
            
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()
                    print("gotem!")
             
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
