from infusionsoft.api.apimodel import ApiModel


class Note(ApiModel):
    """Note object for calling Infusionsoft API related to the remote Note Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Note object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Note, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/notes'

    def list_notes(self):
        """Retrieves a list of all notes

        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.service_url)

    def create_note(self, json):
        """Creates a new note as the authenticated user. Either a "title" or "body" is required

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('post', self.service_url, json=json)

    def delete_note(self, note_id):
        """Deletes a note. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Note/deleteNoteUsingDELETE>`.

        Args:
            note_id: The ID of the note to be deleted.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{note_id}'
        return self.infusionsoft.request('delete', url)

    def retrieve_note(self, note_id):
        """Retrieves a single note. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Note/getNoteUsingGET>`.

        Args:
            note_id: The ID of the note to be deleted.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{note_id}'
        return self.infusionsoft.request('get', url)

    def update_note(self, note_id, json):
        """Retrieves a single note. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Note/updatePropertiesOnNoteUsingPATCH>`.

        Args:
            note_id:
                The ID of the note to be deleted.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{note_id}'
        return self.infusionsoft.request('patch', url, json=json)

    def replace_note(self, note_id, json):
        """Replaces all values of a given note. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Note/updateNoteUsingPUT>`.

        Args:
            note_id:
                The ID of the note to be deleted.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{note_id}'
        return self.infusionsoft.request('put', url, json=json)

    def retrieve_note_model(self):
        """Replaces all values of a given note. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Note/retrieveNoteModelUsingGET>`.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/model'
        return self.infusionsoft.request('get', url)

    def create_custom_field(self, json):
        """Adds a custom field of the specified type and options to the Note object. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Note/createNoteCustomFieldUsingPOST>`.

        Args:
            note_id:
                The ID of the note to be deleted.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/model/customFields'
        return self.infusionsoft.request('post', url, json=json)




