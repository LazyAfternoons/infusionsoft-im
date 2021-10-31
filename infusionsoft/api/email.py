from infusionsoft.api.apimodel import ApiModel


class Email(ApiModel):
    """Email object for calling Infusionsoft API related to the remote Email Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Email object.`

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Email, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/emails'

    def list_emails(self, params=None):
        """Retrieve a list of emails that have been sent. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Email/listEmailsUsingGET>`

        Args:
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

         Returns:
             The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.service_url, params=params)

    def create_email_record(self, json):
        """Retrieve a list of emails that have been sent. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Email/createEmailUsingPOST>`

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
             The JSON result of the request.
        """
        return self.infusionsoft.request('post', self.service_url, json=json)

    def delete_email_record(self, email_id):
        """Delete a specific email record. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Email/deleteEmailUsingDELETE>`.

        Args:
            email_id:
                The id of the email record.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{email_id}'
        return self.infusionsoft.request('delete', url)

    def retrieve_email_record(self, email_id):
        """Retrieves a single email that has been sent. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Email/getEmailUsingGET>`.

        Args:
            email_id:
                The id of the email record.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{email_id}'
        return self.infusionsoft.request('get', url)

    def update_email_record(self, email_id, json):
        """Update a record of an email sent to a contact. Warning: DEPRECATED.`API reference <https://developer.infusionsoft.com/docs/rest/#!/Email/updateEmailUsingPUT>`

        Args:
            email_id:
                The id of the email record.

            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{email_id}'
        return self.infusionsoft.request('put', url, json=json)

    def update_email_record(self, json):
        """Send an Email to a list of Contacts. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Email/sendEmailUsingPOST>`

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/queue'
        return self.infusionsoft.request('post', url, json=json)

    def create_set_email_records(self, json):
        """Create a set of records of emails sent to contacts, maximum 1000 per transaction. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Email/createEmailsUsingPOST>`

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/queue'
        return self.infusionsoft.request('post', url, json=json)

    def unsync_batch_email_records(self, json):
        """Un-syncs a batch of email records. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Email/deleteEmailsUsingPOST>`

        Args:
            json: 
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/unsync'
        return self.infusionsoft.request('post', url, json=json)
