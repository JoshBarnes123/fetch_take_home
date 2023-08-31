import boto3
import json
import pandas as pd
boto3.compat.filter_python_deprecation_warnings()

ENDPOINT_URL = "http://localhost:4566/_aws/sqs/messages"
AWS_S3_CREDS = {
    "aws_access_key_id":"foobar",
    "aws_secret_access_key":"foobar"
}

client = boto3.client("sqs", endpoint_url=ENDPOINT_URL, **AWS_S3_CREDS, region_name="us-east-1")
result = client.receive_message(QueueUrl="http://localhost:4566/000000000000/login-queue")
#--
# result_json = json.dumps(result, indent=4)
# response_subset = result["Messages"][0]["Body"]

# desired_data = json.loads(response_subset)
# desired_data_subset = desired_data["user_id"]
# print(desired_data)
# print(desired_data_subset)
#--
result_json = json.dumps(result, indent=4)
response_subset = result["Messages"][0]["Body"]
desired_data = json.loads(response_subset)

record =  pd.DataFrame(columns=["user_id", "device_type", "masked_ip", "masked_device_id", "locale", "app_version", "create_date"]).fillna(2)

record =  pd.DataFrame()
record["user_id"] = "NAN"
