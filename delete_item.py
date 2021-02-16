# import Boto3 exceptions and error handling module
from botocore.exceptions import ClientError
from pprint import pprint  # import pprint, a module that enable to “pretty-print”
import boto3  # import Boto3


def delete_device(device_id, datacount, info_timestamp, dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="http://localhost:8000")
    # Specify the table to delete from
    devices_table = dynamodb.Table('Devices')

    try:
        response = devices_table.delete_item(
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
        if er.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(er.response['Error']['Message'])
        else:
            raise
    else:
        return response


if __name__ == '__main__':
    print("DynamoBD Conditional delete")
    # Provide device_id, datacount, info_timestamp
    delete_response = delete_device("10001", 3, "1712519200")
    if delete_response:
        print("Item Deleted:")
        # Print response
        pprint(delete_response)
