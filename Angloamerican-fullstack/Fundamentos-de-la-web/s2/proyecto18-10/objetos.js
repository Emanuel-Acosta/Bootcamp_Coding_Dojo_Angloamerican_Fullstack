// var sandwich ={
//     pan: [2,3],
//     queso: 1,
//     hamburguesa:2,
//     salsas:["mayo", "ketchup", "mostaza"],
//     comer: function(){
//         console.log("que rico oeeee")
//     }
// }

// console.log(sandwich.pan);

// sandwich.pan[0]= 5;
// console.log(sandwich.pan);
// sandwich.comer()


// var hamburguesaClasica = {
//     "pan": "pan con semillas de sésamo",
//     "carne": "carne de res 100%",
//     "queso": "queso cheddar",
//     "extras": ["lechuga", "tomate", "cebolla", "salsa especial"],
//     "infoHamburguesa": function() {
//         console.log("Pan: " + hamburguesaClasica.pan);
//         console.log("Carne: " + this.carne);
//         console.log("Queso: " + this.queso);
//         console.log("Extras: " + this.extras.join(", "));
//     }
// }

// Ahora, con solo una línea, ¡podemos obtener todos los detalles de nuestra hamburguesa clásica!
// hamburguesaClasica.infoHamburguesa();

// var sandwich = {
//     pan: "masa madre",
//     proteína: "asado",
//     queso: "queso suizo lacey",
//     salsas: ["lechuga romana", "tomates reliquia", "salsa de rábano"]
// };

// console.log(sandwich);

// function sandwichFactory(pan,proteína,queso,salsas){
//     let sandwich={};
//     sandwich.pan= pan;
//     sandwich.proteína=proteína;
//     sandwich.queso=queso;
//     sandwich.salsas=salsas;
//     return sandwich;
// }

// let sandwich1= sandwichFactory("trigo","pavo","provolone",["mostaza","cebolla frita","rúcula"])
// console.log(sandwich1);

// let sandwich1= sandwichFactory("trigo","pavo","provolone",["mostaza","cebolla frita","rúcula"])


// function pizzaOven(corteza,salsa,quesos,salsas){
//     let pizza={};
//     pizza.corteza= corteza;
//     pizza.salsa=salsa;
//     pizza.quesos=quesos;
//     pizza.salsas=salsas;
    
//     return pizza;
// }

// let pizzaChicago= pizzaOven("estilo chicago","tradicional","mozzarella",["pepperoni","salchicha"]);
// console.log(pizzaChicago);

function pizzaOven(tipoCorteza,tipoSalsa,quesos,salsas){
    let pizza={
        corteza: tipoCorteza,
        salsa: tipoSalsa,
        queso:quesos,
        salsaAdicional:salsas
        
    }
    
    return pizza 
    
}

let pizzaChicago= pizzaOven("estilo chicago","tradicional","mozzarella",["pepperoni","salchicha"]);
console.log(pizzaChicago);

let pizzaCoro= pizzaOven("masa madre", "tomate albahaca", ["queso de mano", "telita"],["bbq","anchoas"] );
console.log(pizzaCoro);

