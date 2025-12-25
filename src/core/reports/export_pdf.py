# Placeholder for future PDF export functionality
def export_pdf(report, path="data/reports/report.pdf"):
    with open(path.replace(".pdf",".json"),"w") as f:
        import json
        json.dump(report,f,indent=4)
