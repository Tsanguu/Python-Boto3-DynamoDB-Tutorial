from pprint import pprint
import boto3


def put_device(device_id, datacount, timestamp, temperature1, temperature2, temperature3, temperature4, temperature5, dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="http://localhost:8000")

    devices_table = dynamodb.Table('Devices')
    response = devices_table.put_item(

        Item={
            'device_id': device_id,
            'datacount': datacount,
            'info': {
                'info_timestamp': timestamp,
                'temperature1': temperature1,
                'temperature2': temperature2,
                'temperature3': temperature3,
                'temperature4': temperature4,
                'temperature5': temperature5
            }
        }
    )
    return response


if __name__ == '__main__':
    device_resp = put_device("10001", 3, "1612522800",
                             "23.74", "32.56", "12.43", "44.74", "12.74")
    print("Create item successful.")
    pprint(device_resp)
