import json
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "buckets": {
            "type": "object",
            "properties": {
                "create": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"}
                        },
                        "required": ["name"],
                        "additionalProperties": False
                    }
                },
                "delete": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"}
                        },
                        "required": ["name"],
                        "additionalProperties": False
                    }
                }
            },
            "additionalProperties": False  
        }
    },
    "required": ["buckets"],  
    "additionalProperties": False
}

def validate_buckets_config(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        validate(instance=data, schema=schema)
        print("Validation successful: The configuration file is valid.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format. {e}")
    except ValidationError as e:
        print(f"Validation failed: {e.message}")

if __name__ == "__main__":
    config_file = "buckets.json"  
    validate_buckets_config(config_file)
