import simpy
from simulation_test import simulation
from schduler_test import schduler
from simulations_test.algorithms.first_fit import algorithm
from simulations_test.policy.Policy_gradient import policy
import matplotlib.pyplot as plt

# env = simpy.Environment()
# Algorithm=algorithm()
# Policy=policy()
# Schduler=schduler(Algorithm,Policy,env)
# Simulation=simulation(env,Schduler)
# Simulation.init_simulation()
# env.process(Simulation.run())
# env.run()

Algorithm=algorithm()
Policy=policy()
Schduler=schduler(Algorithm,Policy)
Simulation=simulation(env,Schduler)
Simulation.init_simulation()
Policy.init_Policy_gradient(Simulation.broker)
for i_episode in range(3000):
    Simulation.broker.reset()
    env.process(Simulation.run())
    env.run()
    reward=21382.5-Simulation.broker.total_finish_time/2
    Policy.RL.store_final_reward(reward)
    print("episode:", i_episode, "  reward:", int(reward))

    vt = Policy.RL.learn()

    if i_episode == 0:
        plt.plot(vt)  # plot the episode vt
        plt.xlabel('episode steps')
        plt.ylabel('normalized state-action value')
        plt.show()

