class policy(object):
    def run(self,broker,machine):
        if broker.running_task_list !=[]:
            task=broker.running_task_list[0]
            task.machine_list.append(machine)
        else:
            if broker.waiting_task_list != []:
                task = broker.waiting_task_list.pop()
                broker.running_task_list.append(task)
                task.task_start_flag = True
                task.machine_list.append(machine)