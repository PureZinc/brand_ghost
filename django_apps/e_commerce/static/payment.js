var stripe = Stripe('{{ public_key }}');
var elements = stripe.elements();

var card = elements.create('card');

card.mount('#card-element');

card.addEventListener('change', function (event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
});

// Handling errors for the frontend
var form = document.getElementById('payment-form');
form.addEventListener('submit', function (event) {
  event.preventDefault();

  stripe.createToken(card).then(function (result) {
    if (result.error) {
      var errorElement = document.getElementById('card-errors');
      errorElement.textContent = result.error.message;
    } else {
      var token = result.token;
      var hiddenInput = document.createElement('input');
      hiddenInput.setAttribute('type', 'hidden');
      hiddenInput.setAttribute('name', 'stripeToken');
      hiddenInput.setAttribute('value', token.id);
      form.appendChild(hiddenInput);
      form.submit();
    }
  });
});