import pytest
import requests
import json
from jsonschema import validate


def test_response_time(base_url):
    response = requests.get(base_url+"/posts")
    assert response.status_code == 200
    response_time = response.elapsed.total_seconds()
    print(response_time)
    assert response_time < 2

def test_schema(base_url):
    response = requests.get(base_url+ "/posts")
    json_data = response.json()
    assert response.status_code == 200
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }
    for item in json_data:
        validate(instance=item, schema=schema)

@pytest.mark.parametrize("endpoint", ["posts", "comments", "users"])
def test_endpoint(base_url,endpoint):
    response = requests.get(f"{base_url}/{endpoint}")
    json_data = response.json()
    assert response.status_code == 200

