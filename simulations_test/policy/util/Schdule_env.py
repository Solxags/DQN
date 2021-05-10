import numpy
class Schdule_env(object):
    def __init__(self,broker):
        self.broker=broker
        self.action_space = self.broker.task_list
        self.n_actions = len(self.broker.task_list)
        self.n_features = (len(self.broker.machine_list)+1)*len(self.broker.task_list)

    def step(self, action,machine):
        action.machine_list.append(machine)