class student():
    def __init__(self,name,age,course):
        self.name= name
        self.age=age
        self.course=course

    def display_info(self):
        print(f"student name: {self.name}")
        print(f"student Age: {self.age}")
        print(f"student course: {self.course}")


user1= student('chala',20,'python')

user1.display_info()