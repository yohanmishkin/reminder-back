from core.objects import (Remindr, PhoneNumber, Cron, 
                            AzureStorageObject, AzureFunctions, Polly)

class Handler(object):
    
    def run(self, event):
        
        remindr = Remindr(
                    PhoneNumber(
                        event['phone']
                    ),
                    AzureStorageObject(
                        Polly(
                            event['message']
                        )
                    ),
                    AzureFunctions(),
                    Cron(
                        event['cron']
                    )
                )

        remindr.save()
