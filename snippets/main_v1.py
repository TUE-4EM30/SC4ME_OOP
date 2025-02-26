import pygame
⋮
class App:
    ⋮
    def execute(self):
        """
        Execute the main loop of the simulation.
        """
        self.initialize()

        clock = pygame.time.Clock()
        while self._running:
            self.check_events()
            self.update()
            self.render()
            clock.tick(self.fps)

        self.cleanup()
    ⋮

if __name__ == "__main__":
    ⋮
    # Run the simulation
    app.execute()