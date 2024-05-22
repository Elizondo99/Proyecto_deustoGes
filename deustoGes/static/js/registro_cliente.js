

let nombre_cliente = document.getElementById("id_nombre");
let usuario_cliente = document.getElementById("id_usuario");
nombre_cliente.addEventListener("input", crearNombreUsuarioCliente);
usuario_cliente.addEventListener("input", validarNombreUsuarioCliente);

function crearNombreUsuarioCliente(){
    let nombre_introducido_cliente = nombre_cliente.value.trim();
    if(nombre_cliente){
        usuario_cliente.value = `${nombre_introducido_cliente}.cl`
    } else{
        usuario_cliente.value = '';
    }
}

function validarNombreUsuarioCliente(){
    let errorUsuario = document.getElementById("error_usuario");
    errorUsuario.innerHTML = "";

    if(usuario_cliente.value.slice(-3) !== '.cl'){
        let comentarioErrorUsuario = document.createElement("p");
        comentarioErrorUsuario.innerHTML = "El usuario debe terminar en '.cl'.";
        comentarioErrorUsuario.style.color="red";
        errorUsuario.appendChild(comentarioErrorUsuario);
        return false;
    }
    return true;
}

let formulario_registro = document.getElementById("formulario_registro");
formulario_registro.addEventListener("submit", noEnviarRegistro);

function noEnviarRegistro(event){
    if (!validarNombreUsuarioCliente()){
        event.preventDefault();
    }
}