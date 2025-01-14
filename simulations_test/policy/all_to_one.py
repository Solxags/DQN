class policy(object):
    def run(self,broker,machine):
        if broker.running_task_list !=[]:
            task=broker.running_task_list[0]
            machine.env.process(machine.run_task(task))
        else:
            if broker.waiting_task_list != []:
                task = broker.waiting_task_list.pop()
                broker.running_task_list.append(task)
                task.task_start_flag = True
                machine.env.process(machine.run_task(task))