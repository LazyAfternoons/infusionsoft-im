from infusionsoft.api.apimodel import ApiModel


class Users(ApiModel):
    """Setting object for calling Infusionsoft API related to the remote Users object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Users object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Users, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/users'

    def list_users(self, params=None):
        """Retrieves a list of all users. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Users/listUsersUsingGET>`.

        Args:
            params: Dictionary, list of tuples or bytes to send in the query string for the Request.
            See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        return self.infusionsoft.request('get', self.service_url, params)

    def create_user(self, json):
        """Creates a new user record. NB: Users will be invited to the application and remain in the "Invited" status
        until the user accepts the invite. "Inactive" users will not take up a user license. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Users/createUserUsingPOST_2>`.

        Args:
            json: A JSON serializable Python object to send in the body of the Request.
            See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        return self.infusionsoft.request('post', self.service_url, json)

    def get_user_email_signature(self, user_id):
        """Retrieves a HTML snippet that contains the user's email signature. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Users/getUserSignatureUsingGET>`.

        Args:
            user_id:
                The ID of the user.s

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{user_id}/signature'
        return self.infusionsoft.request('post', url)
