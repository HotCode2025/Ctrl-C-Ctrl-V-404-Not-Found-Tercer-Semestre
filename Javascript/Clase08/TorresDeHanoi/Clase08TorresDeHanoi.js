// TORRES DE HANOI - JAVASCRIPT
// Algoritmo Recursivo

// Cantidad de discos
const cantidadDiscos = 5;

// Guardar movimientos
let movimientos = [];

// Función recursiva
function hanoi(n, origen, auxiliar, destino) {

    // Caso base
    if (n === 1) {

        movimientos.push(
            `Mover disco 1 desde ${origen} hacia ${destino}`
        );

        return;
    }

    // Paso 1:
    // mover n-1 discos al auxiliar
    hanoi(
        n - 1,
        origen,
        destino,
        auxiliar
    );

    // Paso 2:
    // mover disco mayor al destino
    movimientos.push(
        `Mover disco ${n} desde ${origen} hacia ${destino}`
    );

    // Paso 3:
    // mover n-1 discos al destino
    hanoi(
        n - 1,
        auxiliar,
        origen,
        destino
    );
}

// Ejecutar algoritmo
hanoi(
    cantidadDiscos,
    "A",
    "B",
    "C"
);

// Mostrar resultado
console.log("===== TORRES DE HANOI =====\n");

movimientos.forEach((movimiento, index) => {

    console.log(
        `Paso ${index + 1}: ${movimiento}`
    );

});

console.log(
    `\nTotal de movimientos: ${movimientos.length}`
);