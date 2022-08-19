class Student:
    #static or class variable
    sch_name="SDVP"
    def __init__(self, sname,sroll): # contructor
        self.sname=sname #instance variable
        self.sroll=sroll
        print(self.sname,self.sroll,Student.sch_name)

    def display(self):
        print("clg name :" + Student.sch_name) #call class variable

s1=Student('RAHUL', 59) # create object
s1.display() #call method 