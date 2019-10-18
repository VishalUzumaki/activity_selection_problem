import sys

print("For input file",sys.argv[1])

class Activity:

    def __init__(self,a,b,c):
        self.start=a
        self.finish=b
        self.value=c

# start=[]
# finish=[]
# values=[]


items=[]

with open(sys.argv[1],"r") as fp:
    for line in fp.read().split("\n"):
        counter=0
        for numbers in line.split(" "):
            if counter==0:
                a=int(numbers)
            if counter==1:
                b=int(numbers)
            if counter==2:
                c=int(numbers)
            counter+=1
        ob=Activity(a, b, c)
        items.append(ob)

# print("start",start)
# print("finish",finish)
# print("values",values)

items.sort(key=lambda ob:ob.finish)

profit=[]

for i in items:
    profit.append(int(i.value))


for i in range(1,len(profit)):
    final_result=[]
    for j in range(0,i):
        if int(items[j].finish)<=int(items[i].start):
            final_result.append(profit[j]+profit[i])

    if final_result:
        profit[i]=max(final_result)

print(max(profit))

