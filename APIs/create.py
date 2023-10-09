# Importing Dependencies #
from APIs import *
from Utilities import validate_data_schema, generate_file_path, upload_file_to_s3


# Create API #
def create():
    response = None
    try:
        data = json.loads(request.data)
        data_schema = None
        if 'schema_file' in data:
            file = data['schema_file']
            data_schema = file.read()
        elif data.get('data_schema'):
            data_schema = json.dumps(data.get('data_schema'))
        schema_validation_result = validate_data_schema(data_schema)
        if schema_validation_result[0]:
            data['data_schema'] = json.loads(data_schema)
            file_path = generate_file_path()
            assert upload_file_to_s3(file_path, json.dumps(data)), "Failed to upload file to AWS S3."
            response = {
                'statusCode': 200,
                'message': 'Record inserted successfully.'
            }
        else:
            response = {
                'statusCode': 400,
                'message': schema_validation_result[1]
            }
    except Exception as err:
        print(f"Exception occurred while processing data: {err}")
        response = {
            'statusCode': 500,
            'message': 'Internal Server Error.',
            'additionalInfo': str(err)
        }
    return jsonify(response)