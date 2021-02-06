from botocore.exceptions import ClientError
from pprint import pprint
import boto3


def delete_device(device_id, datacount, info_timestamp, dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="http://localhost:8000")

    devices_table = dynamodb.Table('Devices')

    try:
        response1 = devices_table.delete_item(
            Key={
                'device_id': device_id,
                'datacount': datacount
            },
            # Conditional request
            ConditionExpression="info.info_timestamp <= :value",
            ExpressionAttributeValues={
                ":value": info_timestamp
            }
        )
    except ClientError as er:
        if er.response1['Error']['Code'] == "ConditionalCheckFailedException":
            print(er.response['Error']['Message'])
        else:
            raise
    else:
        return response1


if __name__ == '__main__':
    print("DynamoBD Conditional delete")
    # Provide device_id, datacount, info_timestamp
    delete_response = delete_device("10001", 1, 1714910791415)
    if delete_response:
        print("Item Deleted:")
        pprint(delete_response)
