import csv
import simpy

gpu_config_path= '/home/ssego/DQN/simulations_test/processos_config/gpu.csv'
gpu_power_consumption=24

mlu_config_path= '/home/ssego/DQN/simulations_test/processos_config/mlu.csv'
mlu_power_consumption=24

cpu_config_path= '/home/ssego/DQN/simulations_test/processos_config/cpu.csv'
cpu_power_consumption=24

fpga_config_path= '/home/ssego/DQN/simulations_test/processos_config/fpga.csv'
fpga_power_consumption=24

def accelerator_list_generator(accelerators_list,env):
    accelerator_list=[]
    id=0
    for accelerator in accelerators_list:
        if accelerator=='CPU':
            processor=CPU(id,cpu_config_path,env,cpu_power_consumption)
            accelerator_list.append(processor)
        elif accelerator=='GPU':
            processor = GPU(id, gpu_config_path, env, gpu_power_consumption)
            accelerator_list.append(processor)
        elif accelerator=='FPGA':
            processor = FPGA(id, fpga_config_path, env, fpga_power_consumption)
            accelerator_list.append(processor)
        elif accelerator=='MLU':
            processor = MLU(id, mlu_config_path, env, mlu_power_consumption)
            accelerator_list.append(processor)
        else:
            continue
        id+=1
    return accelerator_list

    # @property
    # def state(self):
    #     return{
    #         'machine':self.machine,
    #         'processor_list':self.Accelerator_list
    #     }
    #
    # def unoccupied_processor_search(self):
    #     unoccupied_processor_list=[]
    #     for processor in self.Accelerator_list:
    #         if processor.running_task_instance==None:
    #             unoccupied_processor_list.append(processor)
    #     return unoccupied_processor_list

# class Task_instance(object):
#     def __init__(self,type):
#         self.type=type
#         self.started=False
#         self.started_timestamp=None
#         self.finished=False
#         self.finished_timestamp=None

class accelerator(object):
    def __init__(self, env, id, power_consumption):
        self.id=id
        self.power_consumption_total=0
        self.power_consumption = power_consumption
        self.runtime = None
        self.env = env
        self.machine = None
        self.running_task_instance = None
        self.free = env.event()

    def accommodate(self):
        return self.running_task_instance is None

    @property
    def name(self):
        assert NotImplementedError

    @property
    def state(self):
        assert NotImplementedError

    def caculate_runtime(self, task_instance):
        return self.runtime_list[task_instance.type]

    def caculate_power_compution(self, runtime):
        return runtime * self.power_consumption

    def do_work(self, runtime):
        self.running_task_instance.started = True
        self.running_task_instance.started_timestamp = self.env.now
        yield self.env.timeout(runtime)
        self.running_task_instance.task.running_task_instance_list.remove(self.running_task_instance)
        self.running_task_instance.finished = True
        self.running_task_instance.finished_timestamp = self.env.now
        self.power_consumption_total+=self.caculate_power_compution(runtime)
        print(self.state, self.env.now)
        self.running_task_instance=None
        self.free.succeed()
        self.free = self.env.event()


class FPGA(accelerator):
    name = "FPGA"

    def __init__(self, id,fpga_config_path, env,power_consumption):
        super().__init__(env,id,power_consumption)
        self.runtime_list={}
        with open(fpga_config_path, "r", encoding="utf-8") as csvfile:
            spam_reader = csv.DictReader(csvfile)
            for item in spam_reader:
                self.runtime_list[item["task"]] = (int)(item["execute_time"])

    def run_task_instance(self, task_instance):
        self.running_task_instance = task_instance
        runtime=self.caculate_runtime(task_instance)
        self.env.process(self.do_work(runtime))

    @property
    def state(self):
        return {
            'id': FPGA.name + "-" + str(self.id),
            'clock':self.env.now,
            'power_consumption_total': self.power_consumption_total,
            'running_task_instance': self.running_task_instance.type,
            'running_task_instance_ID':self.running_task_instance.id
        }

    def __eq__(self, other):
        return isinstance(other, FPGA) and other.id == self.id

class GPU(accelerator):
    name = "GPU"

    def __init__(self, id,gpu_config_path, env,power_consumption):
        super().__init__(env,id,power_consumption)
        self.runtime_list={}
        with open(gpu_config_path, "r", encoding="utf-8") as csvfile:
            spam_reader = csv.DictReader(csvfile)
            for item in spam_reader:
                self.runtime_list[item["task"]] = (int)(item["execute_time"])

    def run_task_instance(self, task_instance):
        self.running_task_instance = task_instance
        runtime=self.caculate_runtime(task_instance)
        self.env.process(self.do_work(runtime))

    @property
    def state(self):
        return {
            'id': GPU.name + "-" + str(self.id),
            'clock':self.env.now,
            'power_consumption_total': self.power_consumption_total,
            'running_task_instance': self.running_task_instance.type,
            'running_task_instance_ID': self.running_task_instance.id
        }

    def __eq__(self, other):
        return isinstance(other, GPU) and other.id == self.id

class MLU(accelerator):
    name = "MLU"

    def __init__(self, id,mlu_config_path, env,power_consumption):
        super().__init__(env,id,power_consumption)
        self.runtime_list={}
        with open(mlu_config_path, "r", encoding="utf-8") as csvfile:
            spam_reader = csv.DictReader(csvfile)
            for item in spam_reader:
                self.runtime_list[item["task"]] = (int)(item["execute_time"])

    def run_task_instance(self, task_instance):
        self.running_task_instance = task_instance
        runtime=self.caculate_runtime(task_instance)
        self.env.process(self.do_work(runtime))

    @property
    def state(self):
        return {
            'id': MLU.name + "-" + str(self.id),
            'clock':self.env.now,
            'power_consumption_total': self.power_consumption_total,
            'running_task_instance': self.running_task_instance.type,
            'running_task_instance_ID': self.running_task_instance.id
        }

    def __eq__(self, other):
        return isinstance(other, MLU) and other.id == self.id

class CPU(accelerator):
    name = "CPU"

    def __init__(self, id,cpu_config_path, env,power_consumption):
        super().__init__(env,id,power_consumption)
        self.runtime_list={}
        with open(cpu_config_path, "r", encoding="utf-8") as csvfile:
            spam_reader = csv.DictReader(csvfile)
            for item in spam_reader:
                self.runtime_list[item["task"]] = (int)(item["execute_time"])

    def run_task_instance(self, task_instance):
        self.running_task_instance = task_instance
        runtime=self.caculate_runtime(task_instance)
        self.env.process(self.do_work(runtime))

    @property
    def state(self):
        return {
            'id': CPU.name + "-" + str(self.id),
            'clock':self.env.now,
            'power_consumption_total': self.power_consumption_total,
            'running_task_instance': self.running_task_instance.type,
            'running_task_instance_ID': self.running_task_instance.id
        }

    def __eq__(self, other):
        return isinstance(other, CPU) and other.id == self.id

# def main():
#     env=simpy.Environment()
#     mlu=MLU(0,mlu_config_path,env,mlu_power_consumption)
#     task_instance=Task_instance('vgg16')
#     env.process(mlu.run_task_instance(task_instance))
#     env.run()
#
# if __name__ == "__main__":
#     main()