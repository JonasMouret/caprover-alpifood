import stripe

stripe.Token.create(
  card={
    "number": "4242424242424242",
    "exp_month": 11,
    "exp_year": 2021,
    "cvc": "314",
  },
)