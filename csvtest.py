import csv
import random

path="simulations_test/machine_config/machine_config_"
random.seed(21)

for i in range(0,16):
    csvfile=open(path+str(i)+".csv", "w")
    spam_writer = csv.writer(csvfile)
    headers = ['id','accelerator']
    spam_writer.writerow(headers)
    for j in range(0,2):
        a = random.randint(0, 3)
        if(a==0):
            spam_writer.writerow([j,'CPU'])
        elif(a==1):
            spam_writer.writerow([j, 'GPU'])
        elif(a==2):
            spam_writer.writerow([j, 'FPGA'])
        else:
            spam_writer.writerow([j, 'MLU'])

