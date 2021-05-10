import os
import csv

def task_list_generator(task_path,env):
    task_list=[]
    list = os.listdir(task_path)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(task_path, list[i])
        if os.path.isfile(path):
            Task=task(i,path,env)
            task_list.append(Task)
    return task_list

class task(object):
    def __init__(self,id,path,env):
        self.id=id
        self.machine_list=[]
        self.waiting_task_instance_list=self.task_generator(path)
        self.running_task_instance_list=[]
        self.start_time=None
        self.finish_time=None
        self.task_start_flag=False
        self.task_finish_flag=False
        self.task_finish=env.event()

    def taskLoadFromCSV(self,trace_path):
        trace=[]
        with open(trace_path, "r", encoding="utf-8") as csvfile:
            spam_reader = csv.DictReader(csvfile)
            spam_reader = list(spam_reader)
        for i in range(len(spam_reader)):
            trace.append(spam_reader[i])
        return trace

    def task_generator(self,trace_path):
        Task_instance_list=[]
        trace=self.taskLoadFromCSV(trace_path)
        for instance in trace:
            Task_instance=task_instance(instance,self)
            Task_instance_list.append(Task_instance)
        return Task_instance_list

    @property
    def finished(self):
        """
        A task is finished only if it has no waiting task instances and no running task instances.
        :return: bool
        """
        if len(self.waiting_task_instance_list) != 0:
            return False
        if len(self.running_task_instance_list) != 0:
            return False
        return True

    @property
    def is_waiting(self):
        """
        A task is waiting if it has waiting task instances.
        :return: bool
        """
        if len(self.waiting_task_instance_list) != 0:
            return True
        return False

class task_instance(object):
    def __init__(self,trace,task):
        self.task=task
        self.id=int(trace['id'])
        self.start_flag=False
        self.finish_flag=False
        self.type=trace['task_type']
        self.submit_time=int(trace['submit_time'])
