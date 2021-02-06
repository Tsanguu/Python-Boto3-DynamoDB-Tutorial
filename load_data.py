import json
from decimal import Decimal
import boto3


def load_data(devices, dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="http://localhost:8000")

    devices_table = dynamodb.Table('Devices')
    for device in devices:
        device_id = (device['device_id'])
        datacount = device['datacount']
        print("Loading Devices Data:", device_id, datacount)
        devices_table.put_item(Item=device)


if __name__ == '__main__':
    with open("data.json") as json_file:
        device_list = json.load(json_file, parse_float=Decimal)
    load_data(device_list)
