"use strict";
//Para evitar errores
try {
  let x = 10;
  //miFuncion();
  throw "Mi Error";
} catch (error) {
  console.log(typeof error);
} finally {
  console.log("Termina la revision de errores");
}
console.log("continuamos... ");

let resultado = -8;

try {
  //y = 5
  if (isNaN(resultado)) throw "No es un numero";
  else if (resultado === "") throw "es una cadena vacia";
  else if (resultado >= 0) throw "valor positivo";
  else if (resultado <= 0) throw "valor negativo";
} catch (error) {
  console.log(error);
  console.log(error.name);
  console.log(error.message);
} finally {
  console.log("termina la revision 2");
}
