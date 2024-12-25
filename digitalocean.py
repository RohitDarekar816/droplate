import requests
import json

# Replace with your DigitalOcean API token
API_TOKEN = 'dop_v1_bca16ed397adfd4b3d119c148f8cf1bf366f256f989ac594037fb2feda7114bc'

# Set the headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_TOKEN}'
}

# Define the droplet configuration
droplet_data = {
    "name": "Test-droplet",
    "region": "nyc3", # Region where the droplet will be created
    "size": "s-1vcpu-1gb", # Droplet size
    "image": "ubuntu-20-04-x64", # Image to use for the droplet
    "ssh_keys": [], # Optional: List of SSH key fingerprints or IDs
    "backups": False, # Optional: Enable backups
    "ipv6": True, # Optional: Enable IPv6
    "user_data": None, # Optional: Cloud-init metadata
    "private_networking": None, # Optional: Private networking
    "volumes": None, # Optional: List of volumes
    "tags": ["example"] # Optional: List of tags
}

# Make the API request to create the droplet
response = requests.post(
    "https://api.digitalocean.com/v2/droplets",
    headers=headers,
    data=json.dumps(droplet_data)
)

# Check the response status code
if response.status_code == 202:
    print("Droplet creation initiated successfully!")
    droplet_info = response.json()
    print(json.dumps(droplet_info, indent=4))
else:
    print("Failed to create droplet")
    print("Status Code:", response.status_code)
    print("Response:", response.json())