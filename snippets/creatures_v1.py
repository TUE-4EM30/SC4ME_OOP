⋮
# Creature class
class Creature:
  def __init__(self, radius, speed, stamina, color):
    """
    Initialize a Creature object.
    """
    ⋮
  ⋮  
  def reproduce(self):
    """
    Reproduce a new creature with slight variations.

    Returns:
    Creature: A new creature with slightly varied attributes.
    """
    Δradius = 0
    Δspeed = 0

    return Creature(self.radius+Δradius, \
      self.speed+Δspeed, self.stamina, self.color)
  ⋮