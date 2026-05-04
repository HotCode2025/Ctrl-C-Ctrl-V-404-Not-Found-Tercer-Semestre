function miFuncion() {
  console.log("Saludos desde mi funcion");
}

miFuncion();

let myFuncion = function () {
  console.log("saludos desde funcion anonima");
};

let miFuncionFlecha = () => {
  console.log("saludos desde mi fucnon flecha");
};
// hay mas variantes para funciones flecha
miFuncionFlecha();

// lo hacemos en una linea
const saludar = () => console.log("1 sadludos a todos desde funcion flecha ");

//console.log(saludar()); undefined
saludar();

const saludo = () => {
  return "saludos";
};

console.log(saludo());

// simplificamos la funcion anterior

const saludo2 = () => "saludos 2";

console.log(saludo2());

const regresaObjeto = () => ({ nombre: "juan", apellido: "larro" });

console.log(regresaObjeto());

const funcionParametros = (mensjae) => console.log(mensjae);

funcionParametros("saludos desde funcion con parametros");

//funcion clasica

const funcionParametrosClasico = function (mensjae) {
  console.log(mensjae);
};

funcionParametrosClasico("saludos desde funcion clasica");

const funcionConParametros = (mensjae) => console.log(mensjae);

funcionConParametros("otra forma con funcion flecha");

const funConParametros2 = (op1, op2) => {
  let resultado = op1 + op2;
  return resultado;
};
