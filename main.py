#code for a tution class
class Tution:
    name_institute = "ABC classes"
    area = "xyzcolony"

    def __init__(self, name, age, course, fee_status):
        self.name = name
        self.age = age
        self.course = course
        self.fee_status = fee_status


print("data of students in database......")

stu1 = Tution("ravi", 22, "java", "submitted")
print(stu1.name,stu1.age,stu1.course,stu1.fee_status)
print(Tution.area,Tution.name_institute)



