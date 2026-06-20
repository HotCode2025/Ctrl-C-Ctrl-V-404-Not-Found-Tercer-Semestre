let ataqueJugador
let ataqueEnemigo

function iniciarJuego() {
    let botonPersonajeJugador = document.getElementById("boton-seleccionar")

    botonPersonajeJugador.addEventListener(
        "click",
        seleccionarPersonajeJugador
    )

    let botonPunio = document.getElementById("boton-punio")
    botonPunio.addEventListener("click", ataquePunio)

    let botonPatada = document.getElementById("boton-patada")
    botonPatada.addEventListener("click", ataquePatada)

    let botonBarrida = document.getElementById("boton-barrida")
    botonBarrida.addEventListener("click", ataqueBarrida)
}

function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min
}

function seleccionarPersonajeJugador() {
    let inputZuko = document.getElementById("zuko")
    let inputAang = document.getElementById("aang")
    let inputKatara = document.getElementById("katara")
    let inputToph = document.getElementById("toph")

    let spanPersonajeJugador =
        document.getElementById("personaje-jugador")

    if (inputZuko.checked) {
        spanPersonajeJugador.innerHTML = "Zuko"
    } else if (inputAang.checked) {
        spanPersonajeJugador.innerHTML = "Aang"
    } else if (inputKatara.checked) {
        spanPersonajeJugador.innerHTML = "Katara"
    } else if (inputToph.checked) {
        spanPersonajeJugador.innerHTML = "Toph"
    } else {
        alert("Selecciona un personaje para jugar")
        return
    }

    seleccionarPersonajeEnemigo()
}

function seleccionarPersonajeEnemigo() {
    let personajeAleatorio = aleatorio(1, 4)

    let spanPersonajeEnemigo =
        document.getElementById("personaje-enemigo")

    if (personajeAleatorio == 1) {
        spanPersonajeEnemigo.innerHTML = "Zuko"
    } else if (personajeAleatorio == 2) {
        spanPersonajeEnemigo.innerHTML = "Aang"
    } else if (personajeAleatorio == 3) {
        spanPersonajeEnemigo.innerHTML = "Katara"
    } else {
        spanPersonajeEnemigo.innerHTML = "Toph"
    }
}

function ataquePunio() {
    ataqueJugador = "Punio"
    ataqueAleatorioEnemigo()
}

function ataquePatada() {
    ataqueJugador = "Patada"
    ataqueAleatorioEnemigo()
}

function ataqueBarrida() {
    ataqueJugador = "Barrida"
    ataqueAleatorioEnemigo()
}

function ataqueAleatorioEnemigo() {
    let ataqueAleatorio = aleatorio(1, 3)

    if (ataqueAleatorio == 1) {
        ataqueEnemigo = "Punio"
    } else if (ataqueAleatorio == 2) {
        ataqueEnemigo = "Patada"
    } else {
        ataqueEnemigo = "Barrida"
    }

    combate()
}

function combate() {
    if (ataqueEnemigo == ataqueJugador) {
        crearMensaje("Empate")
    } else if (
        ataqueJugador == "Punio" &&
        ataqueEnemigo == "Barrida"
    ) {
        crearMensaje("Ganaste")
    } else if (
        ataqueJugador == "Patada" &&
        ataqueEnemigo == "Punio"
    ) {
        crearMensaje("Ganaste")
    } else if (
        ataqueJugador == "Barrida" &&
        ataqueEnemigo == "Patada"
    ) {
        crearMensaje("Ganaste")
    } else {
        crearMensaje("Perdiste")
    }
}

function crearMensaje(resultado) {
    let sectionMensaje =
        document.getElementById("mensajes")

    let parrafo = document.createElement("p")

    parrafo.innerHTML =
        "Tu personaje atacó con " +
        ataqueJugador +
        ", el enemigo atacó con " +
        ataqueEnemigo +
        ". " +
        resultado

    sectionMensaje.appendChild(parrafo)
}

window.addEventListener("load", iniciarJuego)