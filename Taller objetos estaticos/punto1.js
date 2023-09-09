var DatosVeiculos = {
    "ABC123": {
        marca: "Toyota",
        color: "Rojo",
        valor: "$25,000"
    },
    "XYZ789": {
        marca: "Honda",
        color: "Azul",
        valor: "$20,000"
    }
};


function mostrarInformacion() {
    var placa = document.getElementById("placa").value;
    var vehiculo = DatosVeiculos[placa];

    if (vehiculo) {
        document.getElementById("marca").value = vehiculo.marca;
        document.getElementById("color").value = vehiculo.color;
        document.getElementById("valor").value = vehiculo.valor;
    } else {
        alert("Placa no encontrada en la base de datos.");
    }
}