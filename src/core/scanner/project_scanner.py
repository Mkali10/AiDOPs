import os,json
def scan_project(path="."):
    files=[]
    for root,_,fs in os.walk(path):
        for f in fs: files.append(os.path.join(root,f))
    return files
def save_scan_report(files):
    with open("data/reports/scan.json","w") as f: json.dump(files,f,indent=4)
