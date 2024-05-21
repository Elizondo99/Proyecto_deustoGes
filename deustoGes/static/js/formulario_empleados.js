

let nombre = document.getElementById("id_nombre");
let apellidos = document.getElementById("id_apellidos");
let usuario = document.getElementById("id_usuario");
let email = document.getElementById("id_email")
nombre.addEventListener("input", crearNombreUsuario);
apellidos.addEventListener("input", crearNombreUsuario);
nombre.addEventListener("input", crearEmailEmpleado);
apellidos.addEventListener("input", crearEmailEmpleado);
email.addEventListener("input", validarEmail);

function crearNombreUsuario(){
    let nombre_introducido = nombre.value.trim();
    let apellido_introducido = apellidos.value.trim();
    if(nombre_introducido && apellido_introducido){
        usuario.value = `${nombre_introducido}.${apellido_introducido}`;
    }else if(nombre_introducido){
        usuario.value = nombre_introducido;
    }else{
        usuario.value = "";
    }
}

function crearEmailEmpleado(){
    let nombre_introducido = nombre.value.trim();
    let apellido_introducido = apellidos.value.trim();
    if(nombre_introducido && apellido_introducido){
        email.value = `${nombre_introducido}.${apellido_introducido}@deustoges.com`;
    }else if(nombre_introducido){
        email.value = nombre_introducido;
    }else{
        email.value = "";
    }
}

function validarEmail(event){

    let errorEmail = document.getElementById("error_email")
    errorEmail.innerHTML = "";
    if (email.value.slice(-14) !== '@deustoges.com'){
        let p = document.createElement("p");
        p.innerHTML = "El email debe ser '...@deustoges.com'";
        p.style.color="red";
        errorEmail.appendChild(p);
        return false;
    }
    return true;
}
