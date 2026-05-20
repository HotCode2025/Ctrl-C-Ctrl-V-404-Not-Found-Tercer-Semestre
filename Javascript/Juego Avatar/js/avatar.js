let botonPersonajeJugador = document.getElementById("boton-seleccionar");

botonPersonajeJugador.addEventListener("click", seleccionarPersonajeJugador);

function seleccionarPersonajeJugador() {
  let inputZuko = document.getElementById("zuko");
  let inputAang = document.getElementById("aang");
  let inputKatara = document.getElementById("katara");
  let inputToph = document.getElementById("toph");

  if (inputZuko.checked) {
    alert("Has seleccionado a Zuko");
  } else if (inputAang.checked) {
    alert("Has seleccionado a Aang");
  } else if (inputKatara.checked) {
    alert("Has seleccionado a Katara");
  } else if (inputToph.checked) {
    alert("Has seleccionado a Toph");
  } else {
    alert("Selecciona un personaje para jugar");
  }
}
