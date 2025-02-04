from task_test import task,task_instance
from machine_test import machine

class schduler(object):
    def __init__(self,algorithm,policy):
        self.algorithm=algorithm
        self.policy=policy

    def machine2task(self,broker,machine):
        self.policy.run(broker,machine)

    def accelerator2task_instance(self,task):
        if task.is_waiting==True:
            randy_task_instance_list=task.waiting_task_instance_list
            randy_accelerator_list=[]
            for machine in task.machine_list:
                randy_accelerator_list+=machine.accelerator_list
            randy_task_instance,randy_accelerator=self.algorithm.run(randy_task_instance_list,randy_accelerator_list)
            task.waiting_task_instance_list.remove(randy_task_instance)
            task.running_task_instance_list.append(randy_task_instance)
            randy_accelerator.run_task_instance(randy_task_instance)
