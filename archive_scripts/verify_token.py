import requests

token = "YOUR_TOKEN_HERE"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get("https://huggingface.co/api/whoami-v2", headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Token is VALID!")
    print(f"Logged in as: {data.get('name', 'Unknown')}")
else:
    print(f"Token is INVALID! Status: {response.status_code}")
    print(response.text)
