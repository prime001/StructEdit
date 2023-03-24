import json
import yaml

class SchemaParser:
    def __init__(self, schema_path):
        self.schema_path = schema_path

    def parse(self):
        with open(self.schema_path) as schema_file:
            schema_contents = schema_file.read()

        if self.schema_path.endswith('.json'):
            schema_dict = json.loads(schema_contents)
        elif self.schema_path.endswith('.yaml') or self.schema_path.endswith('.yml'):
            schema_dict = yaml.safe_load(schema_contents)
        else:
            raise ValueError('Unsupported schema file format')

        return schema_dict
