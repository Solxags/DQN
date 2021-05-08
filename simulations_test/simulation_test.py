from  broker_test import broker
from task_test import task_list_generator
from machine_test import machine_list_generator
import os
task_path= '/home/ssego/DQN/simulations_test/tasks'

class simulation(object):
    def __init__(self,env,schduler):
        self.env=env
        self.broker=None
        self.schduler=schduler

    def init_simulation(self):
        self.broker=broker(self.env,self.schduler)
        Task_list=task_list_generator(task_path,self.env)
        self.broker.commit_task_list(Task_list)
        Machine_list=machine_list_generator(self.env)
        self.broker.register_machine_list(Machine_list)

    def run(self):
        self.schduler.machine2task(self.broker)
        while True:
            for task in self.broker.running_task_list:
                if task.finished == True:
                    print("Task Finished!")
                    task.task_start_flag == False
                    task.task_finish_flag == True
                    self.broker.running_task_list.remove(task)
                else:
                    if task.is_waiting==True:
                        for machine in task.machine_list:
                            for accelerator in machine.accelerator_list:
                                if accelerator.running_task_instance==None:
                                    self.schduler.accelerator2task_instance(task)
            if self.broker.finished==True:
                break
            yield self.env.timeout(1)



