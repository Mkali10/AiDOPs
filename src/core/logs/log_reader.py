def read_logs(path="data/logs/"):
    import os
    logs=[]
    for f in os.listdir(path):
        with open(os.path.join(path,f)) as file: logs.append(file.read())
    return logs
