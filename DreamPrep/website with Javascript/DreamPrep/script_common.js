document.getElementById("btn").addEventListener("click", function(e) {
  e.preventDefault()


  User_Name = document.getElementById("username").value;
  Password = document.getElementById("password");

  localStorage.setItem("USER", User_Name);
  localStorage.setItem("PASSWORD", Password);

  window.location.href = "dashboard.html";
})



function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}


function Login(){
window.location = "./login_page.html";
}

function Signup(){
window.location.href = "./Signup.html";
}


// Time Scheduling Submit Button 

function Submit(){

if((document.getElementById("UPSC").selected == true) && (document.getElementById("4 hour").selected == true)){
  window.location.href = "./Timescheduling/UPSC/4-hour.html";
}if((document.getElementById("UPSC").selected == true) && (document.getElementById("5 hour").selected == true)){
  window.location.href = "./Timescheduling/UPSC/5-hour.html";
}if((document.getElementById("UPSC").selected == true) && (document.getElementById("6 hour").selected == true)){
  window.location.href = "./Timescheduling/UPSC/6-hour.html";

}if((document.getElementById("UPSC").selected == true) && (document.getElementById("7 hour").selected == true)){
  window.location.href = "./Timescheduling/UPSC/7-hour.html";
}if((document.getElementById("UPSC").selected == true) && (document.getElementById("8 hour").selected == true)){
  window.location.href = "./Timescheduling/UPSC/8-hour.html";
}
}