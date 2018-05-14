from db import modles
from conf import settings
import os
def login(name,password,type):
    if type=='admin':
        obj=modles.Admin.get_obj_by_name(name)
        if obj:
            if obj.password==password:
                return True,'login successfully'
            else:
                return False,'password differ'
        else:return False,'username does not exist'
    elif type=='teacher':
        obj = modles.Teacher.get_obj_by_name(name)
        if obj:
            if obj.password == password:
                return True, 'login successfully'
            else:
                return False, 'password differ'
        else:
            return False, 'username does not exist'
    elif type=='student':
        obj = modles.Student.get_obj_by_name(name)
        if obj:
            if obj.password == password:
                return True,'login successfully'
            else:
                return False,'password differ'
        else:
            return False,'username does not exist'

def check_info(type):
    path=os.path.join(settings.DB_PATH,type)
    if os.path.isdir(path):
        return os.listdir(path)
    else:
        return False