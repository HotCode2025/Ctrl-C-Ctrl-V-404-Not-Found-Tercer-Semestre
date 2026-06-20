let jugador = 0;
let computadora = 0;
let ronda = 1;
let juegoTerminado = false;

function numerosAleatorios(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function nombreEleccion(numero){

  if(numero === 1){
    return "🪨 Piedra";
  }

  else if(numero === 2){
    return "📄 Papel";
  }

  else{
    return "✂️ Tijera";
  }
}

function jugar(eleccionJugador){

  if(juegoTerminado){
    return;
  }

  const eleccionComputadora = numerosAleatorios(1, 3);

  let mensaje = `
    Vos elegiste ${nombreEleccion(eleccionJugador)} <br>
    La computadora eligió ${nombreEleccion(eleccionComputadora)} <br><br>
  `;

  if(eleccionJugador === eleccionComputadora){

    mensaje += "🤝 Empate";

  }

  else if(
    (eleccionJugador === 1 && eleccionComputadora === 3) ||
    (eleccionJugador === 2 && eleccionComputadora === 1) ||
    (eleccionJugador === 3 && eleccionComputadora === 2)
  ){

    mensaje += "🎉 ¡Ganaste la ronda!";
    jugador++;

  }

  else{

    mensaje += "💀 ¡Perdiste la ronda!";
    computadora++;
  }

  document.getElementById("resultado").innerHTML = mensaje;

  document.getElementById("marcador").innerHTML =
    `Jugador ${jugador} - ${computadora} Computadora`;

  ronda++;

  document.getElementById("ronda").innerHTML =
    `Ronda ${ronda}`;

  if(jugador === 3){

    document.getElementById("ganador").innerHTML =
      "🏆 ¡GANASTE LA PARTIDA!";

    juegoTerminado = true;
  }

  if(computadora === 3){

    document.getElementById("ganador").innerHTML =
      "💻 LA COMPUTADORA GANÓ";

    juegoTerminado = true;
  }
}

function reiniciarJuego(){

  jugador = 0;
  computadora = 0;
  ronda = 1;
  juegoTerminado = false;

  document.getElementById("resultado").innerHTML =
    "Elegí una opción";

  document.getElementById("marcador").innerHTML =
    "Jugador 0 - 0 Computadora";

  document.getElementById("ronda").innerHTML =
    "Ronda 1";

  document.getElementById("ganador").innerHTML = "";
}
