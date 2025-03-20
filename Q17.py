class Course:
    def __init__(self,course):
        self.course=course

    def get_details(self):
        print(f"the course is called : {Course}")

class WebDevClass(Course):
    def __init__(self,course):
        super().__init__(course)
        
    def get_details(self):
        print(f"the course '{self.course}' is not included in web dev")

user1= WebDevClass("biology")

user1.get_details()