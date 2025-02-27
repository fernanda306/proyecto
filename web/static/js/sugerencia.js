document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Evita el envío inmediato

        const username = document.querySelector("input[name='username']").value.trim();
        const email = document.querySelector("input[name='email']").value.trim();
        const message = document.querySelector("input[name='section_text']").value.trim();

        if (!username || !email || !message) {
            mostrarMensaje("Por favor, complete todos los campos antes de enviar.", "error");
            return;
        }

        if (!validateEmail(email)) {
            mostrarMensaje("Por favor, ingrese un correo electrónico válido.", "error");
            return;
        }

        mostrarMensaje("¿Estás seguro de que deseas enviar tu sugerencia?", "confirmacion", function () {
            form.submit(); // Envía el formulario si todo está correcto
        });
    });
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function mostrarMensaje(mensaje, tipo, callback) {
    const mensajeDiv = document.createElement("div");
    mensajeDiv.textContent = mensaje;
    mensajeDiv.classList.add("mensaje");
    mensajeDiv.classList.add(tipo);

    // Estilos para centrar y estilizar el mensaje
    mensajeDiv.style.position = "fixed";
    mensajeDiv.style.top = "50%";
    mensajeDiv.style.left = "50%";
    mensajeDiv.style.transform = "translate(-50%, -50%)";
    mensajeDiv.style.padding = "20px";
    mensajeDiv.style.border = "1px solid white";
    mensajeDiv.style.borderRadius = "2%";
    mensajeDiv.style.backgroundColor = "rgb(55, 55, 87)";
    mensajeDiv.style.zIndex = "1000"; 
    mensajeDiv.style.height = "30%"; 
    mensajeDiv.style.textAlign = "center"; // Asegura que esté encima de otros elementos// Asegura que esté encima de otros elementos// Asegura que esté encima de otros elementos

    document.body.appendChild(mensajeDiv);

    if (tipo === "confirmacion") {
        const confirmarBtn = document.createElement("button");
        confirmarBtn.textContent = "Sí";
        confirmarBtn.addEventListener("click", function () {
            document.body.removeChild(mensajeDiv);
            if (callback) callback();
        });

        const cancelarBtn = document.createElement("button");
        cancelarBtn.textContent = "No";
        cancelarBtn.addEventListener("click", function () {
            document.body.removeChild(mensajeDiv);
        });

        mensajeDiv.appendChild(confirmarBtn);
        mensajeDiv.appendChild(cancelarBtn);
    } else {
        setTimeout(function () {
            document.body.removeChild(mensajeDiv);
        }, 3000); // Elimina el mensaje después de 3 segundos
    }
}