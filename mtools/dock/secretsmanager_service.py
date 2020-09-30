import ast
import boto3
import jwt

from botocore.exceptions import ClientError

DEFAULTS = {
        'verify_signature': False,
        'verify_aud': False,
        'verify_iat': False,
        'verify_exp': False,
        'verify_nbf': False,
        'verify_iss': False,
        'verify_sub': False,
        'verify_jti': False,
        'verify_at_hash': False,
        'leeway': 0}

class SecretsManagerService(object):
    def __init__(self, region:str):
        super().__init__()
        self.region = region

    def get_app_client(self, authorization):
        return jwt.decode(authorization, algorithms=['RS256'], options=DEFAULTS)['client_id']

    def get_secrets(self, secret):
        try:
            session = boto3.session.Session()
            client = session.client(service_name='secretsmanager', region_name=self.region)
            response = client.get_secret_value(SecretId=secret)
            return ast.literal_eval(response['SecretString'])
        except ClientError as e:
            raise e