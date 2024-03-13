# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html

### for javascript
# npm install @aws-sdk/client-s3


### for python
# python -m pip install boto3


import boto3
import sys
############# using default configuration
# s3 = boto3.resource('s3')                   ### credentials ---> by default ~/.aws/credentials  ([default] profile)
# for bucket in s3.buckets.all():
#     print(bucket.name)
############# using default configuration
    




#### using custom aws profile ############
session = boto3.Session(profile_name='ped_aws23')       ### you know what profile name to give
ped23 = session.client('s3')
response = ped23.list_buckets()
for bucket23 in response['Buckets']:
    print('bucket details ped aws account ===> ', bucket23['Name'])
#### using custom aws profile ############



################# using hardcoded stuff ###################
# client23 = boto3.client(
#     's3',
#     aws_access_key_id='DONT ever paste here... by mistake you may upload accessKey',
#     aws_secret_access_key='DONT ever paste here... by mistake you may upload accessKey'
# )       ########## if you want use above approaches
# response = client23.list_buckets()
# for bucket23 in response['Buckets']:
#     print('bucket details ===> ', bucket23['Name'])
################# using hardcoded stuff ###################

