class algorithm(object):
    def run(self,randy_task_instance_list,randy_accelerator_list):
        for accelerator in randy_accelerator_list:
            for task in randy_task_instance_list:
                if accelerator.accommodate():
                    candidate_accelerator = accelerator
                    candidate_task = task
                    break
            else:
                continue
            break
        return  candidate_task,candidate_accelerator