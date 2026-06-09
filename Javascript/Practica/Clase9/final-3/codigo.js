javascript
const formulario = document.getElementById("loginForm");

const errorBox = document.getElementById("errorBox");

formulario.addEventListener("submit", function(e){

    e.preventDefault();

    errorBox.style.display = "block";

});
