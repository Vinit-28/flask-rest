# Importing Dependencies #
from Utilities import *


# Function to validate data schema #
def validate_data_schema(data_schema):
    try:
        assert data_schema is not None, "Invalid data schema."
        data_schema = json.loads(data_schema)
        assert isinstance(data_schema.get('Columns'), list), "Invalid data schema."
        assert len(data_schema.get('Columns')) > 0, "Empty data schema."

        for column in data_schema['Columns']:
            if not (column.get('Name') and column.get('Type')):
                raise Exception(f"Invalid data schema. Issue with '{column.get('Name')}' Column.")
        return True, ""
    except Exception as err:
        print(f"Exception occurred while validating data schema: {err}")
        return False, f"{err}"