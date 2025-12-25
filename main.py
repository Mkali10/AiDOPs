from flask import Flask, request,jsonify
import json
from src.core.auth.access_control import check_access
from src.core.auth.otp_manager import generate_otp,verify_otp

app=Flask(__name__)
USER_FILE="src/core/auth/users.json"
def load_users():
    with open(USER_FILE) as f: return json.load(f)
def save_users(users):
    with open(USER_FILE,"w") as f: json.dump(users,f,indent=4)

@app.route("/login",methods=["POST"])
def login():
    data=request.json
    username=data.get("username")
    password=data.get("password")
    users=load_users()
    for u in users:
        if (u["username"]==username or u["mobile"]==username) and u["password"]==password:
            return jsonify({"status":"success","role":u["role"]})
    return jsonify({"status":"fail"}),401

@app.route("/send_otp",methods=["POST"])
def send_otp():
    mobile=request.json.get("mobile")
    code=generate_otp(mobile)
    print(f"Simulated OTP for {mobile}: {code}")
    return jsonify({"status":"sent"})

@app.route("/verify_otp",methods=["POST"])
def verify_otp_route():
    mobile=request.json.get("mobile")
    code=request.json.get("otp")
    if verify_otp(mobile,code): return jsonify({"status":"success"})
    return jsonify({"status":"fail"})

@app.route("/update_user",methods=["POST"])
def update_user():
    data=request.json
    users=load_users()
    for u in users:
        if u["username"]==data.get("username"):
            u["username"]=data.get("username",u["username"])
            u["password"]=data.get("password",u["password"])
            u["mobile"]=data.get("mobile",u.get("mobile",""))
    save_users(users)
    return jsonify({"status":"success"})

if __name__=="__main__":
    app.run(port=5000)
