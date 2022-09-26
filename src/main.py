from macaddress_client import MacAddressClient
import os
import logging
import sys

LOG = logging.getLogger(__name__)


def main(mac_address: str):
    mac_address_client = MacAddressClient(api_token=os.getenv("API_TOKEN"))
    print(mac_address_client.get_company_name(mac_address))


if __name__ == "__main__":
    main(sys.argv[1])
