import boto3

# Create an S3 client
client = boto3.client('s3')
response = client.list_buckets()

# Print bucket names
for bucket in response['Buckets']:
    print(bucket['Name'])
