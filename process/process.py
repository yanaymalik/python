import psutil
import time

run = []

def check_if_in(pr_list,name,pid):
    for p in pr_list:
        if pid == p['pid'] and name == p['name']:
            return True 
    return False

def check_new(current):
    new_list = []
    for n_process in current:
        if not check_if_in(run,n_process['name'], n_process['pid']):
            new_list.append(n_process['name'])
            run.append(n_process)
    return new_list

def check_del(current):
    del_list = []
    for p in run:
        if not check_if_in(current, p['name'], p['pid']):
            del_list.append(p['name'])
            run.remove(p)
    return del_list
  
while True:
    new_process = []
    deleted_process = []
    current = []
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        current.append(proc.info)
    new_process = check_new(current)
    deleted_process = check_del(current)
    if len(new_process) > 0:
        print("--------{} new process--------".format(len(new_process)))
        f = open("Status_log.txt", 'a')
        f.writelines("--------{} new process--------\n".format(len(new_process)))
        for p in new_process:
            f.write(p)
            f.write("\n")
            print(p)
        f.close()
    if len(deleted_process) > 0:
        print("---------- {} deleted process---------".format(len(deleted_process)))
        for p in deleted_process:
            print(p)
    print("sleep")
    time.sleep(6)