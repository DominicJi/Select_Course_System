from interface import teacher_interface,common_interface
from lib import common
user_data={'name':None}
def login():
    while True:
        name=input('please input your username>>:').strip()
        password=input('plesae input your password>>:').strip()
        flag,msg=common_interface.login(name,password,'teacher')
        if flag:
            user_data['name']=name
            print(msg)
            break
        else:print(msg)
@common.login_auth('teacher')
def check_courses():
    course_list=teacher_interface.check_courses(user_data['name'])
    if course_list:
        for i in course_list:
            print(i)
    else:print('暂无教授的课程')
@common.login_auth('teacher')
def choose_course():
    course_list=common_interface.check_info('course')
    if course_list:
        for i,name in enumerate(course_list):
            print(i+1,name)
        dec= input('please choice>>"').strip()
        if dec.isdigit():
            dec = int(dec)
            if dec in range(1, len(course_list) + 1):
                course_name = course_list[dec - 1]
                teacher_interface.choose_course(course_name,user_data['name'])
                print('选课成功')
                return
            else:print('not in range')
        else:print('must be int ')
    else:print('暂无任何课程')
@common.login_auth('teacher')
def check_student():
    course_list=teacher_interface.check_courses(user_data['name'])
    if course_list:
        while True:
            for i,name in enumerate(course_list):
                print(i,name)
            dec=input('please choice>>:').strip()
            if dec=='q':return
            if dec.isdigit():
                dec=int(dec)
                if dec in range(0,len(course_list)):
                    coures_name=course_list[dec]
                    student_list=teacher_interface.check_student(coures_name)
                    if student_list:
                        for name in student_list:
                            print(name)
                        return
                    else:print('not student')
                else:print('range error')
            else:print('must be int')
    else:print('暂无教授课程所以无法查看学生')
@common.login_auth('teacher')
def modify_score():
    course_list=teacher_interface.check_courses(user_data['name'])
    if course_list:
        while True:
            for i,course in enumerate(course_list):
                print(i+1,course)
            dec=input('你想修改哪门课程下的学生成绩>>:').strip()
            if dec=='q':return
            if dec.isdigit():
                dec = int(dec)
                if dec in range(1, len(course_list) + 1):
                    course_name = course_list[dec - 1]
                    student_list=teacher_interface.check_student(course_name)
                    if student_list:
                        for i,name in enumerate(student_list):
                            print(i+1,name)
                        dec=input('please choose student').strip()
                        if dec.isdigit():
                            dec = int(dec)
                            if dec in range(1, len(student_list) + 1):
                                student_name = student_list[dec - 1]
                                score=input('你想将学生这门课的成绩改成多少？').strip()
                                if score.isdigit():
                                    score=int(score)
                                    teacher_interface.modify(student_name,course_name,score,user_data['name'])
                                    print('修改成功')
                                    return
                                else:print('分数必须是数字')
                            else:print('not in normal range')
                        else:print('choose must be int')
                    else:print('课程下暂无学生')
                else:print('not in normal range')
            else:print('choose must be int')
    else:print('你暂时还没有教授的课程')

func_dic={'1':login,'2':check_courses,'3':choose_course,'4':check_student,'5':modify_score}
def run():
    while True:
        print('''
            1、登录
            2、查看教授课程
            3、选择教授课程
            4、查看课程下学生
            5、修改学生成绩   
        ''')
        choice = input('please choice>>:').strip()
        if choice not in func_dic: continue
        func_dic[choice]()