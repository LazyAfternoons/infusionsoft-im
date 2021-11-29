from abc import ABCMeta


class ApiModel(metaclass=ABCMeta):
    """Abstract class for defining a new API object"""

    def __init__(self, infusionsoft):
        self.infusionsoft = infusionsoft
        self.base_payload = {'access_token': self.infusionsoft.token.access_token}
        self.base_url = "https://api.infusionsoft.com/crm/rest/v1"
