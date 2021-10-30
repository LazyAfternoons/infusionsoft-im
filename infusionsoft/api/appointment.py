from infusionsoft.api.apimodel import ApiModel


class Appointment(ApiModel):
    """Appointment object for calling Infusionsoft API related to the remote Appointment object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Appointment object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Appointment, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/appointments'

    def list_appointments(self, params=None):
        """Retrieves all appointments for the authenticated user. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Appointment/listAppointmentsUsingGET>`.

        Args:
            params:
                Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.service_url, params)

    def create_appointment(self, json=None):
        """Creates a new appointment as the authenticated user. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Appointment/createAppointmentUsingPOST>`.

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        return self.infusionsoft.request('post', self.service_url, json=json)

    def delete_appointment(self, appointment_id):
        """Creates a new appointment as the authenticated user. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Appointment/createAppointmentUsingPOST>`.

        Args:
            appointment_id:
                The id of the appointment.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{appointment_id}'
        return self.infusionsoft.request('delete', url)

    def retrieve_appointment(self, appointment_id):
        """Retrieves a specific appointment with respect to user permissions. The authenticated user will need the "can view all records" permission for Task/Appt/Notes. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Appointment/getAppointmentUsingGET>`.

        Args:
            appointment_id:
                The id of the appointment.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{appointment_id}'
        return self.infusionsoft.request('get', url)

    def update_appointment(self, appointment_id, json):
        """Updates the provided values of a given appointment. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Appointment/updatePropertiesOnAppointmentUsingPATCH>`.

        Args:
            appointment_id:
                The id of the appointment.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{appointment_id}'
        return self.infusionsoft.request('patch', url, json=json)

    def replace_appointment(self, appointment_id, json):
        """Replaces all values of a given appointment. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Appointment/updateAppointmentUsingPUT>`.

        Args:
            appointment_id:
                The id of the appointment.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/{appointment_id}'
        return self.infusionsoft.request('patch', url, json=json)

    def replace_appointment_model(self):
        """Get the custom fields for the Appointment object. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Appointment/retrieveAppointmentModelUsingGET>`.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/model'
        return self.infusionsoft.request('get', url)

    def create_custom_field(self, json):
        """Adds a custom field of the specified type and options to the Appointment object. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Appointment/createAppointmentCustomFieldUsingPOST>`.

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON result of the request.
        """
        url = f'{self.service_url}/model/customFields'
        return self.infusionsoft.request('post', url, json=json)
