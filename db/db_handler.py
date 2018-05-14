import os,pickle
from conf import settings

def save(obj):
    path=os.path.join(settings.DB_PATH,obj.__class__.__name__.lower())
    if not os.path.isdir(path):
        os.mkdir(path)
    file_name=os.path.join(path,obj.name)
    with open(file_name,'wb')as f :
        pickle.dump(obj,f)
        f.flush()

def select(name,type):
    path=os.path.join(settings.DB_PATH,type)
    if not os.path.isdir(path):
        os.mkdir(path)
    file_name=os.path.join(path,name)
    if os.path.isfile(file_name):
        with open(file_name,'rb')as f:
            return pickle.load(f)
    else:return False