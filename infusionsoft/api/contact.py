from infusionsoft.api.apimodel import ApiModel


class Contact(ApiModel):
    """Contact object for calling Infusionsoft API related to the remote Contact object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Contact object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Contact, self).__init__(infusionsoft)
        self.service_url = f'{self.service_url}/contacts'

    def list_contact(self):
        """Lists all the contacts in Infusionsoft. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/listContactsUsingGET!>`.

        Returns:
            The JSON response containing contacts.
        """
        r = self.infusionsoft.request('get', self.service_url)
        return r.text

    def create_contact(self, params):
        """Creates a new contact in Infusionsoft. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/createContactUsingPOST!>`.

        Args:
            params:
                Dictionary, bytes, or file-like object parameters for creating the contact. See the API reference for more information.
        Returns:
            The JSON result of the request.
        """
        r = self.infusionsoft.request('post', self.service_url, json=params)
        return r.text

    def create_update_contact(self, params):
        """Creates or updates a contact in Infusionsoft. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/createOrUpdateContactUsingPUT>`.

        Args:
            params:
                Dictionary, bytes, or file-like object parameters for creating the contact. See the API reference for more information.
        Returns:
            The JSON result of the request.
        """
        r = self.infusionsoft.request('put', self.service_url, json=params)
        return r.text

    def delete_contact(self, contact_id):
        """Deletes a contact in Infusionsoft. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/deleteContactUsingDELETE>`.

        Args:
            contact_id:
                The ID of the contact.
        Returns:
            The JSON result of the request.
        """
        url = f"{self.service_url}/{contact_id}"
        r = self.infusionsoft.request('delete', url)
        return r.text

    def update_contact(self, contact_id, params):
        """Deletes a contact in Infusionsoft. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/updatePropertiesOnContactUsingPATCH>`.

        Args:
            contact_id:
                The ID of the contact.
            params:
                Dictionary, bytes, or file-like object parameters for updating the contact. See the API reference for more information.
        Returns:
            The JSON result of the request.
        """
        url = f"{self.service_url}/{contact_id}"
        r = self.infusionsoft.request('patch', url, json=params)
        return r.text

    def retrieve_credit_cards(self, contact_id):
        """Lists all credit cards on a contact. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/listCreditCardsUsingGET>`.

       Args:
           contact_id:
               The ID of the contact.
       Returns:
           The JSON result of the request containing credit cards.
       """
        url = f"{self.service_url}/{contact_id}/creditCards"
        r = self.infusionsoft.request('get', url)
        return r.text

    def create_credit_card(self, contact_id):
        """Creates a new credit card associated to a contact. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/createCreditCardUsingPOST>`.

        Args:
            contact_id:
                The ID of the contact whose credit card is.

        Returns:
            The JSON result of the request.
        """
        url = f"{self.service_url}/{contact_id}/creditCards"
        r = self.infusionsoft.request('post', url)
        return r.text

    def list_emails(self, contact_id, params):
        """Lists Emails that have been sent to a Contact. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/listEmailsForContactUsingGET>`.

        Args:
            contact_id:
                The contact ID.
            params:
                Dictionary, bytes, or file-like object parameters of the request for sorting mails. See the API reference for more information.

        Returns:
            The JSON result of the request containing emails.
        """
        url = f"{self.service_url}/{contact_id}/emails"
        r = self.infusionsoft.request('get', url, json=params)
        return r.text

    def create_email_record(self, contact_id, params):
        """Creates a record of an email sent to a contact. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/createEmailForContactUsingPOST>`.

        Args: contact_id: The ID of the contact.
            params:
                Dictionary, bytes, or file-like object parameters of the request for providing context. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f"{self.service_url}/{contact_id}/emails"
        r = self.infusionsoft.request('post', url, json=params)
        return r.text

    def remove_applied_tags(self, contact_id, params):
        """
        url = f"{self.service_url}/{contact_id}/tags"
        r = self.infusionsoft.request('delete', url, json=params)
        return r.text
        """
        raise NotImplementedError

    def list_applied_tags(self, contact_id, params=None):
        """Retrieves a list of tags applied to a given contact. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/listAppliedTagsUsingGET>`

        Args:
            contact_id:
                The contact ID.
            params:
                Dictionary, bytes, or file-like object parameters for filtering tags. See the API reference for more information.

        Returns:
            The JSON result of the request containing tags applied to a contact.
        """
        url = f"{self.service_url}/{contact_id}/tags"
        r = self.infusionsoft.request('get', url, json=params)
        return r.text

    def apply_tags(self, contact_id, params):
        """Applies a list of tags to a given contact. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/applyTagsToContactIdUsingPOST>`.

        Args:
            contact_id:
                The contact ID.
            params:
                Dictionary, bytes, or file-like object parameters containing tag ids. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f"{self.service_url}/{contact_id}/tags"
        r = self.infusionsoft.request('post', url, json=params)
        return r.text

    def remove_applied_tag(self, contact_id, tag_id):
        """Applies a list of tags to a given contact. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/applyTagsToContactIdUsingPOST>`.

        Args:
            contact_id:
                The contact ID.
            tag_id:
                The tag ID that has to be removed.

        Returns:
            The JSON result of the request.
        """
        url = f"{self.service_url}/{contact_id}/tags/{tag_id}"
        r = self.infusionsoft.request('delete', url)
        return r.text

    def retrieve_contact(self, contact_id, params=None):
        """Retrieves a single contact. `API Reference <https://developer.infusionsoft.com/docs/rest/#!/Contact/getContactUsingGET>`.

        Args:
            contact_id:
                The contact ID.
            params:
                 Dictionary, bytes, or file-like object parameters containing contact properties to be included in the response. See the API reference for more information.

        Returns:
            The JSON request response containing the request contact properties.
        """
        url = f"{self.service_url}/{contact_id}"
        r = self.infusionsoft.request('delete', url, json=params)
        return r.text

    def retrieve_contact_model(self):
        """Gets the custom fields and optional properties for the Contact object

        Returns:
            The JSON request response containing the requested custom fields and optional properties of the model.
        """
        url = f"{self.service_url}/model"
        r = self.infusionsoft.request('delete', url)
        return r.text

    def create_custom_field(self, params):
        """Adds a custom field of the specified type and options to the Contact object.

        Args:
            params:

        Returns:
            The JSON request response.
        """
        url = f"{self.service_url}/model"
        r = self.infusionsoft.request('post', url, json=params)
        return r.text

    """Returns the service url of the REST endpoint.
    """
    def get_service_url(self):
        return self.service_url
