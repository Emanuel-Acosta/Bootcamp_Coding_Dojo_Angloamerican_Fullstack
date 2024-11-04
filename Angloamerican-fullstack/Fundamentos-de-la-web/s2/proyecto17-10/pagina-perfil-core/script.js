var borrar = document.querySelectorAll(".borrarBotton");
borrar.forEach(function(borrarbotton) {
    borrarbotton.addEventListener("click", function() {
        
        this.remove();
    });
});
