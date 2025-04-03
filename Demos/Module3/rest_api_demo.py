# REST API Demo using Python Requests
# Demonstrates GET, POST, PUT, PATCH, DELETE requests
# Includes Simple Authentication, Token Authentication, OAuth2

import requests
from requests.auth import HTTPBasicAuth

# Base URL for JSONPlaceholder
BASE_URL = "https://jsonplaceholder.typicode.com"

# ================================
# 1. GET Request (No Authentication)
# ================================
response = requests.get(f"{BASE_URL}/posts/1")
print("GET Response:", response.json())

# ================================
# 2. POST Request (No Authentication)
# ================================
payload = {"title": "Test Post", "body": "This is a test post.", "userId": 1}
response = requests.post(f"{BASE_URL}/posts", json=payload)
print("POST Response:", response.json())

# ================================
# 3. PUT Request (No Authentication)
# ================================
update_payload = {"title": "Updated Title", "body": "Updated body.", "userId": 1}
response = requests.put(f"{BASE_URL}/posts/1", json=update_payload)
print("PUT Response:", response.json())

# ================================
# 4. PATCH Request (No Authentication)
# ================================
patch_payload = {"title": "Patched Title"}
response = requests.patch(f"{BASE_URL}/posts/1", json=patch_payload)
print("PATCH Response:", response.json())

# ================================
# 5. DELETE Request (No Authentication)
# ================================
response = requests.delete(f"{BASE_URL}/posts/1")
print("DELETE Response Code:", response.status_code)

# ================================
# 6. Simple Authentication (Basic Auth)
# ================================
response = requests.get("https://httpbin.org/basic-auth/user/pass", auth=HTTPBasicAuth('user', 'pass'))
print("Basic Auth Response:", response.json())

# ================================
# 7. Token Authentication
# ================================
TOKEN = "your_token_here"
headers = {"Authorization": f"Bearer {TOKEN}"}
response = requests.get("https://httpbin.org/bearer", headers=headers)
print("Token Auth Response:", response.json())

# ================================
# 8. OAuth2 Authentication
# ================================
# Example using client credentials flow
OAUTH_URL = "https://example.com/oauth/token"
client_id = "your_client_id"
client_secret = "your_client_secret"

data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

# Uncomment the following lines when using a real OAuth2 service
# response = requests.post(OAUTH_URL, data=data)
# access_token = response.json().get("access_token")
# headers = {"Authorization": f"Bearer {access_token}"}
# response = requests.get("https://example.com/protected_resource", headers=headers)
# print("OAuth2 Response:", response.json())

print("Demo complete.")