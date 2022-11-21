class studname:
    def __init__(self, name):
        self.name = name

    def getName(self):
        self.name = input('enter your name:')


class studmark(studname):
    def __init__(self, mark):
        self.mark = mark

    def getMark(self):
        self.mark = input("enter your mark:")


class studage(studmark):
    def __init__(self, age):
        self.age = age

    def getAge(self):
        self.age = input("enter your age:")


class display(studage):
    def printDetails(self):
        print("student name:", self.name, '\t', "student mark:", self.mark, "student age:", "\t", self.age)


stud = display("")
stud.getName()
stud.getMark()
stud.getAge()
stud.printDetails()
