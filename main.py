import csv
import time
res=[]
a = 0
max = 0
ta = time.time()
with open('Slime.csv','r') as f:
    read = csv.reader(f)
    for line in read:
        a+=1
        try:
            if int(line[2]) >= 35:
                print(line)
                # max=int(line[2])
                li = line
        except ValueError:
            print(line)
            break

        # if a>=100:
        #     break
        # res.append(line)
tb = time.time()
# print(li,max)
print(tb-ta)
