import yaml
import json

# Load variables from YAML file
with open('pipeline.yaml', 'r') as yaml_file:
    variables = yaml.safe_load(yaml_file)

# Load test cases from JSON file
with open(variables['test_case_file_path'], 'r') as json_file:
    test_cases = json.load(json_file)

# Print test cases
print(test_cases)
