const container4 = document.querySelector('.container4');
const register = document.querySelector('.register');
const login = document.querySelector('.login');

register.addEventListener('click', () => {
    container4.classList.add('active');
})

login.addEventListener('click', () => {
    container4.classList.remove('active');
})