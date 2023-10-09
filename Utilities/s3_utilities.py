# Importing Dependencies #
import os
import boto3
from datetime import datetime

# Global Configurations #
BUCKET_NAME = os.environ.get('BUCKET_NAME')
S3_CLIENT = boto3.client('s3')


# Function to create a file name #
def generate_file_path():
    prefix = 'testing/'
    file_name = f"file_{datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S')}.json"
    return f"{prefix}{file_name}"


# Function to upload file to S3 #
def upload_file_to_s3(path, data):
    response = S3_CLIENT.put_object(Bucket=BUCKET_NAME, Key=path, Body=data)
    # Check if the upload was successful
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("File uploaded successfully!")
        return True
    else:
        print("Failed to upload file.")
        return False