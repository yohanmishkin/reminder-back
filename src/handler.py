import json
import urllib.parse
import stripe

stripe.api_key = os.environ['STRIPE_KEY']

def charge(event, context):

    body = event['body']
    encoded_form = urllib.parse.unquote(body)
    decoded_form = urllib.parse.parse_qs(encoded_form)

    token = decoded_form["token"][0]
    email = decoded_form["email"][0]

    charge = stripe.Charge.create(
        amount=100,
        currency="usd",
        description="One reminder",
        source=token,
    )

    body = {
        "message": "Charging credit card",
        "token": token,
        "email": email
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response