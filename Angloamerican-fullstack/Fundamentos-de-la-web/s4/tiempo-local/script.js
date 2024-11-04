document.addEventListener("DOMContentLoaded", function () {

    //aceptar cookies
    let aceptar = document.querySelectorAll("#acepto");
    let footerBorrar = document.getElementById("footer1");

    let mainContent = document.getElementById("mains");
    let h1Content = document.querySelector(".pais");

    //boton de buenos aires
    let buenosAires = document.querySelectorAll("#buenosAires");
    //boton de santiago
    let santiago = document.querySelectorAll("#santiago");

    let hoyImg = document.getElementById("hoyImg");
    let hoyText = document.getElementById("hoyText");
    let hoyTemperatura = document.getElementById("hoyTemperatura");

    let mañanaImg = document.getElementById("mañanaImg");
    let mañanaText = document.getElementById("mañanaText");
    let mañanaTemperatura = document.getElementById("mañanaTemperatura");

    let miercolesImg = document.getElementById("miercolesImg");
    let miercolesText = document.getElementById("miercolesText");
    let miercolesTemperatura = document.getElementById("miercolesTemperatura");

    let juevesImg = document.getElementById("juevesImg");
    let juevesText = document.getElementById("juevesText");
    let juevesTemperatura = document.getElementById("juevesTemperatura");

    let viernesImg = document.getElementById("viernesImg");
    let viernesText = document.getElementById("viernesText");
    let viernesTemperatura = document.getElementById("viernesTemperatura");
    // cambiar el texto del h1 pais
    let cambioPais = document.getElementById("cambioPais");


    //aceptar cookies
    aceptar.forEach(function (button) {
        button.addEventListener('click', function () {
            footerBorrar.remove(); //remover el elemento
        });
    });

    //alerta y borra footer, main y h1
    window.addEventListener("load", function () {

        mainContent.style.display = "none";
        h1Content.style.display = "none";

        // Utiliza setTimeout para dar un pequeño retraso antes de mostrar la alerta
        setTimeout(function () {
            alert("Cargando reporte del clima");
        }, 100); // Retraso de 100 ms
    });


    // para mostrar buenos aires
    buenosAires.forEach(function (editButton) {
        editButton.addEventListener("click", function () {
            
            mainContent.style.display = "flex";
            h1Content.style.display = "flex";
            cambioPais.innerText = "Buenos Aires";

            hoyImg.src = 'img/nublado.jpg';
            hoyText.innerText = "Nublado";
            hoyTemperatura.innerText = "22°C° 15°C°";
            //
            mañanaImg.src = "img/Lluvioso.png";
            mañanaText.innerText = "Lluvioso";
            mañanaTemperatura.innerText ="20°C° 13°C°";
            //
            miercolesImg.src ="img/tormenta.png";
            miercolesText.innerText = "Tormenta";
            miercolesTemperatura.innerText ="18°C° 11°C°";
            //
            juevesImg.src ="img/parcialmente.png";
            juevesText.innerText = "Parcialmente nublado";
            juevesTemperatura.innerText ="21°C° 14°C°";
            //
            viernesImg.src ="img/soleado.jpg";
            viernesText.innerText = "Soleado";
            viernesTemperatura.innerText ="24°C° 17°C°";
            
        });
    });

    //para mostrar santiago
    santiago.forEach(function (edit) {
        edit.addEventListener("click", function () {
            mainContent.style.display = "flex";
            h1Content.style.display = "flex";
            cambioPais.innerText = "Santiago de Chile";
            
            hoyImg.src = "img/lluvioso.png";
            hoyText.innerText = "Lluvioso";
            hoyTemperatura.innerText = "20°C° 13°C°";
            //
            mañanaImg.src = "img/nublado.jpg";
            mañanaText.innerText = "Nublado";
            mañanaTemperatura.innerText = "22°C° 15°C°";
            //
            miercolesImg.src ="img/soleado.jpg";
            miercolesText.innerText = "Soleado";
            miercolesTemperatura.innerText ="24°C° 17°C°";
            //
            juevesImg.src ="img/tormenta.png";
            juevesText.innerText = "Tormenta";
            juevesTemperatura.innerText ="18°C° 11°C°";
            //
            viernesImg.src ="img/parcialmente.png";
            viernesText.innerText = "Parcialmente nublado";
            viernesTemperatura.innerText ="21°C° 14°C°";


        });
    });















});    