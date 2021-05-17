import simpy
from simulation_test import simulation
from schduler_test import schduler
from simulations_test.algorithms.first_fit import algorithm
from simulations_test.policy.Policy_gradient import policy
# from policy.all_to_one import policy
import matplotlib.pyplot as plt

task_train_path= '/home/ssego/DQN/simulations_test/tasks_train'
task_test_path= '/home/ssego/DQN/simulations_test/tasks_test'

# env = simpy.Environment()
# Algorithm=algorithm()
# Policy=policy()
# Schduler=schduler(Algorithm,Policy)
# Simulation=simulation(env,Schduler)
# Simulation.init_simulation(task_test_path)
# env.process(Simulation.run())
# env.run()

Algorithm=algorithm()
Policy=policy()
Schduler=schduler(Algorithm,Policy)
env = simpy.Environment()
Simulation=simulation(env,Schduler)
Simulation.init_simulation(task_train_path)
Policy.init_Policy_gradient(Simulation.broker)
time=[]
for i_episode in range(150):
    env.process(Simulation.run())
    env.run()
    time.append(Simulation.broker.total_finish_time/8)
    reward=38-((Simulation.broker.total_finish_time/8)/1000)
    Policy.RL.store_final_reward(reward)
    print("episode:", i_episode, "  reward:", int(reward))

    vt = Policy.RL.learn()

    # plt.plot(vt)  # plot the episode vt
    # plt.xlabel('episode steps')
    # plt.ylabel('normalized state-action value')
    # plt.show()
    env = simpy.Environment()
    Simulation = simulation(env, Schduler)
    Simulation.init_simulation(task_train_path)
plt.plot(time)  # plot the episode vt
plt.xlabel('episode steps')
plt.ylabel('normalized state-action value')
plt.show()
env = simpy.Environment()
Simulation = simulation(env, Schduler)
Simulation.init_simulation(task_test_path)
env.process(Simulation.run())
env.run()


