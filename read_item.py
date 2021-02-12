# import Boto3 exceptions and error handling module
from botocore.exceptions import ClientError
import boto3  # import Boto3


def get_device(device_id, datacount, dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="http://localhost:8000")
    # Specify the table to read from
    devices_table = dynamodb.Table('Devices')

    try:
        response = devices_table.get_item(
            Key={'device_id': device_id, 'datacount': datacount})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    device = get_device("10001", 3,)
    if device:
        print("Get Device Data Done:")
        # Print the data read
        print(device)
