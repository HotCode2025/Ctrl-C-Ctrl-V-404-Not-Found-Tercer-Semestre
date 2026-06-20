// Saludo setTimeout
function miFuncionBatman(){
    document.getElementById("mensaje").innerHTML += "Ctr C + Ctrl V = 404 Not Found <br>";/* */
}

setTimeout(miFuncionBatman, 3000);

setTimeout(function() {
    document.getElementById("mensaje").innerHTML += "Buenas noches Profe <br>";
}, 5000);

let reloj = () => {

    let fecha = new Date ();

    let horas = fecha.getHours().toString().padStart(2, '0');
    let minutos = fecha.getMinutes().toString().padStart(2, '0');
    let segundos = fecha.getSeconds().toString().padStart(2, '0');

    document.getElementById("reloj").innerHTML =
    `${horas}:${minutos}:${segundos}`;
}

reloj();

setInterval(reloj, 1000);