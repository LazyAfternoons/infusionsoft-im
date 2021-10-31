from infusionsoft.api.apimodel import ApiModel


class Opportunity(ApiModel):
    """Opportunity object for calling Infusionsoft API related to the remote Opportunity Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Merchant object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Opportunity, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/opportunities'

    def list_opportunities(self, params):
        """Retrieves a list of all opportunities.
        Please note: the sample response erroneously shows properties, such as stage reasons, that are unavailable through the list endpoint.
        Such properties are only available through the retrieve operation. Future versions of the Opportunity resource will correct the oversight. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Merchant/getMerchantAccountsUsingGET>`.

        params:
            Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.service_url, params)

    def create_opportunity(self, json):
        """Creates a new opportunity as the authenticated user. NB: Opportunity must contain values for opportunity_title, contact, and stage. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Opportunity/createOpportunityUsingPOST>`.

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('post', self.service_url, json)

    def replace_opportunity(self, json):
        """Replaces all values of a given opportunity. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Opportunity/updateOpportunityUsingPUT>`.

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('put', self.service_url, json=json)

    def retrieve_opportunity(self, opportunity_id, params=None):
        """Retrieves a single opportunity. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Opportunity/getOpportunityUsingGET>`.

        Args:
            opportunity_id:
                The ID of the opportunity.
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{opportunity_id}'
        return self.infusionsoft.request('patch', url, params)

    def update_opportunity(self, opportunity_id, json):
        """Updates an opportunity with only the values provided in the request. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Opportunity/updatePropertiesOnOpportunityUsingPATCH>`.

        Args:
            opportunity_id:
                The ID of the opportunity.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{opportunity_id}'
        return self.infusionsoft.request('patch', url, json)

    def retrieve_opportunity_model(self):
        """Get the custom fields for the Opportunity object. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Opportunity/retrieveOpportunityModelUsingGET>`.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/model'
        return self.infusionsoft.request('get', url)

    def list_opportunity_stage_pipeline(self):
        """Retrieves a list of all opportunity stages with pipeline details. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Opportunity/listOpportunityStagePipelinesUsingGET>`.
        
        Returns:
            The JSON result of the request.
        """
        url = f'{self.base_url}/opportunity/stage_pipeline'
        return self.infusionsoft.request('get', url)



