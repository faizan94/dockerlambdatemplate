import boto3
import logging
import base64
import json


def get_secret(secret_name, region_name='eu-central-1'):
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        logging.info("Received Response")
    except KeyError:
        logging.error("Error in getting secret keys!")
    else:
        if 'SecretString' in get_secret_value_response:
            return get_secret_value_response['SecretString']
        else:
            return base64.b64decode(get_secret_value_response['SecretBinary'])


# custom function for bitcap / write your own if needed
def get_rds_connection_details(secret_name):
    db_secrets = get_secret(secret_name)
    db_details = json.loads(db_secrets)
    return {
        'user': db_details['USER'],
        'password': db_details['PASSWORD'],
        'host': db_details['HOST'],
        'db_name': db_details['DB_NAME']
    }
