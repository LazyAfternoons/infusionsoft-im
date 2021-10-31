from infusionsoft.api.apimodel import ApiModel


class Product(ApiModel):
    """Product object for calling Infusionsoft API related to the remote Product Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Product object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Product, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/products'

    def list_product(self, params=None):
        """Retrieves a list of all products. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Product/listProductsUsingGET>`.

        Args:
            params:
                Dictionary, list of tuples or bytes to send in the query string for the Request. See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        return self.infusionsoft.request('get', self.service_url, params=params)

    def create_product(self, json):
        """Creates a new product. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Product/createProductUsingPOST>`.

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        return self.infusionsoft.request('post', self.service_url, json=json)

    def delete_product(self, product_id):
        """Deletes a product and its subscriptions. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Product/deleteProductUsingDELETE>`.

        Args:
            product_id:
                The ID of the product to be deleted.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{product_id}'
        return self.infusionsoft.request('delete', url)

    def retrieve_product(self, product_id):
        """Retrieves a single product. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Product/retrieveProductUsingGET>`.

        Args:
            product_id:
                The ID of the product to be deleted.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{product_id}'
        return self.infusionsoft.request('get', url)

    def update_product(self, product_id, json=None):
        """Updates a Product with only the values provided in the request. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Product/updateProductUsingPATCH>`.

        Args:
            product_id:
                The ID of the product to be deleted.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{product_id}'
        return self.infusionsoft.request('patch', url)

    def delete_product_image(self, product_id):
        """Updates a Product with only the values provided in the request. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Product/updateProductUsingPATCH>`.

        Args:
            product_id:
                The ID of the product to be deleted.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{product_id}/image'
        return self.infusionsoft.request('delete', url)

    def upload_product_image(self, product_id, json):
        """Updates a Product image. Max payload 3 megabytes, the file_data is base64 encoded. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Product/updateProductUsingPATCH>`.

        Args:
            product_id:
                The ID of the product to be deleted.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{product_id}/image'
        return self.infusionsoft.request('post', url, json=json)

    def create_product_subscription(self, product_id, json):
        """Creates a new product subscription. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Product/createProductSubscriptionUsingPOST>`.

        Args:
            product_id:
                The ID of the product to be deleted.
            json:
                A JSON serializable Python object to send in the body of the Request. See the API reference for more information.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{product_id}/subscriptions'
        return self.infusionsoft.request('post', url, json=json)

    def delete_product_subscription(self, product_id, subscription_id):
        """Creates a new product subscription. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Product/deleteProductSubscriptionUsingDELETE>`.

        Args:
            product_id:
                The ID of the product to be deleted.
            subscription_id:
                The ID of the subscription.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{product_id}/subscriptions/{subscription_id}'
        return self.infusionsoft.request('delete', url)

    def retrieve_product_subscription(self, product_id, subscription_id):
        """Retrieves a product subscription. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Product/retrieveProductSubscriptionUsingGET>`.

        Args:
            product_id:
                The ID of the product to be deleted.
            subscription_id:
                The ID of the subscription.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/{product_id}/subscriptions/{subscription_id}'
        return self.infusionsoft.request('get', url)

    def retrieve_synced_products(self, params=None):
        """The Sync endpoint returns a set of products that have been updated or created since the last result set was retrieved, minus any products that have been deleted. `API reference <https://developer.infusionsoft.com/docs/rest/#!/Product/retrieveProductSubscriptionUsingGET>`.
        WARNING: DEPRECATED.

        Returns:
            The JSON response of the request.
        """
        url = f'{self.service_url}/sync'
        return self.infusionsoft.request('get', url, params=params)


