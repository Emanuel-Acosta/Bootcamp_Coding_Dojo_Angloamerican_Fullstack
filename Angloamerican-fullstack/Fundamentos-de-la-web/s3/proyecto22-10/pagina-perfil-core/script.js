document.addEventListener("DOMContentLoaded", function () {
    const editarProfile = document.querySelectorAll("#editProfile");// elementos del DOM para editar perfil
    const namePerfil = document.getElementById("namePerfil");//elemento del DOM para nombre de perfil

    const cerrarSesion = document.getElementById("iniciar");// para editar el cerrar sesion

    const acceptButtons = document.querySelectorAll('.accept-btn'); //elementos del DOM para botones de aceptar
    let totalSoli = document.querySelectorAll('.connection-item').length; //conteo total de elementos de solicitudes
    let soliConnect = document.getElementById('soli-connect'); //texto para modificar total de solicitudes
    let conex = document.getElementById('total-connect'); //texto para modificar total de conexiones
    let totalConex = 500;

    const negarButtons = document.querySelectorAll('.negar-btn');// para negar boton

    let botonCambio = document.querySelectorAll("#editImg1" );
    let botonCambio2 = document.querySelectorAll("#editImg2");
    let imgIzq = document.getElementById("img");
    let imgDer = document.getElementById("img");



    
    

    

    //Para editar el perfil pero solo sirve una sola vez el cambio

    // Event listener para editar perfil
    // editarProfile.forEach(function(editButton) {
    //     editButton.addEventListener("click", function() {
    //         namePerfil.innerHTML = 'Acosta Emanuel  <i class="fa-solid fa-user-tie"></i>'; // utilizar siempre comillas simples para concatenar elementos
    //     });
    // });


    //para poder cambiar cada vez que se apriete el clik

    const textoOriginal = 'Emanuel Acosta'; // texto original 
    const textoAlternativo = 'Acosta Emanuel  <i class="fa-solid fa-user-tie"></i>'; // texto alternativo
    editarProfile.forEach(function (editButton) {
        editButton.addEventListener("click", function () {
            if (namePerfil.innerHTML === 'Emanuel Acosta') {
                namePerfil.innerHTML = textoAlternativo;
            }
            else {
                namePerfil.innerHTML = textoOriginal;
            }
        });
    });


    // de esta forma podemos cambiar seguidamente el texto varias veces
    cerrarSesion.addEventListener("click", function () {
        if (this.innerText === "Cerrar Sesión") {
            this.innerText = "Iniciar Sesión";
        }
        else {
            this.innerText = "Cerrar Sesión";
        }

    });


    // Event listener para botones de aceptar
    soliConnect.innerText = totalSoli;
    acceptButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const connectionItem = this.closest('.connection-item'); //obtener el elemento padre más cercano con la clase connection-item
            
            if (connectionItem) { //si existe el elemento
                connectionItem.remove(); //remover el elemento
                totalSoli--; //disminuir el total de solicitudes
                totalConex++; //aumentar el total de conexiones
                soliConnect.innerText = totalSoli; //actualizar el elemento de texto de total de solicitudes
                conex.innerText = totalConex; //actualizar el elemento de texto de total de conexiones
                console.log('Conexiones restantes:', totalSoli);
            }
        });
    });


    // Event listener para botones de negar
    negarButtons.forEach(function(button1) {
        button1.addEventListener('click', function() {
            const connectionItem = this.closest('.connection-item'); //obtener el elemento padre más cercano con la clase connection-item
            
            if (connectionItem) { //si existe el elemento
                connectionItem.remove(); //remover el elemento
                totalSoli--; //disminuir el total de solicitudes
                soliConnect.innerText = totalSoli; //actualizar el elemento de texto de total de solicitudes
            }
        });
    });


    // para mover las fotos con botones
    botonCambio.forEach(function(editButton) {
        editButton.addEventListener("click", function() {
                imgIzq.src = 'img/emanu.jpg';
        });
    });

    botonCambio2.forEach(function(editButton) {
        editButton.addEventListener("click", function() {
                imgDer.src = 'img/perfil1.jpg' 
        });
    });







    
});