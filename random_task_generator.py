import random
import csv
random.seed(8)

headers = ['id','submit_time','task_type']

f=open('simulations_test/tasks_test/task8', 'w')
f_csv = csv.writer(f)
f_csv.writerow(headers)
b=0
for i in range(0,1000):
    a=random.randint(0,3)
    b=random.randint(b,i*10)
    if(a==0):
        f_csv.writerow([i,b,'resnet50'])
    elif(a==1):
        f_csv.writerow([i, b, 'vgg16'])
    elif(a==2):
        f_csv.writerow([i, b, 'vgg19'])
    else:
        f_csv.writerow([i, b, 'inception_v1'])
