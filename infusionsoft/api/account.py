from infusionsoft.api.apimodel import ApiModel


class AccountInfo(ApiModel):
    """AccountInfo object for calling Infusionsoft API related to the remote Account Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new AccountInfo object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(AccountInfo, self).__init__(infusionsoft)
        self.service_url = f'{self.service_url}/account/profile'

    def retrieve_account_profile(self):
        """Retrieves profile/company info for an account. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Account_Info/getAccountProfileUsingGET>`.

        Returns:
            The JSON result of the request.
        """
        r = self.infusionsoft.request('get', self.service_url)
        return r.text

    def updates_account_profile(self, json):
        """Updates profile/company info for an account. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Account_Info/updateAccountInfoUsingPUT>`.

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        r = self.infusionsoft.request('put', self.service_url, json=json)
        return r.text



