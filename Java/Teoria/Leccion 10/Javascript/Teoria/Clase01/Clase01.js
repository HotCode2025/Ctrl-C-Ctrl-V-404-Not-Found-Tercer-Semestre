/* Documentación del archivo Clase01.js
 Este archivo implementa un sistema simple para gestionar dispositivos de entrada, monitores, computadoras y órdenes de compra.
 Se organiza en tres secciones principales:
 1. Declaración de clases: Definición de las clases base y derivadas.
 2. Herencias: Clases que heredan de otras.
 3. Creación de órdenes: Instanciación de objetos y creación de órdenes.
*/

// 1. Declaración de clases

// Clase base para dispositivos de entrada
class DispositivoEntrada {
  constructor(tipoEntrada, marca) {
    this._tipoEntrada = tipoEntrada;
    this._marca = marca;
  }

  get tipoEntrada() {
    return this._tipoEntrada;
  }
  set tipoEntrada(tipoEntrada) {
    this._tipoEntrada = tipoEntrada;
  }

  get marca() {
    return this._marca;
  }
  set marca(marca) {
    this._marca = marca;
  }
}

// 2. Herencias

// Raton hereda de DispositivoEntrada
class Raton extends DispositivoEntrada {
  static contadorRatones = 0;

  constructor(tipoEntrada, marca) {
    super(tipoEntrada, marca);
    this._idRaton = ++Raton.contadorRatones;
  }

  toString() {
    return `Raton: [idRaton: ${this._idRaton}, tipoEntrada: ${this.tipoEntrada}, marca: ${this.marca}]`;
  }
}

class Teclado extends DispositivoEntrada {
  static contadorTeclados = 0;

  constructor(tipoEntrada, marca) {
    super(tipoEntrada, marca);
    this._idTeclado = ++Teclado.contadorTeclados;
  }

  toString() {
    return `Teclado: [idTeclado: ${this._idTeclado}, tipoEntrada: ${this.tipoEntrada}, marca: ${this.marca}]`;
  }
}

// Clase Monitor independiente
class Monitor {
  static contadorMonitores = 0;

  constructor(marca, tamaño) {
    this._idMonitor = ++Monitor.contadorMonitores;
    this._marca = marca;
    this._tamaño = tamaño;
  }

  get idMonitor() {
    return this._idMonitor;
  }

  get marca() {
    return this._marca;
  }
  set marca(marca) {
    this._marca = marca;
  }

  get tamaño() {
    return this._tamaño;
  }
  set tamaño(tamaño) {
    this._tamaño = tamaño;
  }

  toString() {
    return `Monitor: [idMonitor: ${this._idMonitor}, marca: ${this._marca}, tamaño: ${this._tamaño}]`;
  }
}

// Clase Computadora que agrupa monitor, teclado y raton
class Computadora {
  static contadorComputadoras = 0;

  constructor(nombre, monitor, teclado, raton) {
    this._idComputadora = ++Computadora.contadorComputadoras;
    this._nombre = nombre;
    this._monitor = monitor;
    this._teclado = teclado;
    this._raton = raton;
  }

  get idComputadora() {
    return this._idComputadora;
  }
  get nombre() {
    return this._nombre;
  }
  set nombre(nombre) {
    this._nombre = nombre;
  }
  get monitor() {
    return this._monitor;
  }
  set monitor(monitor) {
    this._monitor = monitor;
  }
  get teclado() {
    return this._teclado;
  }
  set teclado(teclado) {
    this._teclado = teclado;
  }
  get raton() {
    return this._raton;
  }
  set raton(raton) {
    this._raton = raton;
  }

  toString() {
    return `Computadora ${this._idComputadora}: ${this._nombre} \n ${this._monitor} \n ${this._raton} \n ${this._teclado}`;
  }
}

// Clase Orden para gestionar listas de computadoras
class Orden {
  static contadorOrdenes = 0;

  constructor() {
    this._idOrden = ++Orden.contadorOrdenes;
    this._computadoras = [];
  }

  get idOrden() {
    return this._idOrden;
  }

  agregarComputadora(computadora) {
    this._computadoras.push(computadora);
  }

  mostrarOrden() {
    let computadorasOrden = "";
    for (let computadora of this._computadoras) {
      computadorasOrden += `\n${computadora.toString()}`;
    }

    console.log(`Orden: ${this._idOrden}, Computadoras: ${computadorasOrden}`);
  }
}

// 3. Creación de órdenes

let raton1 = new Raton("USB", "Logitech");
let raton2 = new Raton("Bluetooth", "Genius");
console.log(raton1.toString());
console.log(raton2.toString());

let teclado1 = new Teclado("USB", "Redragon");
console.log(teclado1.toString());
let monitor1 = new Monitor("Samsung", "27 pulgadas");
let monitor2 = new Monitor("LG", "24 pulgadas");
console.log(monitor1.toString());
console.log(monitor2.toString());

let compu1 = new Computadora("HP", monitor1, teclado1, raton1);
console.log(compu1.toString());

let compu2 = new Computadora("Gamer Armada", monitor2, teclado1, raton2);
console.log(compu2.toString());

let orden1 = new Orden();
orden1.agregarComputadora(compu1);
orden1.agregarComputadora(compu2);
orden1.mostrarOrden();

let orden2 = new Orden();
orden2.agregarComputadora(compu2);
orden2.mostrarOrden();
