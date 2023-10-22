$(document).ready(function () {
  $(".validarEmail").on("change", function () {
    var email = document.getElementsByClassName("validarEmail")[0].value;
    var resultApi = document.getElementById("resultApi");
    var result = "";
    var color;

    resultApi.innerHTML = "";

    // send API request
    $.ajax({
      url: "https://api.email-validator.net/api/verify",
      type: "POST",
      cache: false,
      crossDomain: true,
      data: {
        EmailAddress: email.value,
        APIKey: "ev-4e2870c214ee30462cd50453659c8647",
      },
      dataType: "json",
      success: function (json) {
        // check API result
        if (typeof json.status != "undefined") {
          var resultcode = json.status;

          if (resultcode == 200 || resultcode == 207 || resultcode == 215) {
            result = "Correo OK";
            color = "#58D68D";
          } else {
            if (resultcode == 215) {
              result = "Intentar nuevamente";
              color = "#D4AC0D";
            } else {
              if (resultcode == 114 || resultcode == 118) {
                result = "Intentar en 5 min";
                color = "#D4AC0D";
              } else {
                if (resultcode == 118) {
                  result = "Intentar nuevamente";
                  color = "#D4AC0D";
                } else {
                  if (resultcode >= 300) {
                    result = "mail erroneo";
                    color = "#E74C3C";
                  } else {
                    result = "";
                  }
                }
              }
            }
          }
          resultApi.style.color = color;
          resultApi.innerHTML = result;

          if (typeof json.info != "undefined") {
            // short summary
            info = json.info;
          } else info = "";
          if (typeof json.details != "undefined") {
            // detailed description
            details = json.details;
          } else details = "";
          // resultcode 200, 207, 215 - valid
          // resultcode 215 - can be retried to update catch-all status
          // resultcode 114 - greylisting, wait 5min and retry
          // resultcode 118 - api rate limit, wait 5min and retry
          // resultcode 3xx/4xx - bad
        }
      },
    });
  });
});
