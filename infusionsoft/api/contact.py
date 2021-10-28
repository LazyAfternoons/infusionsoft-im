class Contact:


    def __init__(self, infusionsoft):
        self.infusionsoft = infusionsoft
        self.base_payload = {'access_token': self.infusionsoft.token.access_token}
        self.service_url = 'https://api.infusionsoft.com/crm/rest/v1/contacts'

    def list_contact(self):
        r = self.infusionsoft.request('get', self.service_url)
        return r.text

    def create_contact(self, params):
        r = self.infusionsoft.request('post', self.service_url, json=params)
        return r.text

    def create_update_contact(self, params):
        r = self.infusionsoft.request('put', self.service_url, json=params)
        return r.text

    def delete_contact(self, contact_id):
        url = f"{self.service_url}/{contact_id}"
        r = self.infusionsoft.request('delete', url)
        return r.text

    def update_contact(self, contact_id, params):
        url = f"{self.service_url}/{contact_id}"
        r = self.infusionsoft.request('patch', url, json=params)
        return r.text

    def retrieve_credit_cards(self, contact_id):
        url = f"{self.service_url}/{contact_id}/creditCards"
        r = self.infusionsoft.request('get', url)
        return r.text

    def create_credit_card(self, contact_id):
        url = f"{self.service_url}/{contact_id}/creditCards"
        r = self.infusionsoft.request('post', url)
        return r.text

    def list_emails(self, contact_id, params):
        url = f"{self.service_url}/{contact_id}/emails"
        r = self.infusionsoft.request('get', url, json=params)
        return r.text

    def create_email_record(self, contact_id, params):
        url = f"{self.service_url}/{contact_id}/emails"
        r = self.infusionsoft.request('post', url, json=params)
        return r.text

    def remove_applied_tags(self, contact_id, params):
        url = f"{self.service_url}/{contact_id}/tags"
        r = self.infusionsoft.request('delete', url, json=params)
        return r.text

    def list_applied_tags(self, contact_id, params=None):
        url = f"{self.service_url}/{contact_id}/tags"
        r = self.infusionsoft.request('get', url, json=params)
        return r.text

    def apply_tags(self, contact_id, params):
        url = f"{self.service_url}/{contact_id}/tags"
        r = self.infusionsoft.request('post', url, json=params)
        return r.text

    def remove_applied_tag(self, contact_id, tag_id):
        url = f"{self.service_url}/{contact_id}/tags/{tag_id}"
        r = self.infusionsoft.request('delete', url)
        return r.text

    def retrieve_contact(self, contact_id, params=None):
        url = f"{self.service_url}/{contact_id}"
        r = self.infusionsoft.request('delete', url, json=params)
        return r.text

    def retrieve_contact_model(self):
        url = f"{self.service_url}/model"
        r = self.infusionsoft.request('delete', url)
        return r.text

    def create_custom_field(self, params):
        url = f"{self.service_url}/model"
        r = self.infusionsoft.request('post', url, json=params)
        return r.text
