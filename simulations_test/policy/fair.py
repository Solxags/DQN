class policy(object):
    def run(self,broker):
        while True:
            if broker.waiting_task_list !=[]:
                task=broker.waiting_task_list.pop()
                broker.running_task_list.append(task)
                task.task_start_flag=True
                for i in range(0,2):
                    machine=broker.free_machine_list.pop()
                    task.machine_list.append(machine)
            else:
                break

