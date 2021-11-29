from infusionsoft.api.apimodel import ApiModel


class RestHook(ApiModel):
    """RestHook object for calling Infusionsoft API related to the remote RestHook Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new RestHook object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(RestHook, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/hooks'

    def list_hook_event_types(self):
        """List hook event types.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/REST_Hooks/list_hook_event_types>`.

         Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/hooks/event_keys'
        return self.infusionsoft.request('get', url)

    def create_hook_subscription(self, json):
        """Creates a hook subscriptions.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/REST_Hooks/create_a_hook_subscription>`

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request.
                See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        return self.infusionsoft.request('post', self.service_url, json=json)

    def verify_hook_subscription(self, key):
        """This operation is used to verify or reactivate a hook subscription
        using RESTHooks.org's Immediate Confirmation pattern.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/REST_Hooks/verify_a_hook_subscription>`

        Args:
            key:
                The key of the hook subscription.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{key}/verify'
        return self.infusionsoft.request('post', url)

    def verify_hook_subscription_delayed(self, key, x_hook_secret):
        """This operation is used to verify or reactivate a hook subscription out-of-band
        using RESTHooks.org's Delayed Confirmation pattern.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/REST_Hooks/verify_a_hook_subscription_delayed>`

        Args:
            key:
                The key of the hook subscription.
            x_hook_secret:
                X hook secret which allows you to confirm a subscription.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{key}/delayedVerify'
        headers = {'X-Hook-Secret': x_hook_secret}
        return self.infusionsoft.request('post', url, headers=headers)

    def list_stored_hook_subscriptions(self):
        """Lists your hook subscriptions.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/REST_Hooks/list_stored_hook_subscriptions>`

        Returns:
            The JSON response of the request.
        """
        return self.infusionsoft.request('get', self.service_url)

    def retrieve_hook_subscription(self, key):
        """Retrieves an existing hook subscription and its status.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/REST_Hooks/retrieve_a_hook_subscription>`.

        Args:
            key:
                The key of the hook subscription.
        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{key}'
        return self.infusionsoft.request('get', url)

    def update_hook_subscription(self, key, json):
        """Modify an existing hook subscription using the provided values.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/REST_Hooks/update_a_hook_subscription>`.

        Args:
            key:
                The key of the hook subscription.

            json:
                A JSON serializable Python object to send in the body of the Request.
                See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{key}'
        return self.infusionsoft.request('put', url, json=json)

    def delete_hook_subscription(self, key):
        """Stop receiving hooks by deleting an existing hook subscription.
        `API reference <https://developer.infusionsoft.com/docs/rest/#!/REST_Hooks/delete_a_hook_subscription>`.

        Args:
            key:
                The key of the hook subscription.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{key}'
        return self.infusionsoft.request('delete', url)
