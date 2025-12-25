import json,datetime
def generate_report(data,user_role):
    report={"generated_by":user_role,"timestamp":str(datetime.datetime.now()),"summary":data.get("summary",""),"issues":data.get("issues",[]),"paths":data.get("paths",[])}
    return report
def export_report_pdf(report,file_path="data/reports/report.pdf"):
    with open(file_path.replace(".pdf",".json"),"w") as f: json.dump(report,f,indent=4)
