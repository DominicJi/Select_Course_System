from interface import student_interface,common_interface
from lib import common
user_data={'name':None}
def register():
    while True:
        name=input('please input your name>>"').strip()
        password=input('please input your password>>"').strip()
        pwd=input('please confirm passowrd>>:').strip()
        if password==pwd:
            flag,msg=student_interface.register(name,password)
            if flag:
                print(msg)
                break
            else:print(msg)
        else:print('password confirm failure')
def login():
    while True:
        name=input('please input your name>>"').strip()
        password=input('please input your password>>:').strip()
        flag,msg=common_interface.login(name,password,'student')
        if flag:
            user_data['name']=name
            print(msg)
            break
        else:print(msg)

@common.login_auth('student')
def choose_school():
    school_list=common_interface.check_info('school')
    if school_list:
        while True:
            for i,name in enumerate(school_list):
                print(i+1,name)
            dec=input('你想在哪一个学校里开设课程》》：').strip()
            if dec.isdigit():
                dec=int(dec)
                if dec in range(1,len(school_list)+1):
                    school_name=school_list[dec-1]
                    flag,msg=student_interface.choose_school(school_name,user_data['name'])
                    if flag:
                        print(msg)
                        return
                    else:print(msg)
                else:print('not in range')
            else:print('must be int!')
    else:print('暂时没有学校')
@common.login_auth('student')
def choose_course():
    school_name,course_list=student_interface.get_school_and_courses(user_data['name'])
    if school_name:
        courses=student_interface.get_school_courses(school_name)
        if courses:
            while True:
                for i,name in enumerate(courses):
                    print(i+1,name)
                dec=input('please choice>>"').strip()
                if dec.isdigit():
                    dec=int(dec)
                    if dec in range(1,len(courses)+1):
                        name=courses[dec-1]
                        if name not in course_list:
                            student_interface.choose_course(name,user_data['name'])
                            print('选课成功')
                            return
                        else:print('课程已经存在你的学习课程中')
                    else:print('not in normal range')
                else:print('choice must be int')
        else:print('学校暂时没有任何课程')
    else:print('你暂时还没有选择学校，请先选择学校')
@common.login_auth('student')
def check_score():
    score_list=student_interface.check_score(user_data['name'])
    if score_list:
        print(score_list.items())
    else:print('暂无课程')
func_dic={'1':register,'2':login,'3':choose_school,'4':choose_course,'5':check_score}
def run():
    while True:
        print('''
            1.学生注册
            2.学员登陆
            3.选择学校
            4.选择课程(选择课程默认创建为0)
            5.查看课程成绩     
        ''')
        dec=input('please chocie>>:').strip()
        if dec not in func_dic:continue
        func_dic[dec]()