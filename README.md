# awspresign
Ths repo holds a single file that outputs a presigned URL for a single object in an S3 bucket.
Code assumes environment variables `aws_access_key_id` and `aws_secret_access_key` is already set prior to running. Access Key set must have full rights over object for which presigned URL needs to be created.
