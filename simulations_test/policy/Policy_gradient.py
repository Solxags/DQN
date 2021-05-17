from simulations_test.policy.util.RL_brain import PolicyGradient
from simulations_test.policy.util.Schdule_env import Schdule_env
import numpy as np

class policy(object):
    def __init__(self):
        self.env = None
        self.RL = None

    def init_Policy_gradient(self,broker):
        self.env=Schdule_env(broker)
        self.RL = PolicyGradient(
                                    n_actions=self.env.n_actions,
                                    n_features=self.env.n_features ,
                                    learning_rate=0.02,
                                    reward_decay=0.99,
                                    # output_graph=True,
                                )


    def run(self,broker,machine):
        observation=broker.generate_task_machine_graph
        observation=observation.flatten()
        # RL choose action based on observation
        action = self.RL.choose_action(observation)
        task=broker.search_task_id(action)
        if task!=None:
            machine.env.process(machine.run_task(task))
            self.RL.store_transition(observation, action, 0)
        else:
            broker.free_machine_list.append(machine)
            self.RL.store_transition(observation, action, -1)
