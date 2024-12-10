// Función para obtener datos de GitHub
function datosDeGithub(username) {
    return fetch(`https://api.github.com/users/${username}`)
        .then(response => response.json())
        .catch(error => {
            console.error("Error:", error);
            throw error;
        });
}

// Función que muestra los datos en la página
function mostrarUsuario() {
    // Obtenemos el valor del input desde el DOM y el div donde mostraremos los datos
    const username = document.getElementById('username').value;
    const resultadoDiv = document.getElementById('resultado');
    
    // Mostramos mensaje de carga mientras se obtienen los datos
    resultadoDiv.innerHTML = 'Cargando...';
    
    // Obtenemos los datos de GitHub
    datosDeGithub(username)
        .then(datosUsuario => {
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
        })
        .catch(error => {
            resultadoDiv.innerHTML = 'Error al cargar los datos.';
        });
}