const registerButton = document.querySelector("a[href*='registrarse']"),
      loginButton = document.querySelector("a[href*='login']"),
      formsContainer = document.querySelector("main");

registerButton.addEventListener("click", (event) => {
  event.preventDefault();
  formsContainer.classList.remove("bounceRight");
  formsContainer.classList.add("bounceLeft");
});

loginButton.addEventListener("click", (event) => {
  event.preventDefault();
  formsContainer.classList.remove("bounceLeft");
  formsContainer.classList.add("bounceRight");
});
