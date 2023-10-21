
const mascotas = {};

//funcion para generar un ID aletorio
function generarID (){
    return Math.random().toString(35).substring(2,15)+ Math.random().toString(36).substring(2,15);
}

//Gurfar mascota 

function gurdarMascota(){
    const nombre= document.getElementById("nombre").value;
    const raza= document.getElementById("raza").value;
    const peso = document.getElementById("peso").value;
    const color=document.getElementById("color").value;
    const consulta = document.getElementById("consulta").value;
    const ID = generarID ();

    //Alamacenar datos 

    mascotas{ID} = {
        nombre,
        raza,
        peso,
        color,
        consulta
    };
    

}