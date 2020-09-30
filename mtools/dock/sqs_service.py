import boto3
import json

def enqueue(queue_name, payload):
    sqs = boto3.client('sqs')
    response = sqs.send_message(
        QueueUrl=queue_name,
        MessageAttributes=payload["attributes"],
        MessageBody=json.dumps(payload["body"])
    )
    return response
