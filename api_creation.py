from google.cloud import api_keys_v2
from google.cloud.api_keys_v2 import Key

def create_api_key(project_id: str, suffix: str) -> Key:
    """
    Creates and restricts an API key. Add the suffix for uniqueness.

    TODO(Developer):
    1. Before running this sample,
      set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
    2. Make sure you have the necessary permissions to create API keys.

    Args:
        project_id: Google Cloud project id.

    Returns:
        response: Returns the created API Key.
    """
    # Create the API Keys client.
    client = api_keys_v2.ApiKeysClient()

    key = api_keys_v2.Key()
    key.display_name = f"My first API key - {suffix}"

    # Initialize request and set arguments.
    request = api_keys_v2.CreateKeyRequest()
    request.parent = f"projects/{project_id}/locations/global"
    request.key = key

    # Make the request and wait for the operation to complete.
    response = client.create_key(request=request).result()

    print(f"Successfully created an API key: {response.name}")
    # For authenticating with the API key, use the value in "response.key_string".
    # To restrict the usage of this API key, use the value in "response.name".
    print(f"API Key: {response.key_string}")  # This will print the actual API key.

    return response

# Example usage:
# Replace with your actual Google Cloud project ID and a suffix for the key.
project_id = 'your-google-cloud-project-id'
suffix = 'unique-suffix'
create_api_key(project_id, suffix)
