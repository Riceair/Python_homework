import json
json_obj = '{"ID":"A1065506","Class":"CSIE","Year":3}'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(json_obj)

print("\nID:",python_obj["ID"])
print("Class:",python_obj["Class"])
print("Year:",python_obj["Year"])
