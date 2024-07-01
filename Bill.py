import datetime

now = datetime.datetime.now()

class bill:

    def __init__(self):
        self.i=1

    def new_bill(self,name,num):
        date = now.strftime("%Y-%m-%d")
        time= now.strftime(" %H:%M:%S")
        newbill1=open(f"../bills/{name}{self.i}.txt" ,"w")
        newbill1.write(f"האיחור של: {name}\n")
        newbill1.write(f"      שעה: {time} \n")
        newbill1.write(f"   תאריך : {date}  \n ")
        newbill1.write(f" מספר איחור :{num}\n")
        self.i=self.i+1
