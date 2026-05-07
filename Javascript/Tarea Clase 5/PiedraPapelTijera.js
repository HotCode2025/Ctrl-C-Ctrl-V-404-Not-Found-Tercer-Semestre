function numerosAleatorios(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

let jugador = 0;
let computadora = 0;
const eleccionJugador = parseInt(
  prompt("Elige: 1 Piedra, 2 Papel o 3 Tijera"),
  10,
);
const eleccionComputadora = numerosAleatorios(1, 3);

if (eleccionJugador === 1) {
  alert("Elegiste Piedra");
} else if (eleccionJugador === 2) {
  alert("Elegiste Papel");
} else if (eleccionJugador === 3) {
  alert("Elegiste Tijera");
} else {
  alert("Elección no válida");
}

alert(`La computadora eligió: ${eleccionComputadora === 1 ? "Piedra" : eleccionComputadora === 2 ? "Papel" : "Tijera"}`);

if (eleccionJugador === eleccionComputadora) {
  alert("Empate");
} else if (
  (eleccionJugador === 1 && eleccionComputadora === 3) ||
  (eleccionJugador === 2 && eleccionComputadora === 1) ||
  (eleccionJugador === 3 && eleccionComputadora === 2)
) {
  alert("¡Ganaste!");
  jugador++;
} else {
  alert("¡Perdiste!");
  computadora++;
}
alert(`Puntuación: Jugador ${jugador} - Computadora ${computadora}`);
