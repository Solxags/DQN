import os
import simpy
import csv
from accelerator_test import accelerator_list_generator,GPU,FPGA,CPU,MLU,accelerator
machine_config_path= 'machine_config/'
def machine_list_generator(env):
    machine_list=[]
    list = os.listdir(machine_config_path)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(machine_config_path, list[i])
        if os.path.isfile(path):
            Machine = machine(i, path,env)
            machine_list.append(Machine)
    return machine_list

class machine(object):
    def __init__(self,id,machine_config_path,env):
        self.running_task = None
        self.free=None
        self.id=id
        self.env=env
        self.accelerator_list=self.machine_generator(machine_config_path,env)

    def machineLoadFromCSV(self,trace_path):
        trace=[]
        with open(trace_path, "r", encoding="utf-8") as csvfile:
            spam_reader = csv.DictReader(csvfile)
            spam_reader = list(spam_reader)
        for i in range(len(spam_reader)):
            trace.append(spam_reader[i])
        return trace

    def machine_generator(self,trace_path,env):
        acc_list=[]
        trace=self.machineLoadFromCSV(trace_path)
        for instance in trace:
            acc_list.append(instance['accelerator'])
        accelerator_list=accelerator_list_generator(acc_list,env)
        return accelerator_list

    def run_task(self,task):
        self.free=self.env.event()
        self.running_task=task
        task.machine_list.append(self)
        yield task.finish
        self.running_task=None
        self.free.succeed()
