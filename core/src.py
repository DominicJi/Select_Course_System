from core import admin,teacher,student
func_dic={'1':admin.run,'2':teacher.run,'3':student.run}
def run():
    while True:
        print('''
            1.管理员视图
            2.教师视图
            3.学生视图
        ''')
        dec=input('please choice one >>:').strip()
        if dec not in func_dic:continue
        func_dic[dec]()