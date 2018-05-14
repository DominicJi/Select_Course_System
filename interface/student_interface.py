from db import modles

def register(name,password):
    obj=modles.Student.get_obj_by_name(name)
    if obj:
        return False,'student name has exist'
    else:
        modles.Student(name,password)
        return True,'register successfully!'

def choose_school(name,type):
    obj=modles.Student.get_obj_by_name(type)
    if obj.school:
        return False,'你已经选择过校区：%s'%obj.school
    else:
        obj.choose_school(name)
        return True,'选择成功，学校为%s'%name

def get_school_and_courses(type):
    obj=modles.Student.get_obj_by_name(type)
    return obj.school,obj.courses
def get_school_courses(school_name):
    obj=modles.School.get_obj_by_name(school_name)
    return obj.courses

def choose_course(course_name,type):
    obj=modles.Student.get_obj_by_name(type)
    obj.add_course(course_name)
    obj_course=modles.Course.get_obj_by_name(course_name)
    obj_course.add_student_name(type)
def check_score(type):
    obj=modles.Student.get_obj_by_name(type)
    return obj.score