from infusionsoft.api.apimodel import ApiModel


class UserInfo(ApiModel):
    """Setting object for calling Infusionsoft API related to the remote User Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new UserInfo object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(UserInfo, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/oath/connect/userinfo'

    def retrieve_user_info(self):
        """Retrieves a list of all tasks using the specified search criteria. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Task/listTasksUsingGET>`.

        Returns:
            The JSON response of the request.
        """
        return self.infusionsoft.request('get', self.service_url)
