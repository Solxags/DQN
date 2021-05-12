class Schdule_env(object):
    def __init__(self,broker):
        self.n_actions = len(broker.task_list)
        self.n_features = (len(broker.machine_list)+1)*len(broker.task_list)

    def step(self, task,machine):
        task.machine_list.append(machine)