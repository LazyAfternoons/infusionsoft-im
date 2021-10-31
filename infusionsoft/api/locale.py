from infusionsoft.api.apimodel import ApiModel


class Locale(ApiModel):
    """Locale object for calling Infusionsoft API related to the remote Locale Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Locale object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Locale, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/locales/countries'

    def list_countries(self):
        """Retrieves a list of all countries with their locale code. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Locale/listCountriesUsingGET>`.

        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.service_url)

    def list_country_provinces(self, country_code):
        """Retrieves a list of all the provinces of the given country. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Locale/listCountriesUsingGET_1>`.

        Args:
            country_code: The code of the country.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{country_code}/provinces'
        return self.infusionsoft.request('get', self.service_url)