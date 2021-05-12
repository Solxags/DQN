import simpy
from simulation_test import simulation
from schduler_test import schduler
from simulations_test.algorithms.first_fit import algorithm
from simulations_test.policy.Policy_gradient import policy
# from policy.fair import policy
import matplotlib.pyplot as plt

# env = simpy.Environment()
# Algorithm=algorithm()
# Policy=policy()
# Schduler=schduler(Algorithm,Policy)
# Simulation=simulation(env,Schduler)
# Simulation.init_simulation()
# env.process(Simulation.run())
# env.run()

Algorithm=algorithm()
Policy=policy()
Schduler=schduler(Algorithm,Policy)
env = simpy.Environment()
Simulation=simulation(env,Schduler)
Simulation.init_simulation()
Policy.init_Policy_gradient(Simulation.broker)
for i_episode in range(300):
    env.process(Simulation.run())
    env.run()
    reward=-Simulation.broker.total_finish_time/8
    Policy.RL.store_final_reward(reward)
    print("episode:", i_episode, "  reward:", int(reward))

    vt = Policy.RL.learn()

    # plt.plot(vt)  # plot the episode vt
    # plt.xlabel('episode steps')
    # plt.ylabel('normalized state-action value')
    # plt.show()
    env = simpy.Environment()
    Simulation = simulation(env, Schduler)
    Simulation.init_simulation()


