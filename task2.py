class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, studying {self.course}.")

# Creating student objects
student1 = Student("Ariel C. Lacambra", 25, "Diploma Information Technology II")
student2 = Student("Nikka Senado", 22, "Diploma Information Technology II")
student3 = Student("Jhen Senado", 27, "Diploma Information Technology II")

# Calling introduce method
student1.introduce()
student2.introduce()
student3.introduce()
