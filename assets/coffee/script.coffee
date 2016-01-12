# donate section setup
webshim.setOptions 'forms-ext',
  replaceUI: 'auto'
  types: 'number',

webshim.polyfill 'forms forms-ext'


$("#btn-donate").click (e)->
  amount =  $("#donate-amount").val() * 100
  stripeHandler = StripeCheckout.configure(
    key: stripeKey
    token: (token)->
      $.ajax(
        type: "POST"
        url: donateURL
        data: { token: token.id, amount: amount, email: token.email }
        success: (response)->
          console.log response
          $("#donate-money-container").append response
          return
      )
  )
  stripeHandler.open(
    name: "CWRU Food Recovery Network"
    description: "Donation for CWRU Food Recovery Network via website"
    amount: amount
  )
  e.preventDefault()
  return

$(window).on 'popstate', ->
  stripeHandler.close()
  return
