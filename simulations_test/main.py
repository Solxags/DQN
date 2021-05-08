import simpy
from simulation_test import simulation
from schduler_test import schduler
from simulations_test.algorithms.first_fit import algorithm
from policy_test import policy

env = simpy.Environment()
Algorithm=algorithm()
Policy=policy()
Schduler=schduler(Algorithm,Policy,env)
Simulation=simulation(env,Schduler)
Simulation.init_simulation()
env.process(Simulation.run())
env.run()