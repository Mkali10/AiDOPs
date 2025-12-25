import os
def check_env_vars(vars_list=["PATH","HOME"]):
    status={}
    for v in vars_list: status[v]=os.environ.get(v,"Not Set")
    return status
