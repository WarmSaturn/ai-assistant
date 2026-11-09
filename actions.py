import os

import config


def normalized(name):
        return " ".join(name.lower().split())

def open_target(name):
    name = normalized(name)
    # نام ماژول.نام (دیکشنری).تابع(آرگومان)    
    path = config.ALIASES.get(name)
    
    if path is None: # اسمی که کاربر گفته در ALIASES نیست
        
        return (False,"Try again")
     
    elif not os.path.exists(path): # فایل روی دیسک نیست
    
        return (False,"The path doesn't exist.")
    
    try:
    
        os.startfile(path)
    
    except OSError:
    
        return (False,"couldn't be opened.")
    
    return (True,path)

ok,message = open_target("AI Assistant File")   

if ok:
    print(f"Success: {message}")
else:
    print(f"Error: {message}")
    