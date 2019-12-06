class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_marks(self):
        return self.marks
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def set_marks(self,marks):
        self.marks=marks
a=Student('divyanshu',18,70)
b=Student('priyanshu',19,80)
c=Student('tushar',26,90)
print(a.name+ " "+b.name+" "+c.name)