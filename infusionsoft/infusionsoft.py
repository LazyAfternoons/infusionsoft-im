import pickle
from os.path import exists

import requests
import base64
import logging
import http.client as http_client
import importlib

from infusionsoft.token import Token


class Infusionsoft:
    """Infusionsoft object for using their `REST API <https://developer.infusionsoft.com/docs/rest/#!>`.
    """

    def __init__(self, client_id, client_secret):
        """Creates a new Infusionsoft object.

        Args: client_id: The application client id which can be found `here
        <https://keys.developer.keap.com/my-apps>`. client_secret: The application client secret which can be found
        `here <https://keys.developer.keap.com/my-apps>`.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self.api = {}
        self.cached_objects = dict()

        # Logging initializer
        http_client.HTTPConnection.debuglevel = 0
        # logging.baseConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True
        logging.disable(logging.DEBUG)

    def set_debug(self, flag: bool):
        """Enable or disable debug for HTTP requests.

        Args:
            flag: True to enable the debug, false to disable it.
        """
        if flag:
            logging.disable(logging.NOTSET)
        else:
            logging.disable(logging.DEBUG)

    def is_token_serialized(self):
        """Check whether a token has been serialized previously.

        Returns:
            True if the serialized token exists, false otherwise.
        """
        return exists('token.dat')

    def deserialize_token(self):
        """Deserialize a previously stored token.
        """
        with open('token.dat', 'rb') as f:
            token = pickle.load(f)
        return token

    def set_token(self, token) -> None:
        """Set the token for the Infusionsoft object.
        """
        self.token = token

    def get_new_token(self, access_token: str, refresh_token: str, end_of_life: str):
        """Generates a new token with the given parameters.

        Args: access_token: The generated access token from the `'Your Accounts'
        <https://accounts.infusionsoft.com/app/central/home>` page. refresh_token: The generated refresh token from
        the `'Your Accounts' <https://accounts.infusionsoft.com/app/central/home>` page. end_of_life: The token
        expiration in unix time.

        Returns:
            The generated token.
        """
        token = Token(access_token, refresh_token, end_of_life)
        with open('token.dat', 'wb') as f:
            pickle.dump(token, f)
        return token

    def refresh_token(self):
        """Refreshes an expired token.

        Raises:
            InfusionsoftException: If an error occurs while refreshing the token.
        """
        url = 'https://api.infusionsoft.com/token'
        string = f'{self.client_id}:{self.client_secret}'
        bytes_string = string.encode('ascii')
        base64_byes = base64.b64encode(bytes_string)
        base64_string = base64_byes.decode('ascii')
        headers = {'Authorization': f'Basic {base64_string}', 'Content-type': 'application/x-www-form-urlencoded'}
        data = {'grant_type': 'refresh_token', 'refresh_token': self.token.refresh_token}
        r = requests.post(url, data=data, headers=headers)
        if r.status_code == 200:
            json_res = r.json()
            self.token.access_token = json_res.get('access_token')
            self.token.refresh_token = json_res.get('refresh_token')
            self.token.end_of_life = json_res.get('end_of_life')
        else:
            raise InfusionsoftException('An error occurred while refreshing the token.')

    def request(self, method, url, params=None, data=None, json=None, headers=None):
        """Performs a request to the REST endpoint.

        Args:
            method: The HTTP method.
            url: URL of the REST endpoint.
            params: Parameters of the request. Defaults to None.
            data: Data of the request. Defaults to None.
            json: JSON of the request. Defaults to None.
            headers: Headers of the request. Defaults to None.

        Returns:
            The content of the answer.
        """
        payload = {'access_token': self.token.access_token}
        if params:
            payload.update(params)
        method_to_call = getattr(requests, method)
        return method_to_call(url, params=payload, data=data, headers=headers, json=json)

    # missing return type
    def get_api(self, service):
        """Getter for an object representing the chosen API interface.
        Uses a cached array so no object is instantiated more than once during a request.

        Args:
             service: the name of the requested service.
        """
        if service in self.cached_objects:
            obj = self.cached_objects.get(service)
        else:
            try:
                module = importlib.import_module(f"infusionsoft.api.{service}")
                class_ = getattr(module, service.capitalize())
                obj = class_(self)
                self.cached_objects[service] = obj
            except (ModuleNotFoundError, AttributeError):
                raise InfusionsoftException("Unable to find the request API service object.")
        return obj

    def contact(self):
        """Getter for the Contact endpoint object.

        Returns:
             The object representing the Contact endpoint.
        """
        key = 'contact'
        return self.get_api(key)

    def company(self):
        """Getter for the Company endpoint object.

        Returns:
             The object representing the Contact endpoint.
        """
        key = 'company'
        return self.get_api(key)

    def account(self):
        """Getter for the Account endpoint object.

        Returns:
             The object representing the Aontact endpoint.
        """
        key = 'account'
        return self.get_api(key)

    def affiliate(self):
        """Getter for the Affiliate endpoint object.

        Returns:
             The object representing the Affiliate endpoint.
        """
        key = 'affiliate'
        return self.get_api(key)

    def appointment(self):
        """Getter for the Appointment endpoint object.

        Returns:
             The object representing the Appointment endpoint.
        """
        key = 'appointment'
        return self.get_api(key)

    def campaign(self):
        """Getter for the Campaign endpoint object.

        Returns:
             The object representing the Campaign endpoint.
        """
        key = 'campaign'
        return self.get_api(key)

class InfusionsoftException(Exception):
    """Exception thrown when an error related to Infusionsoft occurs
    """
    pass
