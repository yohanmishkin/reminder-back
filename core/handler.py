from core.objects import (Remindr, PhoneNumber, Cron, 
                            S3Object, AWSLambda, Polly)

class Handler(object):
    
    def run(self, event):
        
        remindr = Remindr(
                    PhoneNumber(
                        event['phone']
                    ),
                    S3Object(
                        Polly(
                            event['message']
                        )
                    ),
                    Cron(
                        event['cron']
                    )
                )

        aws_lambda = AWSLambda()
        aws_lambda.add_item(remindr)
