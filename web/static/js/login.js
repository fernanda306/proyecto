document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".form-box");
    const usernameInput = form.querySelector("input[name='username']");
    const passwordInput = form.querySelector("input[name='password']");

    if (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault(); // Evita el envío del formulario para mostrar el mensaje
            if (!usernameInput.value.trim() || !passwordInput.value.trim()) {
                mostrarMensaje("Por favor, complete todos los campos.", "error");
                return;
            }
            showMessage('Has iniciado sesión satisfactoriamente');
        });
    }

    // Función para mostrar mensajes personalizados
    function mostrarMensaje(mensaje, tipo) {
        const mensajeDiv = document.createElement("div");
        mensajeDiv.textContent = mensaje;
        mensajeDiv.classList.add("mensaje", tipo, "fade-in");

        // Estilos para centrar y estilizar el mensaje
        mensajeDiv.style.position = "fixed";
        mensajeDiv.style.top = "50%";
        mensajeDiv.style.left = "50%";
        mensajeDiv.style.transform = "translate(-50%, -50%)";
        mensajeDiv.style.padding = "20px";
        mensajeDiv.style.border = "1px solid #ccc";
        mensajeDiv.style.borderRadius = "30px";
        mensajeDiv.style.backgroundColor = "rgb(55, 55, 87)";
        mensajeDiv.style.zIndex = "1000"; // Asegura que esté encima de otros elementos
        mensajeDiv.style.height = "40%";
        document.body.appendChild(mensajeDiv);

        setTimeout(function () {
            mensajeDiv.classList.remove("fade-in");
            mensajeDiv.classList.add("fade-out");
            setTimeout(function () {
                document.body.removeChild(mensajeDiv);
            }, 1000); // Tiempo para la animación de desaparición
        }, 3000); // Elimina el mensaje después de 3 segundos
    }

    function showMessage(message) {
        const messageDiv = document.createElement('div');
        messageDiv.textContent = message;
        messageDiv.classList.add("mensaje", "fade-in");

        // Estilos para centrar y estilizar el mensaje
        messageDiv.style.position = 'fixed';
        messageDiv.style.top = '50%';
        messageDiv.style.left = '50%';
        messageDiv.style.transform = 'translate(-50%, -50%)';
        messageDiv.style.backgroundColor = '#4CAF50';
        messageDiv.style.color = 'white';
        messageDiv.style.padding = '20px';
        messageDiv.style.borderRadius = '5px';
        messageDiv.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.1)';
        document.body.appendChild(messageDiv);

        setTimeout(function() {
            messageDiv.classList.remove("fade-in");
            messageDiv.classList.add("fade-out");
            setTimeout(function() {
                messageDiv.remove();
                form.submit(); // Envía el formulario después de mostrar el mensaje
            }, 1000); // Tiempo para la animación de desaparición
        }, 2000); // El mensaje se mostrará durante 2 segundos
    }
});