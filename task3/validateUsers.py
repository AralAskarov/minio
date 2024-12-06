import json
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "users": {
            "type": "object",
            "properties": {
                "create": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "username": {"type": "string"},
                            "password": {"type": "string"},
                            "policies": {
                                "type": "array",
                                "items": {"type": "string"}
                            }
                        },
                        "required": ["username", "password", "policies"],
                        "additionalProperties": False
                    }
                },
                "delete": {
                    "type": "array",
                    "items": {"type": "string"}
                }
            },
            "additionalProperties": False
        }
    },
    "required": ["users"],
    "additionalProperties": False
}

def validate_users_config(file_path):
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
    config_file = "users.json"  
    validate_users_config(config_file)
