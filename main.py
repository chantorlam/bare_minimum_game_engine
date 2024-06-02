import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("Bare Minimum Game Engine with Physics")

# Define colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define a simple physics object (ball)
class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = RED
        self.vx = 0  # velocity in x direction
        self.vy = 0  # velocity in y direction
        self.ax = 0  # acceleration in x direction
        self.ay = 0.5  # acceleration in y direction (gravity)

    def update(self):
        # Update velocity with acceleration
        self.vx += self.ax
        self.vy += self.ay
        
        # Update position with velocity
        self.x += self.vx
        self.y += self.vy

        # Handle collision with window boundaries
        if self.x - self.radius < 0 or self.x + self.radius > SCREEN_WIDTH:
            self.vx = -self.vx  # Reverse velocity in x direction
            self.x = max(self.radius, min(self.x, SCREEN_WIDTH - self.radius))
        
        if self.y - self.radius < 0 or self.y + self.radius > SCREEN_HEIGHT:
            self.vy = -self.vy  # Reverse velocity in y direction
            self.y = max(self.radius, min(self.y, SCREEN_HEIGHT - self.radius))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Main game loop
def main():
    clock = pygame.time.Clock()
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 20)

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update game state
        ball.update()
        
        # Draw everything
        screen.fill(BLACK)  # Fill the screen with black color
        ball.draw(screen)  # Draw the ball
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
