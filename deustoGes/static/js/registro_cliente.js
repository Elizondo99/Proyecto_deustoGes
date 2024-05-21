

let nombre_cliente = document.getElementById("id_nombre");
let usuario_cliente = document.getElementById("id_usuario");
nombre_cliente.addEventListener("input", crearNombreUsuarioCliente)

function crearNombreUsuarioCliente(){
    let nombre_introducido_cliente = nombre_cliente.value.trim();
    if(nombre_cliente){
        usuario_cliente.value = `${nombre_introducido_cliente}.cl`
    } else{
        usuario_cliente.value = '';
    }
}