import boto3  # import Boto3


def delete_devices_table(dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb', endpoint_url="http://localhost:8000")
    # specify the table to be deleted
    devices_table = dynamodb.Table('Devices')
    devices_table.delete()


if __name__ == '__main__':
    delete_devices_table()
    print("Table deleted.")
