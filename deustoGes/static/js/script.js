

let telefono = document.getElementById("id_telefono");
    telefono.addEventListener("input", validarTlf)


function validarTlf (){

    let errorTelefono = document.getElementById("error_telefono")

    errorTelefono.innerHTML = "";
    if (telefono.value.length !== 9){
        let p = document.createElement("p");
        p.className = "comentario-error-formulario";
        p.innerHTML = "No es un teléfono válido";
        errorTelefono.appendChild(p);
        return false;
    }
    return true;
}

let formulario = document.getElementById("formulario");
formulario.addEventListener("submit", noEnviar);

function noEnviar(event){
    if (!validarTlf()){
        event.preventDefault();
    }
}




//intento de implementar funcionalidad de que se rellene automáticamente el apartado Usuario con Nombre.Apellidos

let nombre = document.getElementById("id_nombre");
let apellidos = document.getElementById("id_apellidos");
let usuario = document.getElementById("id_usuario");
nombre.addEventListener("input", crearNombreUsuario);
apellidos.addEventListener("input", crearNombreUsuario);

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
