function toggleForm() {
    const loginBox = document.querySelector('.login-box');
    const registerBox = document.querySelector('.register-box');
    
    if (loginBox.style.display === 'none') {
        loginBox.style.display = 'block';
        registerBox.style.display = 'none';
    } else {
        loginBox.style.display = 'none';
        registerBox.style.display = 'block';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.login-box').style.display = 'block';
});

function login() {
    const user = document.getElementById('login-user').value;
    const pass = document.getElementById('login-pass').value;
    alert(`Bienvenido, ${user}!`);
}

function register() {
    const user = document.getElementById('register-user').value;
    const pass = document.getElementById('register-pass').value;
    alert(`Usuario ${user} registrado con éxito!`);
}