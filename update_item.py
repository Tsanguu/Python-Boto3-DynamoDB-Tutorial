from pprint import pprint  # import pprint, a module that enable to “pretty-print”
import boto3  # import Boto3


def update_device(device_id, datacount, info_timestamp, temperature1, temperature2, temperature3, temperature4, temperature5, dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="http://localhost:8000")
    # Specify the table
    devices_table = dynamodb.Table('Devices')

    response = devices_table.update_item(
        Key={
            'device_id': device_id,
            'datacount': datacount
        },
        UpdateExpression="set info.info_timestamp=:time, info.temperature1=:t1, info.temperature2=:t2, info.temperature3=:t3, info.temperature4=:t4, info.temperature5=:t5",
        ExpressionAttributeValues={
            ':time': info_timestamp,
            ':t1': temperature1,
            ':t2': temperature2,
            ':t3': temperature3,
            ':t4': temperature4,
            ':t5': temperature5
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_device(
        "10001", 3, "1612522800", "33.74", "23.74", "25.20", "22.00", "25.00")
    print("Device Updated")
    # Print response
    pprint(update_response)
