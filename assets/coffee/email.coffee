# validate contact form
$("#contact-form").submit((e)->
  console.log "email attempt"
  e.preventDefault()
  return
).validate
  errorClass: "validate-error"
  rules:
    name:
      required: true
    subject:
      required: true
    email:
      required: true,
      email: true
    message:
      required: true
  messages:
    name: "This field is required."
    email: "Please enter a valid email."
    message: "This field is required."
  submitHandler: (form)->
    $.ajax
      url: emailUrl
      type: "POST"
      data: $(form).serialize()
      success: (response)->
        $("#contact-form").append response
    return
