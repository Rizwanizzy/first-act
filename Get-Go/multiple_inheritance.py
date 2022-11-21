class Name:
    def __init__(self, name):
        self.name = name

    def getName(self):
        self.name = input("enter name:")


class Mark:
    def __init__(self, mark):
        self.mark = mark

    def getMark(self):
        self.mark = input("enter mark:")


class Student(Name, Mark):
    def printDetails(self):
        print("Student Name:", self.name, "\t", "Student Mark:", "\t", self.mark)


stud = Student("")
stud.getName()
stud.getMark()
stud.printDetails()
