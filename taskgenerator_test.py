import csv
from simulations.config import TaskConfig
import os
import simpy

trace_path='/home/ssego/DQN/simulations/tasks/trace/resnet50_vgg16_vgg19_inception_v1_1000.csv'
number=1000

def taskLoadFromCSV(trace_path):
    trace=[]
    with open(trace_path, "r", encoding="utf-8") as csvfile:
        spam_reader = csv.DictReader(csvfile)
        spam_reader = list(spam_reader)
    for i in range(len(spam_reader)):
        trace.append(spam_reader[i])
    return trace

def taskGenerator(env, number, trace):
    for i in range(number):
        submit_time=int(trace[i]['submit_time'])
        if(env.now!=submit_time):
            yield env.timeout(submit_time-env.now)
        env.process(taskTest(env, trace[i]))

def taskTest(env,task_info):
    print(task_info['submit_time'],task_info['task_type'])
    yield env.timeout(1)


def main():
    trace=taskLoadFromCSV(trace_path)
    env = simpy.Environment()
    env.process(taskGenerator(env,number,trace))
    env.run()

if __name__ == "__main__":
    main()