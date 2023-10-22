$(document).ready(function () {
  $("#boton").on("click", function () {
    var buttonLoader = this.querySelector("#button-loader");
    var buttonText = this.querySelector("#button-text");

    // Muestra el efecto de carga
    buttonLoader.style.display = "inline-block";

    // Deshabilita el botón mientras se realiza la carga
    this.disabled = true;

    var titulo = $("#titulo").val();
    var categoria = $("#categoria").val();
    var medidas = $("#medidas").val();
    var monto = $("#monto").val();
    var archivo = document.getElementById("formFile").files[0];

    // Expresión regular para validar solo letras
    var letrasRegex = /^[a-zA-Z\s]+$/;

    // Expresión regular para validar solo números
    var numerosRegex = /^\d+$/;

    // Validación del campo de título
    if (!letrasRegex.test(titulo)) {
      var tituloInput = document.getElementById("titulo");
      tituloInput.setCustomValidity("El título debe contener solo letras.");
      tituloInput.reportValidity();

      // Restaura el estado del botón y detiene la carga
      buttonLoader.style.display = "none";
      this.disabled = false;
      return;
    } else {
      $("#titulo").get(0).setCustomValidity("");
    }

    // Validación del campo de categoría
    if (!letrasRegex.test(categoria)) {
      var categoriaInput = document.getElementById("categoria");
      categoriaInput.setCustomValidity(
        "La categoría debe contener solo letras."
      );
      categoriaInput.reportValidity();

      // Restaura el estado del botón y detiene la carga
      buttonLoader.style.display = "none";
      this.disabled = false;
      return;
    } else {
      $("#categoria").get(0).setCustomValidity("");
    }

    // Validación del campo de medidas (formato anchoxaltoxlargo)
    var medidasRegex = /^\d+x\d+x\d+$/;
    if (!medidasRegex.test(medidas)) {
      var medidasInput = document.getElementById("medidas");
      medidasInput.setCustomValidity(
        "Las medidas deben tener el formato ancho x alto x largo (por ejemplo, 10x20x30)."
      );
      medidasInput.reportValidity();

      // Restaura el estado del botón y detiene la carga
      buttonLoader.style.display = "none";
      this.disabled = false;
      return;
    } else {
      $("#medidas").get(0).setCustomValidity("");
    }

    // Validación del campo de monto
    if (!numerosRegex.test(monto)) {
      var montoInput = document.getElementById("monto");
      montoInput.setCustomValidity("El monto debe ser un número válido.");
      montoInput.reportValidity();

      // Restaura el estado del botón y detiene la carga
      buttonLoader.style.display = "none";
      this.disabled = false;
      return;
    } else {
      $("#monto").get(0).setCustomValidity("");
    }

    // Validación de la extensión del archivo
    var extensionesPermitidas = ["jpg", "jpeg", "png"];
    var archivoExtension = archivo.name.split(".").pop().toLowerCase();
    if (!extensionesPermitidas.includes(archivoExtension)) {
      var archivoInput = document.getElementById("formFile");
      archivoInput.setCustomValidity("Solo se permiten archivos PNG o JPG.");
      archivoInput.reportValidity();

      // Restaura el estado del botón y detiene la carga
      buttonLoader.style.display = "none";
      this.disabled = false;
      return;
    } else {
      $("#formFile").get(0).setCustomValidity("");
    }

    setTimeout(function () {
      buttonLoader.style.display = "none";

      // Habilita el botón nuevamente
      $("#boton").prop("disabled", false);
      $("#archivoCargadoModal").modal("show");
    }, 1000);
  });
});
