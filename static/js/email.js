// Generated by CoffeeScript 1.10.0
(function() {
  $("#contact-form").submit(function(e) {
    console.log("email attempt");
    e.preventDefault();
  }).validate({
    errorClass: "validate-error",
    rules: {
      name: {
        required: true
      },
      subject: {
        required: true
      },
      email: {
        required: true,
        email: true
      },
      message: {
        required: true
      }
    },
    messages: {
      name: "This field is required.",
      email: "Please enter a valid email.",
      message: "This field is required."
    },
    submitHandler: function(form) {
      $.ajax({
        url: emailUrl,
        type: "POST",
        data: $(form).serialize(),
        success: function(response) {
          return $("#contact-form").append(response);
        }
      });
    }
  });

}).call(this);

//# sourceMappingURL=email.js.map