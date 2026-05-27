function iniciarJuego() {
  let botonPersonajeJugador = document.getElementById("boton-seleccionar");

  botonPersonajeJugador.addEventListener("click", seleccionarPersonajeJugador);
}

function aleatorio(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function seleccionarPersonajeJugador() {
  let inputZuko = document.getElementById("zuko");
  let inputAang = document.getElementById("aang");
  let inputKatara = document.getElementById("katara");
  let inputToph = document.getElementById("toph");

  let spanPersonajeJugador = document.getElementById("personaje-jugador");

  if (inputZuko.checked) {
    spanPersonajeJugador.innerHTML = "Zuko";
  } else if (inputAang.checked) {
    spanPersonajeJugador.innerHTML = "Aang";
  } else if (inputKatara.checked) {
    spanPersonajeJugador.innerHTML = "Katara";
  } else if (inputToph.checked) {
    spanPersonajeJugador.innerHTML = "Toph";
  } else {
    alert("Selecciona un personaje para jugar");
  }

  seleccionarPersonajeEnemigo();
}

function seleccionarPersonajeEnemigo() {
  let spanPersonajeEnemigo = document.getElementById("personaje-enemigo");
  let personajeAleatorio = aleatorio(1, 4);

  if (personajeAleatorio == 1) {
    spanPersonajeEnemigo.innerHTML = "Zuko";
  } else if (personajeAleatorio == 2) {
    spanPersonajeEnemigo.innerHTML = "Aang";
  } else if (personajeAleatorio == 3) {
    spanPersonajeEnemigo.innerHTML = "Katara";
  } else if (personajeAleatorio == 4) {
    spanPersonajeEnemigo.innerHTML = "Toph";
  }
}

window.addEventListener("load", iniciarJuego);
