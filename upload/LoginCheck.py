import boto3
from boto3.dynamodb.conditions import Key, Attr
import DBAccessKey
import hashlib

access_key_id_global=DBAccessKey.DBAccessKey.access_key_id_global
secret_access_key_global=DBAccessKey.DBAccessKey.secret_access_key_global

class LoginCheck:
	def __init__(self, uname, pswd):
		self.uname = uname
		self.pswd = pswd

	def check_login(self):
		dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-2', aws_access_key_id=access_key_id_global,
								  aws_secret_access_key=secret_access_key_global)
		table = dynamodb.Table('security')

		#print("The uname is:",self.uname,"<--" )
		salted_pswd = '$"' + self.pswd+ '$"'
		hash_password = hashlib.md5(salted_pswd.encode())
		#print("Testing pw", hash_password.hexdigest())

		response = table.query(
			KeyConditionExpression=Key('Username').eq(self.uname)
		)
		if (response['Items']):
			for i in response['Items']:
				#print(i['Username'], ":", i['Password'])
				if(i['Password']==hash_password.hexdigest()):
					return True

			#return True
		else:
			#print(response['Items'])
			print("Denied")
			return False




