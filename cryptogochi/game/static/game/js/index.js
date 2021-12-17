let regBtm = document.querySelector(".reg-btm"),
    LogInBtm = document.querySelector(".log-in-btm"),
    regBox = document.querySelector(".reg-box"),
    LogInBox = document.querySelector(".log-in-box");

    regBtm.onclick = showRegForm;
    LogInBtm.onclick = showLogForm;
    
function showLogForm(){
    LogInBox.style.display = "block";
    LogInBtm.style.top = "0";
    LogInBtm.style.fontSize = "2em";
    regBox.style.display = "none";
    regBtm.style.top = "50px";
    regBtm.style.fontSize = ".9em";
}
function showRegForm(){
    regBox.style.display = "block";
    regBtm.style.top = "0";
    regBtm.style.fontSize = "2em";
    LogInBox.style.display = "none";
    LogInBtm.style.top = "50px";
    LogInBtm.style.fontSize = ".9em";
}
