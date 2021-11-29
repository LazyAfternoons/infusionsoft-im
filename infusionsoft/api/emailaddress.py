from infusionsoft.api.apimodel import ApiModel


class EmailAddress(ApiModel):
    """EmailAddress object for calling Infusionsoft API related to the remote EmailAddress Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new EmailAddress object.`

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(EmailAddress, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/Addresses'

    def replace_email_address(self, email, json):
        """Replaces all of the values of a given email address.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/Email_Address/replaceEmailAddressUsingPUT>`

        Args:
            email:
                Email to be replaced.
            json:
                A JSON serializable Python object to send in the body of the Request.
                See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'({self.service_url}/{email}'
        return self.infusionsoft.request('put', url, json)
