import json
import urllib.parse
import uuid
import sys
import os
import stripe
from core.objects import S3Object, Polly

stripe.api_key = os.environ['STRIPE_KEY']
bucket_name = os.environ['AUDIO_BUCKET']

def charge(event, context):

    try:
        email, message, token, phone, cron = unpack_data(event)

        verify_phone(phone)

        url = create_recording(message)

        place_call(url, phone)  # schedule lambda with cron string

        stripe.Charge.create(
            amount=100,
            currency="usd",
            description="One reminder",
            source=token,
        )

        body = {
            "message": "Charging credit card",
            "token": token,
            "email": email,
            "phone": phone,
            "cron": cron,
            "recording_url": url
        }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }

        return response

    except:
        exception = sys.exc_info()[0]
        return {
            "statusCode": 500,
            "body": exception
        }

def call(event, context):
    pass



def unpack_data(event):
    encoded_form = urllib.parse.unquote(event['body'])
    decoded_form = urllib.parse.parse_qs(encoded_form)
    token = decoded_form["token"][0]
    email = decoded_form["email"][0]
    message = decoded_form["message"][0]
    phone = decoded_form["phone"][0]
    cron = decoded_form["cron"][0]

    return email, message, token, phone, cron


def create_recording(message):
    file_name = '{0}.mp3'.format(str(uuid.uuid4()))
    url = S3Object(
        bucket_name,
        Polly(message).recording(file_name),
        file_name
    ).url()

    print(url)

    return url