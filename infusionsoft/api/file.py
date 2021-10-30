from infusionsoft.api.apimodel import ApiModel


class File(ApiModel):
    def __init__(self, infusionsoft):
        """Creates a new EmailAddress object. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Email/listEmailsUsingGET>`

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(File, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/files'

    def list_files(self, params=None):
        """Retrieves a list of all files. `API reference <https://developer.infusionsoft.com/docs/rest/#!/File/listFilesUsingGET>`

        Args:
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.service_url, params)

    def upload_files(self, json):
        """Upload a base64 encoded file. contact_id is required only when file_association is CONTACT. `API reference <https://developer.infusionsoft.com/docs/rest/#!/File/createFileUsingPOST>`.

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.
        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('post', self.service_url, json=json)

    def delete_file(self, file_id):
        """Deletes the specified file. `API reference <https://developer.infusionsoft.com/docs/rest/#!/File/deleteFileUsingDELETE>`.

        Args:
            file_id:
                The ID of the file to be deleted.
        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{file_id}'
        return self.infusionsoft.request('delete', url)

    def retrieve_file(self, file_id, params):
        """Retrieves metadata about a specific file. Optionally returns the base64 encoded file data. `API reference <https://developer.infusionsoft.com/docs/rest/#!/File/getFileUsingGET>`.

        Args:
            file_id:
                The ID of the file to be deleted.

            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.
        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{file_id}'
        return self.infusionsoft.request('get', url, params=params)

    def replace_file(self, file_id, json):
        """Upload a base64 encoded file to replace an existing one. contact_id is required only when file_association is CONTACT. `API reference <https://developer.infusionsoft.com/docs/rest/#!/File/updateFileUsingPUT>`.

        Args:
            file_id:
                The ID of the file to be deleted.

            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{file_id}'
        return self.infusionsoft.request('get', url, json=json)