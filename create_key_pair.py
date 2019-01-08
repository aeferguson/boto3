import sys
import boto3
from botocore.exceptions import ClientError

key_pair_name = sys.argv[1]

ec2 = boto3.client('ec2')

try:
	ec2.create_key_pair(KeyName=key_pair_name, DryRun=True)
except ClientError as e:
	if 'DryRunOperation' not in str(e):
		print("You don't have permission to create a Key Pair.")
		raise

# Dry run succeeded, create a Key Pair without dryrun
try:
	response = ec2.create_key_pair(KeyName=key_pair_name, DryRun=False)
	print('Success', response)
except ClientError as e:
	print('Error', e)
