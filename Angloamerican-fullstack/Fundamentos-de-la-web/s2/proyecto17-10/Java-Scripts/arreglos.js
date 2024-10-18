let compras_semanales = [10000, 2000, 3000, 4000, 5000, 60000, 700];
let dias_semana = compras_semanales.length;


total_compras = 0;

for(let i = 0; i < dias_semana; i ++){
    console.log("dia",i,"gaste:", compras_semanales[i]);
    total_compras += compras_semanales[i];
}

console.log("El total de compras de la semana es:", total_compras);