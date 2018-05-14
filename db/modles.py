from db import db_handler


class Base:
    def save(self):
        db_handler.save(self)
    @classmethod
    def get_obj_by_name(cls,name):
        return db_handler.select(name,cls.__name__.lower())
class Admin(Base):
    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.save()
    def create_school(self,name,address):
        school=School(name,address)
        school.save()
    def create_course(self,name):
        course=Course(name)
        course.save()
    def create_teacher(self,name,password):
        teacher=Teacher(name,password)
        teacher.save()
class Teacher(Base):
    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.teach_courses=[]
    def add_teach_courses(self,name):
        self.teach_courses.append(name)
        self.save()
    def modify_score(self,student,course_name,score):
        student.courses[course_name]=score
        student.save()

class Course(Base):
    def __init__(self,name):
        self.name=name
        self.student_name=[]
    def add_student_name(self,name):
        self.student_name.append(name)
        self.save()

class School(Base):
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.courses=[]
    def add_course(self,course_name):
        self.courses.append(course_name)
        self.save()
class Student(Base):
    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.courses=[]
        self.school=None
        self.score={}
        self.save()
    def add_course(self,course_name):
        self.courses.append(course_name)
        self.score[course_name]=0
        self.save()
    def choose_school(self,name):
        self.school=name
        self.save()

