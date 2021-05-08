class broker(object):
    def __init__(self,env,schduler):
        self.task_list=None
        self.machine_list=None
        self.running_task_list=[]
        self.waiting_task_list=[]
        self.free_machine_list=[]
        self.env=env
        self.scheduler=schduler

    def commit_task_list(self,task_list):
        self.task_list=task_list
        self.waiting_task_list=task_list

    def register_machine_list(self,machine_list):
        self.machine_list=machine_list
        self.free_machine_list=machine_list

    @property
    def finished(self):
        if len(self.waiting_task_list) != 0:
            return False
        if len(self.running_task_list) != 0:
            return False
        return True
