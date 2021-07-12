import os
import glob
path = r"C:\Users\admin\Desktop\digital_fbx"
# file_name_list = os.listdir(r"C:\Users\admin\Desktop\digital_fbx")
# for i in file_name_list:
#     file_path = os.path.join(path, i)

#
# res = (glob.glob(r"C:\Users\admin\Desktop\digital_fbx\*.fbx"))
# for i in res:
#     print(i.replace('\\', "/"))
# print(len(res))
import psutil, subprocess


def kill_process(pid):
    print("**** will kill pid", pid)
    if not psutil.pid_exists(pid):
        print("***** not found pid")
        return
    pids = [pid]
    p = psutil.Process(pid)
    while True:
        if p.parent() is None:
            break
        if p.parent().name().lower() in ["cmd.exe", "conhost.exe", "okra.exe", "python.exe"]:
            pids.append(p.parent().pid)
            p = p.parent()
        else:
            break
    for i in pids:
        subprocess.run(f"taskkill /pid {i} /t /f ", shell=True)


def kill_okra():
    for p in psutil.process_iter():
        try:
            if "okra" not in p.cmdline() and "okra" not in p.name():
                continue
            print(p.name(), p.cmdline())
            cmdline = p.cmdline()
            if p.name() == "okra.exe":
                print("*** match okra")
                kill_process(p.pid)
            if p.name() == "cmd.exe" and "okra.exe" in cmdline and "--broker=" in cmdline:
                print("** match cmd")
                kill_process(p.pid)
        except Exception as e:
            print("!!!!", e)
            pass
kill_okra()