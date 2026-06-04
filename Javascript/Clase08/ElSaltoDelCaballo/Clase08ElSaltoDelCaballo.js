
// PROBLEMA DEL SALTO DEL CABALLO

const N = 8;

// Movimientos posibles del caballo
const movX = [2, 1, -1, -2, -2, -1, 1, 2];
const movY = [1, 2, 2, 1, -1, -2, -2, -1];

// Crear tablero vacío
let tablero = Array.from({ length: N }, () =>
  Array(N).fill(-1)
);

// Posición inicial del caballo
tablero[0][0] = 0;

// Verifica si el movimiento es válido
function esValido(x, y, tablero) {
  return (
    x >= 0 &&
    y >= 0 &&
    x < N &&
    y < N &&
    tablero[x][y] === -1
  );
}

// Función recursiva Backtracking
function resolverSaltoCaballo(x, y, movimiento) {
  
  // Caso base: si recorrió las 64 casillas
  if (movimiento === N * N) {
    return true;
  }

  // Probar los 8 movimientos posibles
  for (let i = 0; i < 8; i++) {

    let siguienteX = x + movX[i];
    let siguienteY = y + movY[i];

    if (esValido(siguienteX, siguienteY, tablero)) {

      // Marcar movimiento
      tablero[siguienteX][siguienteY] = movimiento;

      // Llamada recursiva
      if (
        resolverSaltoCaballo(
          siguienteX,
          siguienteY,
          movimiento + 1
        )
      ) {
        return true;
      }

      // BACKTRACKING
      // Si no funciona, borrar movimiento
      tablero[siguienteX][siguienteY] = -1;
    }
  }

  return false;
}

// Mostrar tablero
function mostrarTablero(tablero) {
  for (let i = 0; i < N; i++) {
    console.log(
      tablero[i]
        .map(num => String(num).padStart(2, "0"))
        .join(" ")
    );
  }
}

// Ejecutar algoritmo
if (resolverSaltoCaballo(0, 0, 1)) {
  console.log("Solución encontrada:\n");
  mostrarTablero(tablero);
} else {
  console.log("No existe solución");
}