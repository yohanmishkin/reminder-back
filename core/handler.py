import json
import os
import stripe
import urllib.parse

stripe.api_key = os.environ['STRIPE_KEY']

def charge(event, context):

    encoded_form = urllib.parse.unquote(event['body'])
    decoded_form = urllib.parse.parse_qs(encoded_form)

    token = decoded_form["token"][0]
    email = decoded_form["email"][0]
    message = decoded_form["message"][0]
    phone = decoded_form["phone"][0]
    cron = decoded_form["cron"][0]

    bucket_name = os.environ['AUDIO_BUCKET']

    url = S3Object(
        bucket_name,
        Polly(message).recording()
    ).url()

    print(url)

    // schedule lambda with cron string
    //      to call number using polly mp3

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