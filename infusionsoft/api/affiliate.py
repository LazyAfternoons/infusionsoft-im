from infusionsoft.api.apimodel import ApiModel


class Affiliate(ApiModel):
    """Affiliate object for calling Infusionsoft API related to the remote Affiliate object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Affiliate object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Affiliate, self).__init__(infusionsoft)
        self.service_url = f'{self.service_url}/affiliates'

    def list_affiliate(self, params=None):
        """Retrieves a list of all affiliates. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Affiliate/listAffiliatesUsingGET>`.

        Args:
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.
        Returns:
            The JSON result of the request.
        """
        r = self.infusionsoft.request('get', self.service_url, params=params)
        return r.text

    def create_affiliate(self, json):
        """Create a single affiliate. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Affiliate/createAffiliateUsingPOST>`.

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        r = self.infusionsoft.request('post', self.service_url, json=json)
        return r.text

    def list_affiliate_clawbacks(self, affiliate_id, params):
        """Retrieves a list of all affiliate clawbacks. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Affiliate/listAffiliateClawbacksUsingGET>`.

        Args:
            affiliate_id:
                The ID of the affiliate.
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{affiliate_id}/clawbacks'
        r = self.infusionsoft.request('get', affiliate_id, params)
        return r.text

    def list_affiliate_payments(self, affiliate_id, json, params):
        """Retrieves a list of all affiliate payments. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Affiliate/listPaymentsUsingGET>`.

        Args:
            affiliate_id:
                The ID of the affiliate.
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{affiliate_id}/payments'
        r = self.infusionsoft.request('get', url, affiliate_id, params=params, json=json)
        return r.text

    def retrieve_affiliate(self, id):
        """Retrieve a single affiliate. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Affiliate/getAffiliateUsingGET>`.

        Args:
            id:
                The ID of the affiliate.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{id}'
        r = self.infusionsoft.request('get', url)
        return r.text

    def list_commissions(self, params):
        """Retrieve a list of Commissions based on Affiliate or Date Range. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Affiliate/listCommissionsUsingGET>`.

        Args:
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/commissions'
        r = self.infusionsoft.request('get', url, params=params)
        return r.text

    def retrive_affiliate_model(self):
        """Get the custom fields for the Affiliate object. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Affiliate/retrieveAffiliateModelUsingGET>`.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/model'
        r = self.infusionsoft.request('get', url)
        return r.text

    def list_commission_programs(self, params=None):
        """Retrieve a list of Commission Programs. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Affiliate/listProgramsUsingGET>`.

        Args:
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/programs'
        r = self.infusionsoft.request('get', url, params=params)
        return r.text

    def list_affiliate_redirects(self, params=None):
        """Retrieves a list of all affiliate redirects. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Affiliate/listAffiliateRedirectLinksUsingGET>`.

        Args:
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/redirectlinks'
        r = self.infusionsoft.request('get', url, params=params)
        return r.text

    def list_affiliate_summaries(self, params=None):
        """Retrieves a list of all affiliate redirects. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Affiliate/listSummariesUsingGET>`.

        Args:
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/summaries'
        r = self.infusionsoft.request('get', url, params=params)
        return r.text
