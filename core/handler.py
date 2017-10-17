import os
import urllib.parse
import uuid

from core import S3Object, Polly, TwilioPhone, TwimlFile, StripePayment, Usecase


def charge(event, context):
    try:
        email, message, token, phone_number, cron = unpack_data(event)

        bucket_name = os.environ['S3_BUCKET']
        folder_name = str(uuid.uuid4())

        Usecase(
            S3Object(
                bucket_name,
                folder_name,
                TwimlFile(
                    S3Object(
                        bucket_name,
                        folder_name,
                        Polly(message).recording(
                            'voice.mp3'
                        )
                    ).url()
                ).write()
            ),
            TwilioPhone(
                phone_number,
                os.environ['TWILIO_FROM'],
                os.environ['TWILIO_ACCOUNT_SID'],
                os.environ['TWILIO_AUTH_TOKEN']
            ),
            StripePayment(
                os.environ['STRIPE_KEY'],
                token
            )
        ).run()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": "Scheduled call and charged card"
        }

    except Exception as exception:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": exception
        }


def unpack_data(event):
    encoded_form = urllib.parse.unquote(event['body'])
    decoded_form = urllib.parse.parse_qs(encoded_form)
    token = decoded_form["token"][0]
    email = decoded_form["email"][0]
    message = decoded_form["message"][0]
    phone = decoded_form["phone"][0]
    cron = decoded_form["cron"][0]

    return email, message, token, phone, cron
