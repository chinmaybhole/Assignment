import json


def compare_json(json1, json2):
    diff = {}
    for key in json1.keys():
        if key not in json2:
            diff[key] = json1[key]

        # If key is also a dict
        elif isinstance(json1[key], dict) and isinstance(json2[key], dict):
            nested_diff = compare_json(json1[key], json2[key])
            if nested_diff:
                diff[key] = nested_diff
        elif json1[key] != json2[key]:
            diff[key] = json1[key]
    for key in json2.keys():
        if key not in json1:
            diff[key] = json2[key]
        elif isinstance(json1[key], dict) and isinstance(json2[key], dict):
            nested_diff = compare_json(json1[key], json2[key])
            if nested_diff:
                diff[key] = nested_diff
        elif json1[key] != json2[key]:
            diff[key] = json2[key]
    return diff


# Test the function
json1 = '{"x": 10.1, "y": 20, "name": "Anu", "dob": "2010-10-10"}'
json2 = '{"x": 10, "y": 20, "name": "Ani", "dob": "2010-10-11", "z": 100}'

parsed_json1 = json.loads(json1)
parsed_json2 = json.loads(json2)

diff_json = compare_json(parsed_json1, parsed_json2)

print(json.dumps(diff_json, indent=4))
"""
{
    "x": 10,
    "name": "Ani",
    "dob": "2010-10-11",
    "z": 100
}
"""
