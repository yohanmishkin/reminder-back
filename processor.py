import boto3
from flask import Flask, request, redirect
import stripe

# ENCRYPTED_STRIPE_KEY = os.environ['ENCRYPTED_STRIPE_KEY']
# # Decrypt code should run once and variables stored outside of the function
# # handler so that these are decrypted once per container
# DECRYPTED = boto.client('kms') decrypt(CiphertextBlob=b64decode(ENCRYPTED_STRIPE_KEY))['Plaintext']
# stripe.api_key = DECRYPTED

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handler(event, context):
    try:
        print(context)
        print(request.form.get('event'))

        customer = stripe.Customer.create(
            email=request.form.get('stripeEmail'),
            source=request.form.get('stripeToken')
        )

        stripe.Subscription.create(
            customer=customer.id,
            plan="base-plan"
        )

        # return redirect("https://www.your-site/success-message")
        response = {
            "statusCode": 200,
            "body": json.dumps(event)
        }

        return response

    except Exception as e:
        # Don't forget to log your errors before doing this!
        return redirect("https://www.your-site/error-message")

if __name__ == "__main__":
    app.run()
