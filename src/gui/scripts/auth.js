async function login(){
    const username=document.getElementById("username").value;
    const password=document.getElementById("password").value;

    const response=await fetch("http://127.0.0.1:5000/login",{
        method:"POST",
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({username,password})
    });

    const data=await response.json();
    if(data.status==="success"){
        window.location.href="dashboard.html?role="+data.role;
    } else {
        document.getElementById("loginMessage").innerText="Login failed!";
    }
}

function showForgot(){document.getElementById("forgotPassword").style.display="block";}

async function sendOTP(){
    const mobile=document.getElementById("otpMobile").value;
    await fetch("http://127.0.0.1:5000/send_otp",{method:"POST",headers:{'Content-Type':'application/json'},body:JSON.stringify({mobile})});
    alert("OTP Sent (Simulated)");
}

async function verifyOTP(){
    const mobile=document.getElementById("otpMobile").value;
    const otp=document.getElementById("otpCode").value;
    const res=await fetch("http://127.0.0.1:5000/verify_otp",{method:"POST",headers:{'Content-Type':'application/json'},body:JSON.stringify({mobile,otp})});
    const data=await res.json();
    if(data.status==="success"){alert("OTP Verified. Login allowed.");}
    else{alert("OTP Failed");}
}
