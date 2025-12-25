def analyze_logs(logs):
    errors=[]
    for l in logs:
        if "ERROR" in l: errors.append(l)
    return errors
