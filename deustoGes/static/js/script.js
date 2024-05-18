

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

