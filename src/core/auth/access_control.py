ROLE_PERMISSIONS={"admin":["all"],"supervisor":["view_logs","minor_fix","limited_files"],"guest":["view_logs"]}
def check_access(role,permission):
    if role not in ROLE_PERMISSIONS: return False
    if "all" in ROLE_PERMISSIONS[role]: return True
    return permission in ROLE_PERMISSIONS[role]
