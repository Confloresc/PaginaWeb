if (window.jQuery) {
  // jQuery está vinculado correctamente
  console.log("jQuery está vinculado correctamente en esta página.");
} else {
  // jQuery no está vinculado o no se ha cargado correctamente
  console.log(
    "jQuery no está vinculado o no se ha cargado correctamente en esta página."
  );
}

const form = document.querySelector(".needs-validation");

form.addEventListener("submit", function (event) {
  if (form.checkValidity() === false) {
    event.preventDefault();
    event.stopPropagation();
  }
  form.classList.add("was-validated");
});

const nombreInput = document.getElementById("nombre");
const apellidoInput = document.getElementById("apellido");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("pwd");

nombreInput.addEventListener("input", function () {
  const regex = /^[A-Za-z]+$/;
  if (!regex.test(nombreInput.value)) {
    nombreInput.setCustomValidity(
      "Por favor ingresar solo letras en el nombre"
    );
    nombreInput.reportValidity();
  } else {
    nombreInput.setCustomValidity("");
  }
});

apellidoInput.addEventListener("input", function () {
  const regex = /^[A-Za-z]+$/;
  if (!regex.test(apellidoInput.value)) {
    apellidoInput.setCustomValidity(
      "Por favor ingresar solo letras en el apellido"
    );
    apellidoInput.reportValidity();
  } else {
    apellidoInput.setCustomValidity("");
  }
});

emailInput.addEventListener("input", function () {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!regex.test(emailInput.value)) {
    emailInput.setCustomValidity(
      "Por favor ingresar un correo electrónico válido (ejemplo@dominio.com)"
    );
  } else {
    emailInput.setCustomValidity("");
  }
});

passwordInput.addEventListener("input", function () {
  const regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8}$/;
  if (!regex.test(password)) {
    passwordInput.setCustomValidity(
      "Contraseña debe tener 8 caracteres, mayuscula, minuscula y números."
    );
  } else {
    passwordInput.setCustomValidity("");
  }
});

checkInput.addEventListener("click", function () {
  if (checkInput.checked) {
    checkInput.setCustomValidity("");
  } else {
    checkInput.setCustomValidity("Haz click para continuar");
  }
});
