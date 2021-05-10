import numpy as np
import simpy


class broker(object):
    def __init__(self,schduler):
        self.task_list=[]
        self.machine_list=[]
        self.running_task_list=[]
        self.waiting_task_list=None
        self.free_machine_list=None
        self.env=None
        self.scheduler=schduler
        self.total_finish_time=0

    def commit_task_list(self,task_list):
        for task in task_list:
            self.task_list.append(task)
        self.waiting_task_list=task_list

    def register_machine_list(self,machine_list):
        for machine in machine_list:
            self.machine_list.append(machine)
        self.free_machine_list=machine_list

    def remove_finished_task(self,task):
        self.running_task_list.remove(task)
        for machine in task.machine_list:
            self.free_machine_list.append(machine)

    @property
    def finished(self):
        if len(self.waiting_task_list) != 0:
            return False
        if len(self.running_task_list) != 0:
            return False
        return True

    @property
    def generate_task_machine_graph(self):
        machine_task_graph=np.zeros([len(self.task_list),len(self.machine_list)+1])
        for task in self.running_task_list:
            for machine in task.machine_list:
                machine_task_graph[task.id,machine.id]=1
            machine_task_graph[task.id, -1]=len(task.waiting_task_instance_list)/1000
        for task in self.waiting_task_list:
            machine_task_graph[task.id, -1] = 1
        return machine_task_graph

    def reset(self):
        self.env=simpy.Environment
        self.waiting_task_list = []
        self.free_machine_list = []
        for task in self.task_list:
            self.waiting_task_list.append(task)
        for machine in self.machine_list:
            self.free_machine_list.append(machine)
        self.total_finish_time = 0

    def search_task_id(self,id):
        for task in self.running_task_list:
            if task.id==id:
                return task
        for task in self.waiting_task_list:
            if task.id==id:
                self.running_task_list.append(task)
                self.waiting_task_list.remove(task)
                return task
        return None
