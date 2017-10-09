import urllib.parse

from core.usecase import Usecase


def charge(event, context):
    try:
        email, message, token, phone_number, cron = unpack_data(event)

        use_case = Usecase(message, phone_number, token)
        # S3Object(
        #     Polly(self._storage_object).recording(
        #         '{0}.mp3'.format(str(uuid.uuid4()))
        #     )
        # ).url()
        use_case.run()

        response = {
            "statusCode": 200,
            "body": "Scheduled call and charged card"
        }

        return response

    except Exception as exception:
        return {
            "statusCode": 500,
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
