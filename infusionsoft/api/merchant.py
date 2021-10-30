from infusionsoft.api.apimodel import ApiModel


class Merchant(ApiModel):
    def __init__(self, infusionsoft):
        """Creates a new Merchant object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Merchant, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/merchants'

    def list_merchant(self):
        """Retrieves a list of all merchant accounts.

        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.service_url)