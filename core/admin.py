from interface import admin_interface,common_interface
from lib import common
user_data={'name':None}

def register():
    if user_data['name']:
        print('你已注册，并处于登陆状态')
        return
    while True:
        name=input('please input your name>>:').strip()
        password=input('please input your password>>:').strip()
        pwd=input('please confirm password>>:').strip()
        if password==pwd:
            flag,msg=admin_interface.register(name,password)
            if flag:
                print(msg)
                break
            else:print(msg)
        else:print('confirm password failure!')

def login():
    if user_data['name']:
        print('你已注册，并处于登陆状态')
        return
    while True:
        name=input('please input youe username>>:').strip()
        password=input('please input your password>>:').strip()
        flag,msg=common_interface.login(name,password,'admin')
        if flag:
            user_data['name']=name
            print(msg)
            break
        else:print(msg)
@common.login_auth('admin')
def create_school():
    while True:
        name=input('please input school name>>:').strip()
        address=input('please input school address>>:').strip()
        flag,msg=admin_interface.create_school(name,address,user_data['name'])
        if flag:
            print(msg)
            break
        else:print(msg)
@common.login_auth('admin')
def create_teacher():
    while True:
        name=input('please input teacher name>:').strip()
        password=input('please input password>>:').strip()
        pwd=input('please confirm password>>:').strip()
        if password==pwd:
            flag,msg=admin_interface.create_teacher(name,password,user_data['name'])
            if flag:
                print(msg)
                break
            else:print(msg)
        else:print('password confirm faliure')
@common.login_auth('admin')
def create_course():
    school_list=common_interface.check_info('school')
    if school_list:
        while True:
            for i,school in enumerate(school_list):
                print(i+1,school)
            dec=input('please choice>>:').strip()
            if dec.isdigit():
                dec=int(dec)
                if dec in range(1,len(school_list)+1):
                    school_name=school_list[dec-1]
                    course_name=input('what course are you want to open>>:').strip()
                    flag,msg=admin_interface.create_course(course_name,school_name,user_data['name'])
                    if flag:
                        print(msg)
                        return
                    else:print(msg)
                else:print('choice not in normal range')
            else:print('dec not numbers')
    else:print('暂时还没有一所学校')




fun_dic={'1':register,'2':login,'3':create_school,'4':create_teacher,'5':create_course}
def run():
    while True:
        print('''
            1.管理员注册
            2.管理员登陆
            3.创建校区
            4.新增老师
            5.创建课程  
        ''')
        choice=input('please choice>>:').strip()
        if choice not in fun_dic:continue
        fun_dic[choice]()