import boto3  # import Boto3
from boto3.dynamodb.conditions import Key  # import Boto3 conditions


def query_devices(device_id, dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="http://localhost:8000")
    # Specify the table to query
    devices_table = dynamodb.Table('Devices')
    response = devices_table.query(
        KeyConditionExpression=Key('device_id').eq(device_id)
    )
    return response['Items']


if __name__ == '__main__':
    query_id = "10001"
    print(f"Device Data from Device ID: {query_id}")
    devices_data = query_devices(query_id)
    # Print the items returned
    for device_data in devices_data:
        print(device_data['device_id'], ":", device_data['datacount'])
