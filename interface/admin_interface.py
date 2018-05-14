from db import modles

def register(name,password):
    obj=modles.Admin.get_obj_by_name(name)
    if obj:
        return False,'该管理员已存在'
    else:
        modles.Admin(name,password)
        return True,'register successfully!'
def create_school(name,address,type):
    obj=modles.School.get_obj_by_name(name)
    if obj:
        return False,'该校区已存在'
    else:
        admin=modles.Admin.get_obj_by_name(type)
        admin.create_school(name,address)
        return True,'校区%s创建成功'%name
def create_course(name,school_name,type):
    school=modles.School.get_obj_by_name(school_name)
    if name not in school.courses:
        admin=modles.Admin.get_obj_by_name(type)
        admin.create_course(name)
        school.add_course(name)
        return True,'课程%s开设与学校%s'%(name,school_name)
    else:return False,'该学校已有该课程名'

def create_teacher(name,password,type):
    obj=modles.Teacher.get_obj_by_name(name)
    if obj:
        return False,'老师名已存在'
    else:
        admin=modles.Admin.get_obj_by_name(type)
        admin.create_teacher(name,password)
        return True,'老师%s添加成功'%name



