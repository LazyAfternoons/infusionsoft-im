from infusionsoft.api.apimodel import ApiModel


class Company(ApiModel):
    """Company object for calling Infusionsoft API related to the remote Company object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Contact object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Company, self).__init__(infusionsoft)
        self.service_url = f'{self.service_url}/companies'

    def get_service_url(self):
        return self.service_url

    def list_companies(self, params=None):
        """Retrieves a list of all companies. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Company/listCompaniesUsingGET>`.

        Args:
            params:
                Dictionary, bytes, or file-like object parameters for filtering companies. See the API reference for more information.
        Returns:
            The JSON result of the request containing companies.
        """
        r = self.infusionsoft.request('get', self.service_url, json=params)
        return r.text

    def create_company(self, params):
        """Creates a new company. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Company/createCompanyUsingPOST>`.

        Args:
            params:
                Dictionary, bytes, or file-like object parameters for creating a company. See the API reference for more information.
        Returns:
            The JSON result of the request.
        """
        r = self.infusionsoft.request('post', self.service_url, json=params)
        return r.text

    def retrieve_company(self, company_id, params=None):
        """Retrieves a single company. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Company/getCompanyUsingGET>`.

        Args:
            company_id:
                The ID of the company.
            params:
                 Dictionary, bytes, or file-like object parameters containing contact properties to be included in the response. See the API reference for more information.

        Returns:
            The JSON result of the request containing the company data.
        """
        url = f"{self.service_url}/{company_id}"
        r = self.infusionsoft.request('get', url, params)
        return r.text

    def update_company(self, company_id, params):
        """Updates a company with only the values provided in the request. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Company/updateCompanyUsingPATCH>`.

        Args:
            company_id:
                The ID of the company to be updated.
            params:
                Dictionary, bytes, or file-like object parameters containing fields to be updated. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f"{self.service_url}/{company_id}"
        r = self.infusionsoft.request('patch', url, params)
        return r.text

    def retrieve_company_model(self):
        """Get the custom fields and optional properties for the Company object

        Returns:
            The JSON result of the request containing the company model.
        """
        url = f"{self.service_url}/model"
        r = self.infusionsoft.request('get', url)
        return r.text


