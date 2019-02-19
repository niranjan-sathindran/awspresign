# awspresign
Ths repo holds a single file that outputs a presigned URL for a single object in an S3 bucket.
Code assumes environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` is already set prior to running. Access Key set must have full rights over object for which presigned URL needs to be created.
