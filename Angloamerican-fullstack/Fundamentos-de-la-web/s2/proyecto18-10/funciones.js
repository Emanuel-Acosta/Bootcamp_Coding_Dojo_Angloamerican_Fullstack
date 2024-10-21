//function saludar(nombreAmigo) {
//    console.log("¡Hola, amigo", nombreAmigo, "!");
//}

//saludar("Luis");

//Acá tenemos la función con las instrucciones
//function encontrarMaximo(a, b) {
//    if (a > b) {
//        return a;
//    } else {
//        return b;
//    }
//}

//Valor de los dos números a comparar
//var numero1 = 10;
//var numero2 = 7;

//Llamamos a la función y le pasamos los números
//var maximo recibe el número mayor
//var maximo = encontrarMaximo(numero1, numero2);

//Vemos por consola los números
//console.log("El máximo entre", numero1, "y", numero2, "es:", maximo);

// function siempreAburrido(arreglo) {
//     for (let i = 0; i < arreglo.length; i++) {
//         if (arreglo[i] === "ver TV") {
//             console.log("¡Entretenido!");
//         }    
//         else {
//             console.log("¡Estoy Aburrido!");
//         }
//     }

// }

// siempreAburrido(["cantar", "correr", "salir", "ver TV"]);

// function numeroDeCorte(arreglo, valorCorte) {
//     let resultado = [];
//     for (let i = 0; i < arreglo.length; i++) {
//         if (arreglo[i] < valorCorte) {
//             resultado.push(arreglo[i]);
//         }
//     }
//     return resultado;
// }

// console.log(numeroDeCorte([1, 2, 8, 4, 5, 7, 6], 4)); // Salida: [1, 2]

// function numerosbajoPromedio(arreglo){
//     let total = 0;
//     for(i=0; i < arreglo.length;i++){
//         total += arreglo[i];
//     }

//     const promedio= total / arreglo.length;
//     numerobajoPromedio =[];
//     for(i=0;i<arreglo.length;i++){
//         if(arreglo[i]<promedio){
//             numerobajoPromedio.push(arreglo[i]);
//         }
//     }
//     console.log(numerobajoPromedio);
// }

// numerosbajoPromedio([2,3,20,15,16,60,500]);

// function conteoPares(arreglo){
//     let contador= 0;
//     for(let i=0;i<arreglo.length;i++){
//         if(arreglo[i]%2===0){
//             contador ++;
//         }
//     }
//     return contador;
// }

// console.log(conteoPares([2,5,6,7,6,5,21]));

function arregloDeFibonacci(n) {
    const fibonacci = [0, 1];
    for (let i = 2; i < n; i++) {
        fibonacci.push(fibonacci[i - 1] + fibonacci[i - 2]);
    }
    return fibonacci;
}

// Ejemplo de uso
console.log(arregloDeFibonacci(6));
