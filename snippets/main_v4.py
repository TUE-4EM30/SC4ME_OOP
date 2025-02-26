import TUEvolution.utils as utils, TUEvolution.graphs as graphs
⋮
class App:
    """
    A class to represent the main application for the TU/evolution simulation.
    """
    ⋮
    def initialize(self):
        """
        Initialize the simulation.
        """
        ⋮
        # Graphs
        ⋮
        self.graphs = graphs.Cycler(left=self.sim_width,
                                    top=0,
                                    width=self.graph_width,
                                    height=self.graph_height,
                                    border=self.border,
                                    graphs=[self.population_graph, self.food_graph],
                                    font_size=self.font_size)

        ⋮ 
  ⋮