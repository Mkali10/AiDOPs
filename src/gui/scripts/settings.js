function saveSettings(){
    const username=document.getElementById("newUsername").value;
    const password=document.getElementById("newPassword").value;
    const mobile=document.getElementById("newMobile").value;
    fetch("http://127.0.0.1:5000/update_user",{
        method:"POST",
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({username,password,mobile})
    }).then(()=>document.getElementById("settingsMessage").innerText="Saved");
}
function openSettings(){window.location.href="settings.html";}
