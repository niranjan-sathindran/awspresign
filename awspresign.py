import boto3

# Modify values below to bucket name and object name
bucket="<sample-bucket>"
key="<object-name-from-bucket>"
expiration=1000 * 60 * 60 * 72 #Modify 72 here to enter number of hours
params = {
    'Bucket': bucket,
    'Key': key
}
s3 = boto3.client('s3')
url = s3.generate_presigned_url('get_object', Params=params, ExpiresIn=expiration)
print('url:' + url)