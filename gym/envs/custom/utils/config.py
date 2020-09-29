from enum import Enum


class TaskInstanceConfig(object):
    def __init__(self, task_config):
        self.cpu = task_config.cpu
        self.gpu = task_config.gpu
        self.fpga = task_config.fpga
        self.mlu = task_config.mlu
        self.memory = task_config.memory
        self.disk = task_config.disk
        self.duration = task_config.duration
        self.type = type


class TaskType(Enum):
    fit_gpu = 1
    fit_fpga = 2
    fit_mlu = 3


class TaskConfig(object):
    def __init__(self, task_index, instances_number, cpu, gpu, fpga, mlu, memory, disk, duration, type,
                 parent_indices=None):
        self.task_index = task_index
        self.instances_number = instances_number
        self.cpu = cpu
        self.gpu = gpu
        self.fpga = fpga
        self.mlu = mlu
        self.memory = memory
        self.disk = disk
        self.duration = duration
        self.type = type
        self.parent_indices = parent_indices


class JobConfig(object):
    def __init__(self, idx, submit_time, task_configs):
        self.submit_time = submit_time
        self.task_configs = task_configs
        self.id = idx