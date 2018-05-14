from db import modles

def check_courses(type):
    obj=modles.Teacher.get_obj_by_name(type)
    return obj.teach_courses

def choose_course(course_name,type):
    obj=modles.Teacher.get_obj_by_name(type)
    obj.add_teach_courses(course_name)

def check_student(course_name):
    obj=modles.Course.get_obj_by_name(course_name)
    return obj.student_name

def modify(student_name,course_name,score,type):
    obj=modles.Teacher.get_obj_by_name(type)
    student=modles.Student.get_obj_by_name(student_name)
    obj.modify_score(student,course_name,score)