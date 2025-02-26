from TUEvolution.creatures import Creature
⋮
class App:
  ⋮
  def initialize(self):
  """
  Initialize the simulation.
  """
  ⋮
  # Population
  self.generation = 0
  self.creatures = [Creature(self.creature_radius, self.creature_speed, self.creature_stamina, utils.color('red')) for _ in range(self.population)]
  self.world.assign_homes(self.creatures)
  ⋮
# Specify the scenario
scenario = 'question1'
⋮
# Create simulation instance
app = App(population=scenario['world']['init']['population'],
          generations=scenario['simulation']['generations'],
          food_supply=scenario['world']['init']['food'],
          world_day=scenario['world']['day'],
          creature_size=scenario['creature']['size'],
          creature_speed=scenario['creature']['speed'],
          creature_stamina=scenario['creature']['stamina'])
⋮