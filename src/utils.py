import yaml
import boto3
import base64
import json


def load_yaml(settings_file):
    with open(settings_file) as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def get_secret(secret_name, region_name='eu-central-1'):
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        print("Succes | Received Response")
    except KeyError:
        print("Error | Unable to secret keys!")
    else:
        if 'SecretString' in get_secret_value_response:
            return json.loads(get_secret_value_response['SecretString'])
        else:
            return json.loads(base64.b64decode(get_secret_value_response['SecretBinary']))
