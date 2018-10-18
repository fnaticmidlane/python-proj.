class Person:

    def __init__ (self, fn, ln):
        self.fn = fn
        self.ln = ln

    def __str__ (self):
        return "{} {}". format(self.fn, self,ln)

    def eat(self, food):
        print("{} will eat {}".format(self, food))


class Student(Person):
    def __init__(self, fn, ln, school = ""):
        super().__init__(fn, ln)
        self.school= school

    def __str__ (self):
        return "{} [{}]".format(super().__str__(),self.school)

    def enroll (self):
        print("{} will enroll at {}". format(self, school))

if __name__ == "__main__":
    Zed = Person("Zed", "Shadow Master")
    print(Zed)
    Zed.eat("Xayah")

    Rakan= Student ("Rakan", "Thought", "VASTAYA")
    print(Rakan)
    Rakan.enroll()





