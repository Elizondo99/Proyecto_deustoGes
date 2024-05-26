

let contrasena = document.getElementById("id_password1");
contrasena.addEventListener("input", validarContrasena)



function validarContrasena() {
    let errorContrasena = document.getElementById("error_contrasena")
    errorContrasena.innerHTML = "";
    let contrasena_corta = document.createElement("p");
    contrasena_corta.className = "comentario-error-formulario";
    contrasena_corta.innerHTML = "❌​ Contraseña demasiado corta.";
    errorContrasena.appendChild(contrasena_corta);

    if (contrasena.value.length > 8) {
        contrasena_corta.innerHTML = "✔️​ Longitud de contraseña adecuada.";
    }

    let contrasena_mayuscula = document.createElement("p");
    contrasena_mayuscula.className = "comentario-error-formulario";
    contrasena_mayuscula.innerHTML = "❌​ La contraseña debe contener al menos una letra mayúscula.";
    errorContrasena.appendChild(contrasena_mayuscula);

    if (/[A-Z]/.test(contrasena.value)) {
        contrasena_mayuscula.innerHTML = "✔️​ La contraseña contiene una letra mayúscula.";
    }

    let contrasena_caracter = document.createElement("p");
    contrasena_caracter.className = "comentario-error-formulario";
    contrasena_caracter.innerHTML = "❌​ La contraseña debe contener al menos un carácter especial.";
    errorContrasena.appendChild(contrasena_caracter);

    if (/[<>,.;:_{}´ç¨`^*+ªº!|"@·#$~%&¬()=?'¡¿]/.test(contrasena.value)) {
        contrasena_caracter.innerHTML = "✔️​  La contraseña debe contener al menos un carácter especial.";
    }

    let contrasena_numero = document.createElement("p");
    contrasena_numero.className = "comentario-error-formulario";
    contrasena_numero.innerHTML = "❌​ La contraseña debe contener al menos un número.";
    errorContrasena.appendChild(contrasena_numero);

    if (/[1234567890]/.test(contrasena.value)) {
        contrasena_numero.innerHTML = "✔️​ La contraseña debe contener al menos un número.";
    }









}