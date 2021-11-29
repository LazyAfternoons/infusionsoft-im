from infusionsoft.api.apimodel import ApiModel


class Tasks(ApiModel):
    """Setting object for calling Infusionsoft API related to the remote Tasks Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Tasks object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Tasks, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/tasks'

    def list_tasks(self, params=None):
        """Retrieves a list of all tasks using the specified search criteria. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Task/listTasksUsingGET>`.

        Args:
            params:
                Dictionary, list of tuples or bytes to send in the query string for the Request.
                See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        return self.infusionsoft.request('get', self.service_url, params=params)

    def create_task(self, json):
        """Creates a new task as the authenticated user. NB: Contact must contain at least one item in the fields
        title and due_date. All other attributes are optional. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Task/createTaskUsingPOST>`

        Returns:
            The JSON response of the request.
        """
        return self.infusionsoft.request('post', self.service_url, json=json)

    def delete_task(self, task_id):
        """Remove a tag from a list of contacts. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Task/deleteTaskUsingDELETE>`

        Args:
            task_id:
                The ID of the task.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{task_id}'
        return self.infusionsoft.request('delete', url)

    def retrieve_task(self, task_id):
        """Retrieves a single tag. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Task/getTaskUsingGET>`

        Args:
            task_id:
                The ID of the task.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{task_id}'
        return self.infusionsoft.request('get', url)

    def update_task(self, task_id, json):
        """Updates a task with only the values provided in the request. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Task/updatePropertiesOnTaskUsingPATCH>`

        Args:
            task_id:
                The ID of the task.
            json:
                A JSON serializable Python object to send in the body of the Request.
                See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{task_id}'
        return self.infusionsoft.request('patch', url, json)

    def replace_task(self, task_id, json):
        """Replaces a task with the values provided in the request. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Task/updateTaskUsingPUT>`

        Args:
            task_id:
                The ID of the task.
            json:
                A JSON serializable Python object to send in the body of the Request.
                See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{task_id}'
        return self.infusionsoft.request('put', url, json)

    def retrieve_task_model(self):
        """Get the custom fields for the Task object. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Task/retrieveTaskModelUsingGET>`

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/model'
        return self.infusionsoft.request('get', url)

    def create_custom_field(self, json):
        """Adds a custom field of the specified type and options to the Task object. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Task/createTaskCustomFieldUsingPOST>`

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request.
                See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/model/customFields'
        return self.infusionsoft.request('post', url, json)

    def search_tasks(self, params):
        """Retrieves Tasks belonging to the authenticated user using the specified search criteria. `API reference
        <https://developer.infusionsoft.com/docs/rest/#!/Task/listTasksForCurrentUserUsingGET>`

        Args:
            params:
                Dictionary, list of tuples or bytes to send in the query string for the Request.
                See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/search'
        return self.infusionsoft.request('get', url, params=params)
