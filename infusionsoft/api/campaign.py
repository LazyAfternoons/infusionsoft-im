from infusionsoft.api.apimodel import ApiModel


class Campaign(ApiModel):
    """Campaign object for calling Infusionsoft API related to the remote Campaign Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Campaign object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Campaign, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/campaigns'

    def list_campaigns(self, params=None):
        """Retrieves all campaigns for the authenticated user. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Campaign/listCampaignsUsingGET>`.

        Args:
            params:
                Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.service_url, params)

    def retrieve_campaign(self, campaign_id, params=None):
        """Retrieves a single campaign. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Campaign/getCampaignUsingGET>`.

        Args:
            campaign_id:
                The id of the campaign.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{campaign_id}'
        return self.infusionsoft.request('get', url, params=params)

    def remove_multiple_campaign_sequence(self, campaign_id, sequence_id, json):
        """Removes a list of contacts from a campaign sequence. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Campaign/removeContactsFromCampaignSequenceUsingDELETE>`.

        Args:
            campaign_id:
                The ID of the campaign.
            sequence_id:
                The ID of the sequence.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{campaign_id}/sequences/{sequence_id}/contacts'
        return self.infusionsoft.request('post', url, json=json)

    def add_multiple_campaign_sequence(self, campaign_id, sequence_id, json):
        """Adds a list of contacts to a campaign sequence. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Campaign/addContactsToCampaignSequenceUsingPOST>`.

        Args:
            campaign_id:
                The ID of the campaign.
            sequence_id:
                The ID of the sequence.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{campaign_id}/sequences/{sequence_id}/contacts'
        return self.infusionsoft.request('post', url, json=json)

    def remove_campaign_sequence(self, campaign_id, sequence_id, contact_id):
        """Removes a single contact from a campaign sequence. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Campaign/removeContactFromCampaignSequenceUsingDELETE>`.

        Args:
            campaign_id:
                The ID of the campaign.
            sequence_id:
                The ID of the sequence.
            contact_id:
                The ID of the contact.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{campaign_id}/sequences/{sequence_id}/contacts/{contact_id}'
        return self.infusionsoft.request('delete', url)

    def add_campaign_sequence(self, campaign_id, sequence_id, contact_id):
        """Adds a single contact to a campaign sequence. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Campaign/addContactToCampaignSequenceUsingPOST>`.

        Args:
            campaign_id:
                The ID of the campaign.
            sequence_id:
                The ID of the sequence.
            contact_id:
                The ID of the contact.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{campaign_id}/sequences/{sequence_id}/contacts/{contact_id}'
        return self.infusionsoft.request('post', url)

    def achieve_api_goal(self, integration, call_name, json):
        """Achieves API goal for campaigns with matching integration, callName for a given contactId. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Campaign/createAchieveApiGoalEventUsingPOST>`.

        Args:
            integration:
                ?
            call_name:
                ?
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/goalgs/{integration}/{call_name}'
        return self.infusionsoft.request('post', url, json=json)
