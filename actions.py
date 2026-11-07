import os

import config


def open_target(name):
    # نام ماژول.نام (دیکشنری).تابع(آرگومان)    
    path = config.ALIASES.get(name)

    if path is None: # اسمی که کاربر گفته در ALIASES نیست
        
        return "Try again"
     
    elif not os.path.exists(path): # فایل روی دیسک نیست
    
        return "The path doesn't exists."
    
    return path

obj = open_target(" ".join("ai assistent file".lower().split()))    
    