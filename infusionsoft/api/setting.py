from infusionsoft.api.apimodel import ApiModel


class Setting(ApiModel):
    """Setting object for calling Infusionsoft API related to the remote Setting Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Setting object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Setting, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/setting'

    def retrieve_application_configuration(self):
        """Get the properties for the current application's configuration.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/Setting/getConfigurationUsingGET>`.

         Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/application/configuration'
        return self.infusionsoft.request('get', url)

    def retrieve_application_status(self):
        """Retrieves whether the application is enabled.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/Setting/getApplicationEnabledUsingGET>`

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/application/enabled'
        return self.infusionsoft.request('get', url)

    def list_contact_types(self):
        """Lists the Contact types in a comma-separated list.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/Setting/getContactOptionTypesUsingGET>`

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/contact/optionTypes'
        return self.infusionsoft.request('get', url)
