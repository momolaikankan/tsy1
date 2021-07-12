import os, sys
from subprocess import Popen
import subprocess
def get_root_dir(is_relative_to_execute=False):
    if getattr(sys, 'frozen', False):
        if is_relative_to_execute:
            return os.path.dirname(sys.executable)
        else:
            return sys._MEIPASS
    else:
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_file_path(path, is_relative_to_execute=False):
    root_dir = get_root_dir(is_relative_to_execute=is_relative_to_execute)
    basename = os.path.basename(path)
    if getattr(sys, 'frozen', False):
        return os.path.join(root_dir, basename)
    else:
        return os.path.join(root_dir, path)
# bb = r"C:\Users\admin\Desktop\short_task.bat"
# ba = r'pwd'
# os.system(bb)
# -*- coding:utf-8 -*-




subprocess.Popen("C:/Users/admin/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/short_task.bat")
