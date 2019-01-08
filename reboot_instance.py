import sys
import boto3
from botocore.exceptions import ClientError

# # will need to specify instance-id when running, ex:
# # > python ./reboot_instances.py i-934857394857 
# # can support multiple instances separated by a space, ex:
# # > python ./reboot_instances.py i-934857394857 i-8675309sjs0

instance_id = sys.argv[1]

ec2 = boto3.client('ec2')

for instance_id in sys.argv[1:]:
	# Do a dryrun first to verify permissions
	try:
		ec2.reboot_instances(InstanceIds=[instance_id], DryRun=True)
	except ClientError as e:
		if 'DryRunOperation' not in str(e):
			print("You don't have permission to reboot instances.")
			raise
	
	# Dry run succeeded, run reboot_instances without dryrun
	try:
		response = ec2.reboot_instances(InstanceIds=[instance_id], DryRun=False)
		print('Success', response)
	except ClientError as e:
		print('Error', e)