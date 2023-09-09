var arreglo1 = [];
var arreglo2 = [];

function guardarArreglo1() {
    var valor = document.getElementById("arreglo1").value;
    arreglo1.push(valor);
    document.getElementById("arreglo1").value = "";
}

function guardarArreglo2() {
    var valor = document.getElementById("arreglo2").value;
    arreglo2.push(valor);
    document.getElementById("arreglo2").value = "";
}

function mostrarArreglos() {
    document.getElementById("Marreglo1").textContent = "Arreglo 1: " + arreglo1.join(", ");
    document.getElementById("Marreglo2").textContent = "Arreglo 2: " + arreglo2.join(", ");
}