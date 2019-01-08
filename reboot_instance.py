import sys
import boto3
from botocore.exceptions import ClientError

instance_id = sys.argv[1]

ec2 = boto3.client('ec2')

try:
    ec2.reboot_instances(InstanceIds=[instance_id], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot instances.")
        raise

try:
    response = ec2.reboot_instances(InstanceIds=[instance_id], DryRun=False)
    print('Success', response)
except ClientError as e:
    print('Error', e)