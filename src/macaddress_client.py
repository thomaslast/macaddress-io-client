import requests
import os


class NoTokenProvided(BaseException):
    pass


class MacAddressClient:
    def __init__(self, url: str = "https://api.macaddress.io/", api_token: str = None):
        """
        A Macaddress.io client to fetch info about the macaddress
        :param url: The base url for the macaddress api
        :type url: str
        :param api_token: the api token used for auth
        :type api_token: str
        """
        self.url = url
        if api_token is not None:
            self.api_token = api_token
        else:
            raise NoTokenProvided("Need to provide an API Token")
        self.headers = {"content-type": "application/json; charset=UTF-8", "X-Authentication-Token": self.api_token}

    def get_company_name(self, mac_address: str) -> str:
        """
        Return the company name string
        :param mac_address: the macaddress to search for
        :type mac_address: str
        :return: The company name
        :rtype: str
        """
        req = requests.get(f"{self.url}/v1?output=json&search={mac_address}", headers=self.headers).json()
        return req["vendorDetails"]["companyName"]

