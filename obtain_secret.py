from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import os

def get_secret_value() -> tuple:
    secret_value = None
    error = None

    # read configuration values from environment
    key_vault_name = os.environ["KEY_VAULT_NAME"]
    environment    = os.environ["APPLICATION_ENVIRONMENT"]
    secret_name    = os.environ["SECRET_NAME"]
    
    # generate key vault URL
    url = f"https://{key_vault_name}-{environment}.vault.azure.net"

    # get application credential
    credential = DefaultAzureCredential()

    client = SecretClient(vault_url=url, credential=credential)

    secret_value = client.get_secret(secret_name).value

    return (error, secret_value)
