import pygame
import numpy
import toml
import pathlib

import TUEvolution.utils as utils, TUEvolution.graphs as graphs
from TUEvolution.map import World, Food
from TUEvolution.creatures import Creature

class App:
    """
    A class to represent the main application for the TU/evolution simulation.
    """

    def __init__(self, *, population, generations, food_supply, world_day, creature_size, creature_speed, creature_stamina):
        """
        Initialize the App object.

        Parameters:
        population (int): The initial population of creatures.
        generations (int): The number of generations to simulate.
        food_supply (int): The amount of food available in the world.
        world_day (int): The duration of a day in the world.
        creature_size (int): The size of the creatures.
        creature_speed (int): The speed of the creatures.
        creature_stamina (int): The stamina of the creatures.
        """
        self.name = "TU/evolution"

        # Screen layout
        # +------------+------------+
        # |            |            |
        # | Simulation |   Graph    |
        # |            |    ...     |
        # +------------+------------+

        self.sim_width = 600
        self.sim_height = 600
        self.graph_width = 600
        self.graph_height = 600
        self.font_size = 16
        self.size = (self.sim_width+self.graph_width, self.sim_height)

        # World
        self.world_day = world_day
        self.border = 20
        self.food_radius = 4

        # Creature
        self.creature_radius = creature_size//2
        self.creature_speed = creature_speed
        self.creature_stamina = creature_stamina

        # Frame rate
        self.fps = 30

        # Simulation
        self.population = population
        self.generations = generations
        self.food_supply = food_supply

    def initialize(self):
        """
        Initialize the simulation.
        """
        # Pygame
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.name)

        # World
        self.world = World(center=(self.sim_width//2,)*2,
                           radius=self.sim_width//2-self.border,
                           homes_width=4*self.creature_radius,
                           day=self.world_day)

        # Population
        self.generation = 0
        self.creatures = [Creature(self.creature_radius, self.creature_speed, self.creature_stamina, utils.color('red')) for _ in range(self.population)]
        self.world.assign_homes(self.creatures)

        # Food
        self.food = []
        for position in self.world.get_food_locations(self.food_supply):
            self.food.append(Food(position, self.food_radius, utils.color('forestgreen')))

        # Time
        self.time = 0

        # Graphs
        self.population_graph = graphs.XY(xlabel='Generations',
                                          ylabel='Population',
                                          xticks=numpy.arange(self.generations+1),
                                          yticks=self.generations,
                                          linecolor=utils.color('red'),
                                          fontsize=self.font_size)
        self.population_graph.add((self.generation,len(self.creatures)))

        self.food_graph = graphs.XY(xlabel='Generations',
                                    ylabel='Food',
                                    xticks=numpy.arange(self.generations+1),
                                    yticks=self.generations,
                                    linecolor=utils.color('forestgreen'),
                                    fontsize=self.font_size)
        self.food_graph.add((self.generation,len(self.food)))

        self.graphs = graphs.Cycler(left=self.sim_width,
                                    top=0,
                                    width=self.graph_width,
                                    height=self.graph_height,
                                    border=self.border,
                                    graphs=[self.population_graph, self.food_graph],
                                    font_size=self.font_size)

        self._running = True

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

    def check_events(self):
        """
        Check for and handle events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB: # Cycle through the graphs
                    if pygame.key.get_pressed()[pygame.K_LSHIFT] or pygame.key.get_pressed()[pygame.K_RSHIFT]:
                        self.graphs.previous()
                    else:
                        self.graphs.next()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.graphs.get_hovered()!=-1: # Activate the graph corresponding to the clicked bullet
                        self.graphs.active = self.graphs.get_hovered()

    def update(self):
        """
        Update the state of the simulation.
        """
        # Move the creatures
        self.world.increment_time()
        for creature in self.creatures:
            if creature.is_home() or creature.has_perished():
                continue
            creature.move()

        # Actions
        for creature in self.creatures:
            if creature.is_home() or creature.has_perished():
                continue

            if creature.energy<0:
                creature.perish()
                continue

            # Collect food until two food has been collected
            for f in range(len(self.food)-1,-1,-1):
                food = self.food[f]
                if(creature.is_hungry() and
                   sum((food.position-creature.position)**2)<=(creature.radius+food.radius)**2):
                    creature.food+=1
                    self.food.pop(f)

            # Eat other creature
            for prey in self.creatures:
                if not creature.is_hungry():
                    break

                if creature.radius<1.2*prey.radius:
                    continue

                if( prey.is_alive() and 
                    sum(prey.position-creature.position)**2<=(creature.radius+prey.radius)**2):
                    creature.food+=1
                    prey.perish()

            # Check whether to go home
            if creature.is_exploring():
                if (creature.food==2 or (creature.food==1 and creature.home_out_of_reach(self.world))):
                    creature.call_home(self.world)

            # Move away from the edge of the world
            if self.world.touches_edge(creature):
                orientation = numpy.arctan2(*numpy.flip(numpy.array(self.world.center)-numpy.array(creature.position)))
                creature.set_state(creature.position, orientation)
                creature.update_destination(reorient=False)

        # End of day/generation check
        if (self.world.end_of_day() or 
            all((creature.is_home() or creature.has_perished()) for creature in self.creatures)):
            
            self.world.next_day()
            self.creatures = [creature for creature in self.creatures if creature.is_home()]

            # Next generation
            if self.generation<self.generations:

                self.generation += 1
                next_generation = []
                for creature in self.creatures:
                    next_generation.append(creature.reincarnate())
                    if creature.food==2:
                        next_generation.append(creature.reproduce())
                self.creatures = next_generation

                self.population=len(self.creatures)
                self.world.assign_homes(self.creatures)

                # Add food
                for position in self.world.get_food_locations(self.food_supply):
                    self.food.append(Food(position, self.food_radius, utils.color('forestgreen')))

                # Update graphs
                self.population_graph.add((self.generation,len(self.creatures)))
                self.food_graph.add((self.generation,len(self.food)))

    def render(self):
        """
        Render the simulation on the screen.
        """
        # Background
        self.screen.fill(utils.color('white'))

        # World
        self.world.draw(self.screen)

        # Food
        for food in self.food:
            food.draw(self.screen)

        # Creatures
        for creature in self.creatures:
            if creature.is_alive():
                creature.draw(self.screen)

        # Graphs
        self.graphs.draw(self.screen)

        # Update the Pygame display
        pygame.display.update()

    def cleanup(self):
        """
        Clean up resources and quit Pygame.
        """
        pygame.quit()

if __name__ == "__main__":

    # Specify the scenario
    scenario = 'default'

    # Load the scenario
    scenario_file = pathlib.Path(__file__).resolve().parent.parent / 'scenarios' / f'{scenario}.toml'
    scenario = toml.load(scenario_file)

    # Create simulation instance
    app = App(population=scenario['world']['init']['population'],
              generations=scenario['simulation']['generations'],
              food_supply=scenario['world']['init']['food'],
              world_day=scenario['world']['day'],
              creature_size=scenario['creature']['size'],
              creature_speed=scenario['creature']['speed'],
              creature_stamina=scenario['creature']['stamina'])
    
    # Run the simulation
    app.execute()