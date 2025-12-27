from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from os import access
import iot_api_client as iot
from iot_api_client.rest import ApiException
from iot_api_client.configuration import Configuration

# Get your token 

oauth_client = BackendApplicationClient(client_id="YOUR_CLIENT_ID")
token_url = "https://api2.arduino.cc/iot/v1/clients/token"

oauth = OAuth2Session(client=oauth_client)
token = oauth.fetch_token(
    token_url=token_url,
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    include_client_id=True,
    audience="https://api2.arduino.cc/iot",
)

# store access token in access_token variable
access_token = token.get("access_token")

# configure and instance the API client with our access_token

client_config = Configuration(host="https://api2.arduino.cc/iot")
client_config.access_token = access_token
client = iot.ApiClient(client_config)
thing_id = "YOUR_THING_ID"

# as an example, interact with the properties API
api = iot.PropertiesV2Api(client)

try:
    resp = api.properties_v2_list(thing_id)
    print(resp)
except ApiException as e:
    print("Got an exception: {}".format(e))
