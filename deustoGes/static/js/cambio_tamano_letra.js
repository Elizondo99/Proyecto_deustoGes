let element = document.getElementById('boton_tamano');
element.addEventListener('click',cambiarTamano)

function cambiarTamano() {
    let elementos = document.getElementsByClassName("estilos-table");

         for (let i = 0; i < elementos.length; i++) {
        elementos[i].style.fontSize = '30px';

    }
}

let element_1 = document.getElementById('boton_tamano_pequeno');
element_1.addEventListener('click',cambiarTamano_p)

function cambiarTamano_p() {
    let elementos_1 = document.getElementsByClassName("estilos-table");

         for (let i = 0; i < elementos_1.length; i++) {
        elementos_1[i].style.fontSize = '16px';

    }
}
