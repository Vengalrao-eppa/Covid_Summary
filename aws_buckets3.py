import boto3

# get a handle on s3
session = boto3.Session(
                    aws_access_key_id='XX',
                    aws_secret_access_key='XX',
                    region_name='XX')
                    
s3 = session.resource('s3')

bucket = s3.Bucket('bucket name') # example: AWS Bucket S3

obj = bucket.Object(key='file to read') # example: covid19/zone1/data.csv

response = obj.get()

lines = response['Body'].read()

with open('data.csv', 'wb') as file:
    file.write(lines)   