class student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark

    def getInput(self):
        self.name = input('enter your name:')
        self.age = input('enter your age:')
        self.mark = input('enter your mark:')
        student.printOutput(self)

    def printOutput(self):
        print("name:", self.name, "\t", "age:", self.age, "\t", "mark:", self.mark)


stud1 = student('', '', '')
stud1.getInput()
#stud1.printOutput()
