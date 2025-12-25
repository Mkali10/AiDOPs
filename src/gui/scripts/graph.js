function drawFlow(data){
    const container=document.getElementById("graphContainer");
    container.innerHTML="";
    data.forEach(unit=>{
        const div=document.createElement("div");
        div.className="flow-unit";
        div.innerHTML=`<strong>${unit.name}</strong><br>${unit.path}<br>Status: ${unit.status}`;
        container.appendChild(div);
    });
}

drawFlow([
    {name:"app.js",path:"/home/app.js",status:"Active"},
    {name:"db.js",path:"/home/db.js",status:"Connected"},
    {name:".env",path:"/home/.env",status:"Warning"}
]);
