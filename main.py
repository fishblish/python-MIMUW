import os
import random
import csv

week=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
line1='Model; Output value; Time of computation;'
listABC=['A','B','C']
path='C:/Users/User/Desktop/uni/magisterka/python/lab6-homework'

if not os.path.exists(path+'/monday'):
    for i in week:
        os.makedirs(path+'/'+i)
        os.makedirs(path+'/'+i+'/morning')
        os.makedirs(path+'/'+i+'/evening')
        line21=random.choice(listABC)
        line22=str(random.choice(range(0,1000)))
        line23 = str(random.choice(range(0, 1000)))+'s'
        f=open(path+'/'+i+'/morning/Solutions.csv','w')
        f.write(line1+'\n'+line21+';'+line22+';'+line23)
        f.close()
        line21 = random.choice(listABC)
        line22 = str(random.choice(range(0, 1000)))
        line23 = str(random.choice(range(0, 1000))) + 's'
        f = open(path+'/' + i + '/evening/Solutions.csv', 'w')
        f.write(line1 + '\n' + line21 + ';' + line22 + ';' + line23)
        f.close()


suma=0
for folder in os.listdir(path):
    for podfolder in os.listdir(path+'/'+folder):
        with open(path+'/'+folder+'/'+podfolder+'/Solutions.csv') as f:
            reader = csv.reader(f, delimiter=';')
            data = list(reader)
            print(data)

            if data[1][0]=='A':
                suma=suma+int(data[1][2][0:len(data[1][2])-1])
                print(suma)

