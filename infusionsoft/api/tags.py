from infusionsoft.api.apimodel import ApiModel


class Tags(ApiModel):
    """Setting object for calling Infusionsoft API related to the remote Setting Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Setting object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Tags, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/tags'

    def list_tags(self, params=None):
        """Retrieve a list of tags defined in the application. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Tags/listTagsUsingGET>`.

        Args:
            params:
                Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        return self.infusionsoft.request('get', self.service_url, params=params)


    def create_tag(self, json):
        """Create a new tag. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Tags/createTagUsingPOST>`

        Returns:
            The JSON response containing contacts.
        """
        return self.infusionsoft.request('post', self.service_url, json=json)

    def retrieve_tag(self, id):
        """Retrieves a single tag. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Tags/getTagUsingGET>`

        Args:
            id:
                The ID of the tag.

        Returns:
            The JSON response containing contacts.
        """
        url = f'{self.service_url}/{id}'
        return self.infusionsoft.request('get', url)

    def list_tagged_companies(self, tag_id, params=None):
        """Retrieves a list of companies that have the given tag applied. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Tags/listCompaniesForTagIdUsingGET>`

        Args:
            tag_id:
                The ID of the tag.
            params:
                Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON response containing contacts.
        """
        url = f'{self.service_url}/{tag_id}'
        return self.infusionsoft.request('get', url, params)

    def remove_tag_contanct(self, tag_id, params):
        """Remove a tag from a list of contacts. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Tags/removeTagFromContactIdsUsingDELETE>`

        Args:
            tag_id:
                The ID of the tag.
            params:
                Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON response containing contacts.
        """
        url = f'{self.service_url}/{tag_id}'
        return self.infusionsoft.request('delete', url, params)

    def list_tagged_contacts(self, tag_id, params):
        """Retrieves a list of contacts that have the given tag applied. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Tags/listContactsForTagIdUsingGET>`

        Args:
            tag_id:
                The ID of the tag.
            params:
                Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON response containing contacts.
        """
        url = f'{self.service_url}/{tag_id}/contacts'
        return self.infusionsoft.request('get', url, params)

    def apply_tag_contact(self, tag_id, json):
        """Apply a tag to a list of contacts. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Tags/applyTagToContactIdsUsingPOST>`

        Args:
            tag_id:
                The ID of the tag.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON response containing contacts.
        """
        url = f'{self.service_url}/{tag_id}/contacts'
        return self.infusionsoft.request('get', url, json)

    def remove_tag_contact(self, tag_id, contact_id):
        """Remove a tag from a Contact. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Tags/removeTagFromContactIdUsingDELETE>`

        Args:
            tag_id:
                The ID of the tag.
            contact_id:
                The ID of the contact.

        Returns:
            The JSON response containing contacts.
        """
        url = f'{self.service_url}/{tag_id}/contacts/{contact_id}'
        return self.infusionsoft.request('get', url)

    def create_tag_category(self, json):
        """Create a new tag category. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Tags/createTagCategoryUsingPOST>`

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON response containing contacts.
        """
        url = f'{self.service_url}/categories'
        return self.infusionsoft.request('post', url, json=json)



