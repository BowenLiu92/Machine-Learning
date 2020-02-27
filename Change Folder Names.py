#We can make this a function
import os
def renameFn(basedir, rstr):
#basedir is the directory where the target folders are located
#rstr is the string that needs to be replaced
    for fn in os.listdir(basedir):
        if rstr in fn:
            newfn = fn.replace(rstr, '').lstrip()
            os.rename(os.path.join(basedir, fn),
                     os.path.join(basedir, newfn))