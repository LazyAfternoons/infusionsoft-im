from infusionsoft.api.apimodel import ApiModel


class Company(ApiModel):
    """Company object for calling Infusionsoft API related to the remote Company object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Company object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Company, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/companies'

    def get_service_url(self):
        return self.service_url

    def list_companies(self, params=None):
        """Retrieves a list of all companies. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Company/listCompaniesUsingGET>`.

        Args:
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.
        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.service_url, params=params)

    def create_company(self, json):
        """Creates a new company. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Company/createCompanyUsingPOST>`.

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.
        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('post', self.service_url, json=json)

    def retrieve_company(self, company_id, params=None):
        """Retrieves a single company. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Company/getCompanyUsingGET>`.

        Args:
            company_id:
                The ID of the company.
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f"{self.service_url}/{company_id}"
        return self.infusionsoft.request('get', url, params)

    def update_company(self, company_id, json):
        """Updates a company with only the values provided in the request. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Company/updateCompanyUsingPATCH>`.

        Args:
            company_id:
                The ID of the company to be updated.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f"{self.service_url}/{company_id}"
        return self.infusionsoft.request('patch', url, json)

    def retrieve_company_model(self):
        """Get the custom fields and optional properties for the Company object

        Returns:
            The JSON result of the request.
        """
        url = f"{self.service_url}/model"
        return self.infusionsoft.request('get', url)


