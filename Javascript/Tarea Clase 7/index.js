
function reinas(n) {
    const soluciones = []; // Aquí guardaremos las soluciones encontradas
    const columnas = Array(n);
    
function valido(fila, col) {
    // Recorre SOLO las filas que ya tienen reinas (0 hasta fila-1)
    for (let i = 0; i < fila; i++) {
        
        // ¿Alguna reina está en la MISMA COLUMNA? ATAQUE VERTICAL
        if (columnas[i] === col) 
            return false;
        
        // ¿Alguna reina está en la MISMA DIAGONAL?
        // |diferencia de columnas| = |diferencia de filas|
        if (Math.abs(columnas[i] - col) === fila - i) 
            return false;
    }
    
    return true;
}
    
    function buscar(fila) {
        if (fila === n) {
            soluciones.push([...columnas]);
            return;
        }
        
        for (let col = 0; col < n; col++) {
            if (valido(fila, col)) {
                columnas[fila] = col;
                buscar(fila + 1);
            }
        }
    }
    
    buscar(0);
    return soluciones;
}

//Ejecucion del programa

console.log('Soluciones para 8 reinas:');
const sols = reinas(8);
console.log(`Total: ${sols.length}`);
console.log('Primera solución:', sols[0]);
console.log('Segunda solución:', sols[1]);
console.log('Tercera solución:', sols[2]);
