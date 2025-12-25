import random
otp_store={}
def generate_otp(mobile):
    code=str(random.randint(1000,9999))
    otp_store[mobile]=code
    return code
def verify_otp(mobile,code):
    return otp_store.get(mobile)==code
