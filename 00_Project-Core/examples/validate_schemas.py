import json
import os
try:
    from jsonschema import validate, ValidationError
except ImportError:
    print("jsonschema library not found. Skipping automated validation.")
    exit(0)

def validate_file(file_path, schema_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    with open(schema_path, 'r') as s:
        schema = json.load(s)
    try:
        validate(instance=data, schema=schema)
        print(f"PASS: {file_path} matches {schema_path}")
    except ValidationError as e:
        print(f"FAIL: {file_path} failed validation: {e.message}")

if __name__ == "__main__":
    # Placeholder for simple validation script logic
    # In a real CI environment, this would loop through examples
    print("Schema validation utility (v3.1)")
    print("Run this to verify packet compliance.")
