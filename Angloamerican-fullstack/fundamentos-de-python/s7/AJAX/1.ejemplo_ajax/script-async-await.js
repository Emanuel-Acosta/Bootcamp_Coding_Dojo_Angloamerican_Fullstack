// Función para obtener datos de GitHub
async function datosDeGithub(username) {
    try {
        const response = await fetch(`https://api.github.com/users/${username}`);
        const datos = await response.json();
        return datos;
    } catch (error) {
        console.error("Error:", error);
    }
}

// Función que muestra los datos en la página
async function mostrarUsuario() {
    // Obtenemos el valor del input 
    const username = document.getElementById('username').value;
    const resultadoDiv = document.getElementById('resultado');
    
    // Mostramos mensaje de carga
    resultadoDiv.innerHTML = 'Cargando...';
    
    // Obtenemos los datos de GitHub
    const datosUsuario = await datosDeGithub(username);
    console.log(datosUsuario); //Imprime json en consola
    // Mostramos los datos en el HTML 
    resultadoDiv.innerHTML = `
        <div style="padding: 20px; border: 1px solid #ccc; border-radius: 8px;">
            <img src="${datosUsuario.avatar_url}" style="width: 100px; border-radius: 50%;">
            <h2>${datosUsuario.name || datosUsuario.login}</h2>
            <p>${datosUsuario.bio || 'No bio available'}</p>
            <p>📍 ${datosUsuario.location || 'No location available'}</p>
            <p>👥 Followers: ${datosUsuario.followers}</p>
            <p>📚 Public repos: ${datosUsuario.public_repos}</p>
            <a href="${datosUsuario.html_url}" target="_blank">Ver perfil en GitHub</a>
        </div>
    `;
}