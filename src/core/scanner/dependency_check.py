import subprocess
def check_dependencies(packages=["flask"]):
    result={}
    for p in packages:
        try: subprocess.run(["pip","show",p],check=True)
        except: result[p]="Missing"
        else: result[p]="Installed"
    return result
