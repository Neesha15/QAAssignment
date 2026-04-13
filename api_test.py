import pytest
import requests
import json


def test_public_api(base_url):
    response = requests.get(base_url+ "/posts")
    json_data = response.json()
    assert response.status_code == 200
    required_keys = {"userId", "id", "title", "body"}

    if all(required_keys.issubset(post) for post in json_data):
        print("All posts valid")

    with open("first_5_posts.json", "w") as file:
        json.dump(json_data[:5], file)

