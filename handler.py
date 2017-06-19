import json 
import stripe
from core.objects import (Remindr, PhoneNumber, Cron, 
                            S3Object, AWSLambda, Polly)

def schedule_remindr(event, context):
    print(event)
    stripe.api_key = "sk_test_k7hRhJ2DKta6DGw5ytbpIo7V"
    #token = request.POST['stripeToken']
    token = event['stripeToken']
    charge = stripe.Charge.create(
      amount=1000,
      currency="usd",
      description="Example charge",
      source=token,
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(event)
    }

    return response

#    remindr = Remindr(
#                PhoneNumber(
#                    event['phone']
#                ),
#                S3Object(
#                    Polly(
#                        event['message']
#                    )
#                ),
#                Cron(
#                    event['cron']
#                )
#            )

#    aws_lambda = AWSLambda()
#    aws_lambda.add_item(remindr)

#def process_remindr():
#    pass

#def hello(event, context):
#    body = {
#        "message": "Go Serverless v1.0! Your function executed successfully!",
#        "input": event
#    }

#    response = {
#        "statusCode": 200,
#        "body": json.dumps(body)
#    }

#    return response

#    # Use this code if you don't use the http event with the LAMBDA-PROXY integration
#    """
#    return {
#        "message": "Go Serverless v1.0! Your function executed successfully!",
#        "event": event
#    }
#    """
