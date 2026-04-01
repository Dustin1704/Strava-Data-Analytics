import webbrowser as webb
import json
from stravalib.client import Client

# --- Setup Strava Authetication ---
client_id, client_secret = open("ingestion/client_secrets.txt").read().strip().split(",")
client = Client()
request_scope = ["read_all", "profile:read_all", "activity:read_all"]
redirect_url = "http://127.0.0.1:5000/authorization"

url = client.authorization_url(
    client_id = client_id,
    redirect_uri = redirect_url,
    scope =  request_scope
)

print(url)

# --- Login and authroise Strava to interact with code ---
code = input("Enter code: ")

token_response = client.exchange_code_for_token(
    client_id = client_id,
    client_secret = client_secret,
    code = code
)

with open(json_poath, "w") as f:
    json.dump(token_response, f)
print("Token Saved")

access_token = token_response["access_token"]
refresh_token = token_response["refresh_topken2"] # Use after 6 hours

# --- Use and refresh strava API token ---
