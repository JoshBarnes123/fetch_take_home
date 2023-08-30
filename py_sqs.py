import boto3

print("hello, world")
# client = boto3.client('sqs', endpoint_url="http://localhost:4566/_aws/sqs/messages", region_name='us-east-2', aws_access_key_id='123', aws_secret_access_key='123')
# result = client.receive_message(QueueUrl="http://localhost:4566/000000000000/login-queue")

sqs_url = "http://localhost:4566/000000000000/login-queue"
result = boto3.client('sqs', region_name='us-east-2')
xx = result.list_queues()

# sqs = boto3.resource('sqs', region_name='us-east-2')
# queue = sqs.Queue(sqs_url)


# xx = queue.list_queues()
# print(queue)



# result = sqs.receive_message(QueueUrl="http://localhost:4566/000000000000/login-queue")
# print(result)
# response = client.receive_message(
#         QueueUrl='http://localhost:4566/000000000000/login-queue',
#         AttributeNames=[
#             'SentTimestamp'
#         ],
#         MaxNumberOfMessages=10,
#         MessageAttributeNames=[
#             'All'
#         ],
#         VisibilityTimeout=0,
#         WaitTimeSeconds=0
#     )

# awslocal sqs receive-message --queue-url http://localhost:4566/000000000000/login-queue