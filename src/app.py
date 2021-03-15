import json
from src.utils import get_secret, load_yaml


def lambda_handler(event, context):
    yaml = load_yaml('src/config.yml')
    print(get_secret(yaml['secret_name']))

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "status": 'processed',
            }
        ),
    }
