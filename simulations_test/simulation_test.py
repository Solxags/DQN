from  broker_test import broker
from task_test import task_list_generator
from machine_test import machine_list_generator
import os
task_path= '/home/ssego/DQN/simulations_test/tasks'

class simulation(object):
    def __init__(self,env,schduler):
        self.env=env
        self.broker=broker(env,schduler)
        self.schduler=schduler

    def init_simulation(self):
        Task_list=task_list_generator(task_path,self.env)
        self.broker.commit_task_list(Task_list)
        Machine_list=machine_list_generator(self.env)
        self.broker.register_machine_list(Machine_list)

    def run(self):
        while True:
            while self.broker.free_machine_list!=[]:
                machine=self.broker.free_machine_list.pop()
                self.schduler.machine2task(self.broker,machine)
            for task in self.broker.running_task_list:
                if task.finished == True:
                    self.broker.total_finish_time+=self.env.now
                    print("Task "+str(task.id)+" Finished on "+str(self.env.now))
                    task.task_start_flag == False
                    task.task_finish_flag == True
                    self.broker.remove_finished_task(task)
                else:
                    if task.is_waiting==True:
                        for machine in task.machine_list:
                            for accelerator in machine.accelerator_list:
                                if accelerator.running_task_instance==None:
                                    self.schduler.accelerator2task_instance(task)
            if self.broker.finished==True:
                print(self.broker.total_finish_time/8)
                break
            yield self.env.timeout(1)



