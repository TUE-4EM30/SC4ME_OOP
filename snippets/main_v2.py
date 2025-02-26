import pathlib
import toml
⋮
if __name__ == "__main__":

  # Specify the scenario
  scenario = 'question1'

  # Load the scenario
  scenario_file = pathlib.Path(__file__).resolve() \
    .parent.parent / 'scenarios' / f'{scenario}.toml'
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