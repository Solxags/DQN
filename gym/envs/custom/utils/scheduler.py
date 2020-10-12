from gym.envs.custom.utils.config import output_logs
class Scheduler(object):
    def __init__(self, env, algorithm):
        self.env = env
        self.algorithm = algorithm
        self.simulation = None
        self.machine = None
        self.destroyed = False
        self.valid_pairs = {}

    def attach(self, simulation):
        self.simulation = simulation
        self.machine = simulation.machine

    def make_decision(self):
        while True:
            accelerator, task_instance = self.algorithm(self.machine, self.env.now)
            if accelerator is None or task_instance is None:
                break
            else:
                accelerator.running_task_instance = task_instance
                task_instance.started = True
                self.env.process(self.machine.run_task_instance(accelerator,task_instance))

    def run(self):
        while not self.simulation.finished:
            self.make_decision()
            if output_logs:
                self.machine.csv_saver.save(self.machine.state)
            else:
                print(self.machine.state)
            yield self.env.timeout(1)
        self.destroyed = True
