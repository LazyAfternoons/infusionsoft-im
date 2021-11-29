from infusionsoft.api.apimodel import ApiModel


class Ecommerce(ApiModel):
    """Ecommerce object for calling Infusionsoft API related to the remote Ecommerce Info object.
    """

    def __init__(self, infusionsoft):
        """Creates a new Ecommerce object.

        Args:
            infusionsoft: the Infusionsoft object representing the client.
        """
        super(Ecommerce, self).__init__(infusionsoft)
        self.service_url = f'{self.base_url}/orders'
        self.subscription_url = f'{self.base_url}/subscriptions'
        self.transactions_url = f'{self.base_url}/transactions'

    def list_orders(self, params=None):
        """Retrieves a list of all orders using the specified search criteria. Each order may or may not have items.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/listOrdersUsingGET>`.

         Args:
             params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request.
                 See the API reference for more information.

         Returns:
             The JSON result of the request.
         """
        return self.infusionsoft.request('get', self.service_url, params=params)

    def create_order(self, json):
        """Create a one time order with order items.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/createOrderUsingPOST>`.

         Args:
             json:
                A JSON serializable Python object to send in the body of the Request.
                See the API reference for more information.

         Returns:
             The JSON result of the request.
         """
        return self.infusionsoft.request('post', self.service_url, json=json)

    def delete_order(self, order_id):
        """Delete an order that does not have a payment.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/deleteOrderUsingDELETE>`.

         Args:
             order_id:
                The ID of the order.

         Returns:
             The JSON result of the request.
        """
        url = f'{self.service_url}/{order_id}'
        return self.infusionsoft.request('delete', url)

    def retrieve_order(self, order_id):
        """Retrieves a single order. The order may or may not have items.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/getOrderUsingGET>`.

         Args:
             order_id:
                The ID of the order.

         Returns:
             The JSON result of the request.
        """
        url = f'{self.service_url}/{order_id}'
        return self.infusionsoft.request('get', url)

    def create_order_item(self, order_id, json):
        """Creates an order item on an existing order. The order may or may not have items. `
        API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/createOrderItemsOnOrderUsingPOST>`.

        Args:
            order_id:
                The ID of the order.
            json:
                A JSON serializable Python object to send in the body of the Request.
                See the API reference for more information.

         Returns:
             The JSON result of the request.
        """
        url = f'{self.service_url}/{order_id}/items'
        return self.infusionsoft.request('post', url, json=json)

    def delete_order_item(self, order_id, order_item_id):
        """Delete an order Item on specified Order. The order may or may not have items.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/deleteOrderOrderItemUsingDELETE>`.

        Args:
            order_id:
                The ID of the order.
            order_item_id:
                The ID of the order item.

         Returns:
             The JSON result of the request.
        """
        url = f'{self.service_url}/{order_id}/items/{order_item_id}'
        return self.infusionsoft.request('delete', url)

    def replace_order_payplan(self, order_id, json):
        """Delete an order Item on specified Order. The order may or may not have items.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/deleteOrderOrderItemUsingDELETE>`.

        Args:
            order_id:
                The ID of the order.
            json:
                A JSON serializable Python object to send in the body of the Request.
                See the API reference for more information.

         Returns:
             The JSON result of the request.
        """
        url = f'{self.service_url}/{order_id}/paymentPlan'
        return self.infusionsoft.request('put', url, json=json)

    def retrieve_order_payments(self, order_id):
        """Retrieves a list of payments made against a given order,
        including historical or external payments of cash or credit card.
        The order may or may not have items.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/listOrderPaymentsUsingGET>`.

        Args:
            order_id:
                The ID of the order.

         Returns:
             The JSON result of the request.
        """
        url = f'{self.service_url}/{order_id}/payments'
        return self.infusionsoft.request('get', url)

    def create_payment(self, order_id, json):
        """Creates a payment record that can charge a credit card. Alternatively,
        adds a record of historical or external payment of cash or credit card. The order may or may not have items.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/createPaymentOnOrderUsingPOST>`.

        Args:
            order_id:
                The ID of the order.
            json:
                A JSON serializable Python object to send in the body of the Request.
                See the API reference for more information.


         Returns:
             The JSON result of the request.
        """
        url = f'{self.service_url}/{order_id}/payments'
        return self.infusionsoft.request('post', url, json=json)

    def retrieve_order_transactions(self, order_id, params):
        """Retrieves a list of all transactions on a given order using the specified search criteria.
        The order may or may not have items.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/listTransactionsForOrderUsingGET>`.

        Args:
            order_id:
                The ID of the order.
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request.
                 See the API reference for more information.

         Returns:
             The JSON result of the request.
        """
        url = f'{self.service_url}/{order_id}/transactions'
        return self.infusionsoft.request('get', url, params=params)

    def retrieve_custom_order_model(self):
        """Get the custom fields for the Order object. The order may or may not have items.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/retrieveOrderModelUsingGET>`.

         Returns:
             The JSON result of the request.
        """
        url = f'{self.service_url}/model'
        return self.infusionsoft.request('get', url)

    def list_subscriptions(self):
        """Retrieves a list of all subscriptions using the specified search criteria.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/listSubscriptionsUsingGET>`.

         Returns:
             The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.subscription_url)

    def create_subscriptions(self, json):
        """Creates a subscription with the specified product and product subscription id.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/createSubscriptionUsingPOST>`.

        Args:
            json:
                A JSON serializable Python object to send in the body of the Request.
                See the API reference for more information.

         Returns:
             The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.subscription_url, json=json)

    def retrieve_subscription_model(self):
        """Get the custom fields for the Subscription object.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/retrieveSubscriptionModelUsingGET>`.

         Returns:
             The JSON result of the request.
        """
        url = f'{self.subscription_url}/model'
        return self.infusionsoft.request('get', url)

    def list_transactions(self, params=None):
        """Retrieves a list transactions for a given contact.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/listTransactionsUsingGET>`.

        Args:
            params:
                 Dictionary, list of tuples or bytes to send in the query string for the Request.
                 See the API reference for more information.

         Returns:
             The JSON result of the request.
        """
        return self.infusionsoft.request('get', self.transactions_url, params)

    def retrieve_transaction(self, transaction_id):
        """Retrieves a single transaction.
        `API Reference <https://developer.infusionsoft.com/docs/rest/#!/E-Commerce/getTransactionUsingGET>`.

        Args:
            transaction_id:
                 The ID of the transaction.

         Returns:
             The JSON result of the request.
        """
        url = f'{self.transactions_url}/{transaction_id}'
        return self.infusionsoft.request('get', url)
